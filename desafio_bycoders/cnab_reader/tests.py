from django.test import TestCase
from .use_cases.cnab_reader_use_case import CnabReaderUseCase
from .use_cases.operations_list_use_case import OperationsListUseCase
from .repository import CnabRepository
import datetime

# Create your tests here.
class CnabReaderTestCase(TestCase):

    def test_cnab_reader_use_case(self):
        data = b'3201903010000014200096206760174753****3153153453JO\xc3\x83O MACEDO   BAR DO JO\xc3\x83O       \n'
        use_case_return = CnabReaderUseCase().execute(data)
        self.assertNotEqual(use_case_return, '3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO')

    def test_cnab_repository_create_transation(self):
        data = {'tipo_transacao': '3', 'data': datetime.date(2019, 3, 1), 'valor': -103.0, 'cpf': '23270298056', 'cartao': '6777****1313', 'hora_transacao': datetime.time(17, 27, 12), 'nome_dono_loja': 'JOSÉ COSTA', 'nome_loja': 'MERCEARIA 3 IRMÃOS'}
        CnabRepository().create_transation(data)
        formatted_query, total_value = CnabRepository().get_transaction_by_store_name('MERCEARIA 3 IRMÃOS')
        self.assertEqual(formatted_query[0]['nome_loja'], 'MERCEARIA 3 IRMÃOS')
        self.assertEqual(total_value, '-103.00')

    def test_operations_list_use_case(self):
        data = b'3201903010000014200096206760174753****3153153453JO\xc3\x83O MACEDO   BAR DO JO\xc3\x83O       \n'
        data2 = b'3201903010000019200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA\n'
        store_name = None

        use_case_return, total = OperationsListUseCase().execute(store_name)
        self.assertEqual(len(use_case_return), 0)

        CnabReaderUseCase().execute(data)
        use_case_return, total = OperationsListUseCase().execute(store_name)
        self.assertEqual(len(use_case_return), 1)
        self.assertEqual(total, None)

        CnabReaderUseCase().execute(data2)
        use_case_return, total = OperationsListUseCase().execute(store_name)      
        self.assertEqual(len(use_case_return), 2)

        store_name2 = 'MERCADO DA AVENIDA'
        use_case_return, total = OperationsListUseCase().execute(store_name2)
        self.assertEqual(len(use_case_return), 1)

        store_name3 = 'BAR DO JOÃO'
        use_case_return, total = OperationsListUseCase().execute(store_name3)
        self.assertEqual(len(use_case_return), 1)
        self.assertEqual(total, '-142.00')




    

