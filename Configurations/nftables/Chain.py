import os

class Chain:

    PATH_CONFIG = './scripts/nft/Chain/'
    # name: str
    # family_type: str
    # chains = {}
    # chain_types = ['filter', 'route','nat']
    # filter_type_supported_by = ['ip', 'ip6', 'inet', 'arp', 'bridge']
    # nat_type_supported_by = ['ip', 'ip6', 'inet']
    # route_type_supported_by = ['ip', 'ip6']
    # ipv4_hook_types = ['prerouting', 'input', 'forward', 'output', 'postrouting', 'egress']
    # ipv6_hook_types = ipv4_hook_types
    # inet_hook_types = ipv4_hook_types
    # arp_hook_types = ['input', 'output']
    # bridge_hoo_types = ipv4_hook_types
    # netdev_hook_types = ['ingress', 'egress']
    

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
                    chain_type = input('pls enter the chain type: ')
                    hook = input('pls enter the hook type: ')
                    priority = input('pls enter the chain priority: ')
                    policy = input('pls enter the chain policy: ')
                    
                    self.add_chain(family_type, table_name, chain_name, chain_type, hook, priority, policy)
                
                case '2':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    chain_name = input('pls enter the chain name: ')

                    self.delete_chain(family_type, table_name, chain_name)
                
                case '3':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    chain_name = input('pls enter the chain name: ')

                    self.list_chain(family_type, table_name, chain_name)
                
                case '4':
                    family_type = input('pls enter the family type: ')
                    self.list_chain(family_type, '', '')

                case '5':
                    family_type = input('pls enter the family type: ')
                    table_name = input('pls enter the table name: ')
                    chain_name = input('pls enter the chain name: ')
                    new_name = input('pls enter the new name: ')
                    self.rename_chain(family_type, table_name, chain_name, new_name)

                case '6':
                    break

    def add_chain(self, family_type, table_name, chain_name, chain_type, hook, priority, policy):
        os.system(f'bash {self.PATH_CONFIG}add.sh {family_type} {table_name} {chain_name} {chain_type} {hook} {priority} {policy}')

    def delete_chain(self, family_type, table_name, chain_name):
        os.system(f'bash {self.PATH_CONFIG}delete.sh {family_type} {table_name} {chain_name}')

    def rename_chain(self, family_type, table_name, chain_name, new_name):
        os.system(f'bash {self.PATH_CONFIG}rename.sh {family_type} {table_name} {chain_name} {new_name}')

    def list_chain(self, family_type, table_name, chain_name):
        if family_type and table_name and chain_name:
            os.system(f'bash {self.PATH_CONFIG}list.sh {family_type} {table_name} {chain_name}')
        elif family_type:
            os.system(f'bash {self.PATH_CONFIG}list.sh {family_type}')

    def flush_chain(self, family_type, table_name, chain_name):
        os.system(f'bash {self.PATH_CONFIG}flush.sh {family_type} {table_name} {chain_name}')
    
    def main_menu(self):

        print('pls select a section:')
        print('1. add chain')
        print('2. delete chain')
        print('3. list chain')
        print('4. list a family chains')
        print('5. rename chain')
        print('6. back')

        return input()