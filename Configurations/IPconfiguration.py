import os

class IPconfiguratoin:
    def __init__(self):
        self.PATH_CONFIG = '../scripts/IP/'

    def changeIP_temporary(self, interface, ip, mask):
        os.system(f'bash {self.PATH_CONFIG}temporary/set.sh {interface} {ip} {ip}/{mask}')

    def changeIP_permanently(self, interface, ip, mask, gateway, dns1, dns2):
        os.system(f'bash {self.PATH_CONFIG}permanently/set.sh {interface} {ip} {mask} {gateway} {dns1} {dns2}')
    
    def restore_permanently(self):
        os.system(f'bash {self.PATH_CONFIG}permanently/restore.sh')

    def restart(self):
        os.system(f'bash {self.PATH_CONFIG}restart.sh')
    
    

if __name__=='__main__':
    ip = IPconfiguratoin()
    # interface = 'lo'
    # ip_address = '127.0.0.1'
    # mask = '8'
    # ip.changeIP_temporary(interface, ip_address, mask)
    # ip.changeIP_permanently('eth2', '192.168.168.0', '255.255.255.0', '192.168.168.254', '8.8.8.8', '1.1.8.8');
    ip.restart()