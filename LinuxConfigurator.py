from Configurations.DNSconfiguration import DNSconfiguratoin
from Configurations.HostnameConfiguration import HostnameConfiguratoin
from Configurations.IPconfiguration import IPconfiguratoin
from Configurations.RootConfiguratoin import RootConfiguratoin
from Configurations.nftables.NFtableHandler import NftableHandler

class LinuxConfigurator:

    def __init__(self):
        
        while True:
            selected_option = self.main_menu()

            match selected_option:
                
                case '1':
                    DNSconfiguratoin()
                case '2':
                    HostnameConfiguratoin()
                case '3':
                    IPconfiguratoin()
                case '4':
                    RootConfiguratoin()
                case '5':
                    NftableHandler()
                case '6':
                    exit(0)

    def main_menu(self):

        print('pls select an option to configure:')
        print('1. DNS')
        print('2. Hostname')
        print('3 IP')
        print('4 Root')
        print('5 nftables')
        print('6 quit')

        return input()

if __name__=='__main__':
    LinuxConfigurator()


