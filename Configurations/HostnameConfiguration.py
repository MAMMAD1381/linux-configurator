import os

class HostnameConfiguratoin:

    PATH_CONFIG = '../scripts/Hostname/'

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
                            hostname = input('pls enter the hostname: ')
                            self.changeHostname_temporary(hostname)
                        elif selected == '2':
                            hostname = input('pls enter the hostname: ')
                            self.changeHostname_permanently(hostname)
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



    def changeHostname_temporary(self, hostname):
        os.system(f'bash {self.PATH_CONFIG}temporary/set.sh {hostname}')

    def changeHostname_permanently(self, hostname):
        os.system(f'bash {self.PATH_CONFIG}permanently/set.sh {hostname}')
    
    def restore_permanently(self):
        os.system(f'bash {self.PATH_CONFIG}permanently/restore.sh')

    def restart(self):
        os.system(f'bash {self.PATH_CONFIG}restart.sh')


    def main_menu(self):

        print('pls select a section:')
        print('1. change hostname')
        print('2. remove hostname')
        print('3. restart')
        print('4. back')

        return input()

