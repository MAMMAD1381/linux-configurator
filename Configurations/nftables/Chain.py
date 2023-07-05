import os

class Chain:

    PATH_CONFIG = '../../scripts/nft/Chain/'
    name: str
    family_type: str
    chains = {}
    chain_types = ['filter', 'route','nat']
    filter_type_supported_by = ['ip', 'ip6', 'inet', 'arp', 'bridge']
    nat_type_supported_by = ['ip', 'ip6', 'inet']
    route_type_supported_by = ['ip', 'ip6']
    ipv4_hook_types = ['prerouting', 'input', 'forward', 'output', 'postrouting', 'egress']
    ipv6_hook_types = ipv4_hook_types
    inet_hook_types = ipv4_hook_types
    arp_hook_types = ['input', 'output']
    bridge_hoo_types = ipv4_hook_types
    netdev_hook_types = ['ingress', 'egress']
    

    def __init__(self):
        os.system(f'bash {self.PATH_CONFIG}../dependencies.sh nftables')

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
    
if __name__=='__main__':
    chain = Chain()
    chain.add_chain('ip', 'my_tables', 'my_chain', 'filter', 'output', '3', 'drop')
    # chain.delete_chain('ip', 'my_tables', 'my_chains')
    # chain.rename_chain('ip', 'my_tables', 'my_chain', 'me')
    # chain.flush_chain('ip', 'my_tables', 'my_chain')
    chain.list_chain('ip', '', '')