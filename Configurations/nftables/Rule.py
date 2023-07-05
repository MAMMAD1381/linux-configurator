import os

class Rule:
    
    PATH_CONFIG = './scripts/nft/Rule/'

    def __init__(self):
        # checking for dependencies
        os.system(f'bash ./scripts/nft/dependencies.sh nftables')

        while True:
            selected_option = self.main_menu()

            match selected_option:
                
                case '1':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    chain_name = input('pls enter the chain name: ')
                    handle = input('pls enter the handle: ')
                    statement = input('pls enter the statement: ')
                    
                    self.add_rule(family_type, table_name, chain_name, handle, statement)
                
                case '2':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    chain_name = input('pls enter the chain name: ')
                    handle = input('pls enter the handle: ')
                    statement = input('pls enter the statement: ')
                    
                    self.replace_rule(family_type, table_name, chain_name, handle, statement)
                
                case '3':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    chain_name = input('pls enter the chain name: ')
                    handle = input('pls enter the handle: ')
                    
                    self.delete_rule(family_type, table_name, chain_name, handle)
                
                case '4':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    chain_name = input('pls enter the chain name: ')

                    self.reset_rules(family_type, table_name, chain_name)

                case '5':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')

                    self.reset_rules(family_type, table_name, '')

                case '6':
                    family_type = input('pls enter the family type: ')

                    self.reset_rules(family_type, '', '')

                case '7':
                    break


    def add_rule(self, family_type, table_name, chain_name, handle, statement):
        os.system(f'bash {self.PATH_CONFIG}add.sh {family_type} {table_name} {chain_name} {handle} {statement}')

    def replace_rule(self, family_type, table_name, chain_name, handle, statement):
        os.system(f'bash {self.PATH_CONFIG}replace.sh {family_type} {table_name} {chain_name} {handle} {statement}')

    def delete_rule(self):
        os.system(f'bash {self.PATH_CONFIG}delete.sh {family_type} {table_name} {chain_name} {handle}')

    def reset_rules(self, family_type, table_name, chain_name):
        os.system(f'bash {self.PATH_CONFIG}reset.sh {family_type} {table_name} {chain_name}')

   
    def main_menu(self):

        print('pls select a section:')
        print('1. add rule')
        print('2. replace rule')
        print('3. delete rule')
        print('4. reset rules on chain')
        print('5. reset rules on table')
        print('6. reset rules on family type')
        print('7. back')

        return input()