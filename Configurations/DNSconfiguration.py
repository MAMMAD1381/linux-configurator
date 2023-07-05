import os
import sys

class DNSconfiguratoin:

    PATH_CONFIG = '/home/mohammad/Documents/Git-hub/linux-configurator/scripts/DNS/'


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
                            dns1 = input('pls enter the first dns: ')
                            dns2 = input('pls enter the second dns: ')
                            self.setDNS_temporary(dns1, dns2)
                        elif selected == '2':
                            dns1 = input('pls enter the first dns: ')
                            dns2 = input('pls enter the second dns: ')
                            self.setDNS_permanently(dns1, dns2)
                        elif selected == '3':
                            break
                case '2':
                    while True:
                        print('1. temporary')
                        print('2. permanently')
                        print('3. back')
                        selected = input()
                        if selected == '1':
                            self.removeDNS_temporary()
                        elif selected == '2':
                            self.removeDNS_permanently()
                        elif selected == '3':
                            break
                case '3':
                    while True:
                        print('1. temporary')
                        print('2. permanently')
                        print('3. back')
                        selected = input()
                        if selected == '1':
                            self.restoreDNS_temporary()
                        elif selected == '2':
                            self.restoreDNS_permanently()
                        elif selected == '3':
                            break
                case '4':
                    self.restart()
                case '5':
                    break


    def setDNS_temporary(self, dns1, dns2):
        self._backup('temporary')
        self.removeDNS_temporary()
        os.system(f'bash {self.PATH_CONFIG}temporary/set.sh {dns1} {dns2}')

    def setDNS_permanently(self, dns1, dns2):
        self._backup('permanently')
        self.removeDNS_permanently()
        os.system(f'bash {self.PATH_CONFIG}permanently/set.sh {dns1} {dns2}')

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



    def main_menu(self):

        print('pls select a section:')
        print('1. set dns')
        print('2. remove dns')
        print('3. restore dns')
        print('4. restart')
        print('5. back')

        return input()

