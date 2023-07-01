from Configurations import DNSconfiguration
from Configurations import HostnameConfiguration
from Configurations import RootConfiguratoin
from Configurations import IPconfiguration

class LinuxConfigurator:
    def __init__(self):
        while True:

            selected_section = self.main_menu()

            match selected_section:
                case '1':
                    pass

                case '2':
                    pass

                case '3':
                    pass

                case '4':
                    pass

    
    
    def main_menu(self):
        print('''select a section to config:
                 1. DNS:
                 2. Hostname:
                 3. Root:
                 4. IP:''')
        return input()


if __name__=='__main__':
    LinuxConfigurator()