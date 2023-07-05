from .Table import Table
from .Chain import Chain
from .Rule import Rule

class NftableHandler:

    def __init__(self):
        while True:
            selected_option = self.main_menu()

            match selected_option:
                
                case '1':
                    Table()
                case '2':
                    Chain()
                case '3':
                    Rule()
                case '4':
                    break


    def main_menu(self):

        print('pls select a section:')
        print('1. Table')
        print('2. Chain')
        print('3. Rule')
        print('4. back')

        return input()