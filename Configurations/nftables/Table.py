import os

class Table:

    PATH_CONFIG = './scripts/nft/Table/'
    family_types = ['ip', 'ip6', 'inet', 'arp', 'bridge']

    def __init__(self):
        # checking for dependencies
        os.system(f'bash ./scripts/nft/dependencies.sh nftables')

        while True:
            selected_option = self.main_menu()

            match selected_option:
                
                case '1':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    self.add_table(family_type, table_name)
                
                case '2':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    self.delete_table(family_type, table_name)
                
                case '3':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    self.list_table(family_type, table_name)
                
                case '4':
                    self.list_table('', '')

                case '5':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    self.flush_table(family_type, table_name)

                case '6':
                    break
        

    def add_table(self, family_type, name):
        if name and family_type in self.family_types:
            os.system(f'bash {self.PATH_CONFIG}add.sh {family_type} {name}')
        else:
            print('an ERROR occured pls enter the right arguments')

    def delete_table(self, family_type, name):
        if name and family_type in self.family_types:
            os.system(f'bash {self.PATH_CONFIG}delete.sh {family_type} {name}')
        else: print('an ERROR occured pls enter the right arguments')
        

    def list_table(self, family_type, name):
        if name and family_type in self.family_types:
            os.system(f'bash {self.PATH_CONFIG}list.sh {family_type} {name}')
        else: os.system(f'bash {self.PATH_CONFIG}list.sh')


    def flush_table(self, family_type, name):
        if name and family_type in self.family_types:
            os.system(f'bash {self.PATH_CONFIG}flush.sh {family_type} {name}')
        else:
            print('an ERROR occured pls enter the right arguments')


    def main_menu(self):

        print('pls select a section:')
        print('1. add table')
        print('2. delete table')
        print('3. list table')
        print('4. list tables')
        print('5. flush table')
        print('6. back')

        return input()