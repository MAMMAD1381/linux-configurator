import os
# from .configs import PATHconfig
# from configs.PATHconfig import PATHconfig
class DNSconfiguratoin:
    def __init__(self):
        # self.PATH_CONFIG = PATHconfig.DNS_PATH_CONFIG
        self.PATH_CONFIG = '../scripts/DNS/'


    def setDNS_temporary(self, dns1, dns2):
        self._backup('temporary')
        self.removeDNS_temporary()
        os.system(f'bash {self.PATH_CONFIG}temporary/set.sh {self.dns1} {self.dns2}')

    def setDNS_permanently(self, dns1, dns2):
        self._backup('permanently')
        self.removeDNS_permanently()
        os.system(f'bash {self.PATH_CONFIG}permanently/set.sh {self.dns1} {self.dns2}')

    def removeDNS_temporary(self):
        os.system(f'bash {self.PATH_CONFIG}temporary/remove.sh')

    def removeDNS_permanently(self):
        os.system(f'bash {self.PATH_CONFIG}permanently/remove.sh')

    def restoreDNS_temporary(self):
        os.system(f'bash {self.PATH_CONFIG}temporary/restore.sh')

    def restoreDNS_permanently(self):
        os.system(f'bash {self.PATH_CONFIG}permanently/restore.sh')

    def restart(self):
        os.system(f'bash {self.PATH_CONFIG}restart.sh')
    
    def _backup(self, type):
        os.system(f'bash {self.PATH_CONFIG}backup.sh {type}')



if __name__=="__main__":
    dns1 = '192.168.168.125'
    dns2 = '8.8.8.8'
    dns = DNSconfiguratoin()
    # dns.setDNS_temporary()
    # dns.setDNS_permanently()
    # dns.removeDNS_temporary()
    # dns.removeDNS_permanently()
    # dns.restoreDNS_permanently()
    # dns.restoreDNS_temporary()
    # dns.restart()
