from ..formatter import CnabFormatter
from ..repository import CnabRepository

class CnabReaderUseCase():
    def __init__(self, cnab_reader_repository = None):
        self.cnab_formatter = CnabFormatter()
        self.cnab_reader_repository = cnab_reader_repository or CnabRepository()

    def execute(self, cnab_file):
        cnab_file = cnab_file.decode('utf-8')
        for line in cnab_file.splitlines():
            cnab_formatter = self.cnab_formatter.cnab_formatted(line)
            self.cnab_reader_repository.create_transation(cnab_formatter)
        return cnab_file