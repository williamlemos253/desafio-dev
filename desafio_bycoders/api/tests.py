from django.test import TestCase
from rest_framework.test import APITestCase
from cnab_reader.models import cnabModel
from cnab_reader.use_cases.cnab_reader_use_case import CnabReaderUseCase
from rest_framework.test import APIRequestFactory
from .views import CnabReaderAPIView

# Create your tests here.
class CnabReaderAPIViewTestCase(APITestCase):
    def setUp(self):
        data = b'3201903010000014200096206760174753****3153153453JO\xc3\x83O MACEDO   BAR DO JO\xc3\x83O       \n3201903010000019200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA\n'
        CnabReaderUseCase().execute(data)

    def test_cnab_reader_api_view(self):
        view = CnabReaderAPIView.as_view()
        factory = APIRequestFactory()
        request = factory.get('/api/cnab/', format='json')
        response = view(request)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), 2)

    def test_cnab_reader_filter_api_view(self):
        view = CnabReaderAPIView.as_view()
        factory = APIRequestFactory()
        test = cnabModel.objects.all()
        request = factory.get('/api/cnab/BAR%20DO%20JOÃO')
        response = view(request)
        self.assertEquals(response.status_code, 200)

        