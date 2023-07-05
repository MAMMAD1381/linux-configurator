import os

class Table:

    PATH_CONFIG = '../../scripts/nft/Table/'
    family_types = ['ip', 'ip6', 'inet', 'arp', 'bridge']

    def __init__(self):
        os.system(f'bash {self.PATH_CONFIG}../dependencies.sh nftables')

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

if __name__=='__main__':
    table_handler = Table()
    table_handler.add_table('ip', 'my_tables')
    # table_handler.delete_table('my_tables', 'ip')
    # table_handler.flush_table('my_tables', 'ip')
    table_handler.list_table('', '')



    table_handler.list_table('', '')