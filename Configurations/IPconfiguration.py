import os

class IPconfiguratoin:
    def __init__(self):
        self.PATH_CONFIG = '../scripts/IP/'

    def changeIP_temporary(self, interface, ip, mask):
        os.system(f'bash {self.PATH_CONFIG}temporary/set.sh {interface} {ip} {mask}')

    def changeIP_permanently(self, interface, ip, mask, gateway, dns1, dns2):
        os.system(f'bash {self.PATH_CONFIG}permanently/set.sh {interface} {ip} {mask} {gateway} {dns1} {dns2}')
    
    def restore_permanently(self):
        os.system(f'bash {self.PATH_CONFIG}permanently/restore.sh')

    def restart(self):
        os.system(f'bash {self.PATH_CONFIG}restart.sh')
