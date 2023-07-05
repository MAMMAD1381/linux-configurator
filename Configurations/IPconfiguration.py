import os

class IPconfiguratoin:

    PATH_CONFIG = '/home/mohammad/Documents/Git-hub/linux-configurator/scripts/IP/'

    def __init__(self):

        while True:
            selected_option = self.main_menu()

            match selected_option:
                
                case '1':
                    while True:
                        print('1. temporary')
                        print('2. permanently')
                        print('3. back')
                        selected = input()
                        if selected == '1':
                            interface = input('pls enter the interface name: ')
                            ip = input('pls enter the ip address: ')
                            mask = input('pls enter the mask (num format): ')
                            self.changeIP_temporary(interface, ip, mask)
                        elif selected == '2':
                            interface = input('pls enter the interface name: ')
                            ip = input('pls enter the ip address: ')
                            mask = input('pls enter the mask (x.x.x.x): ')
                            gateway = input('pls enter the gateway: ')
                            dns1 = input('pls enter dns1: ')
                            dns2 = input('pls enter dns2: ')
                            self.changeIP_permanently(interface, ip, mask, gateway, dns1, dns2)
                        elif selected == '3':
                            break
                case '2':
                    while True:
                        print('1. permanently')
                        print('2. back')
                        selected = input()
                        if selected == '1':
                            self.restore_permanently()
                        elif selected == '2':
                            break
                case '3':
                    self.restart()
                case '4':
                    break


    def changeIP_temporary(self, interface, ip, mask):
        os.system(f'bash {self.PATH_CONFIG}temporary/set.sh {interface} {ip} {ip}/{mask}')

    def changeIP_permanently(self, interface, ip, mask, gateway, dns1, dns2):
        os.system(f'bash {self.PATH_CONFIG}permanently/set.sh {interface} {ip} {mask} {gateway} {dns1} {dns2}')
    
    def restore_permanently(self):
        os.system(f'bash {self.PATH_CONFIG}permanently/restore.sh')

    def restart(self):
        os.system(f'bash {self.PATH_CONFIG}restart.sh')
    
    
    def main_menu(self):

        print('pls select a section:')
        print('1. change IP')
        print('2. restore IP')
        print('3. restart')
        print('4. back')

        return input()