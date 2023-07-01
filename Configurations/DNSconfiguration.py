import os

class DNSconfiguratoin:
    def __init__(self, dns1, dns2):
        self.CONFIG_PATH = '../scripts/DNS/'
        self.dns1 = dns1
        self.dns2 = dns2

    def setDNS_temporary(self):
        self.removeDNS_temporary()
        os.system(f'bash {self.CONFIG_PATH}temporary/set.sh {self.dns1} {self.dns2}')

    def setDNS_permanently(self):
        os.system(f'bash {self.CONFIG_PATH}permanently/set.sh {self.dns1} {self.dns2}')

    def removeDNS_temporary(self):
        os.system(f'bash {self.CONFIG_PATH}temporary/remove.sh')

    def removeDNS_permanently(self):
        os.system(f'bash {self.CONFIG_PATH}permanently/remove.sh {self.dns1} {self.dns2}')

    def restoreDNS(self):
        os.system(f'bash {self.CONFIG_PATH}restore.sh')


if __name__=="__main__":
    dns = DNSconfiguratoin('192.168.168.125', '8.8.8.8')
    dns.setDNS_temporary()
    # dns.setDNS_permanently()
    # dns.removeDNS_temporary()
    # dns.removeDNS_permanently()
    # dns.restoreDNS()
