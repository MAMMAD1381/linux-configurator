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

    def add_chain(self, family_type, table_name, chain_name, chain_type, hook, priority):
        os.system(f'bash {self.PATH_CONFIG}add.sh {family_type} {table_name} {chain_name} {chain_type} {hook} {priority}')

    def delete_chain(self):
        pass

    def edit_chain(self):
        pass

    def list_chain(self):
        pass

    def flush_chain(self):
        pass
    