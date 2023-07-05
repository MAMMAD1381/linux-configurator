import os

class Rule:
    
    PATH_CONFIG = '../../scripts/nft/Rule/'
    rules = {}
    chain_type: str


    def __init__(self):
        os.system(f'bash {self.PATH_CONFIG}../dependencies.sh nftables')

    def add_rule(self, family_type, table_name, chain_name, handle, statement):
        os.system(f'bash {self.PATH_CONFIG}add.sh {family_type} {table_name} {chain_name} {handle} {statement}')

    def replace_rule(self, family_type, table_name, chain_name, handle, statement):
        os.system(f'bash {self.PATH_CONFIG}replace.sh {family_type} {table_name} {chain_name} {handle} {statement}')

    def delete_rule(self):
        os.system(f'bash {self.PATH_CONFIG}delete.sh {family_type} {table_name} {chain_name} {handle}')

    def reset_rules(self, family_type, table_name, chain_name):
        os.system(f'bash {self.PATH_CONFIG}reset.sh {family_type} {table_name} {chain_name}')


if __name__=='__main__':
    rule = Rule()
    # rule.reset_rules('ip', 'my_tables', 'my_chain')