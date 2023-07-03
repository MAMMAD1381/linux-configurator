import os

class HostnameConfiguratoin:
    def __init__(self):
        self.PATH_CONFIG = '../scripts/Hostname/'
        self.hostname = hostname


    def changeHostname_temporary(self, hostname):
        os.system(f'bash {self.PATH_CONFIG}temporary/set.sh {hostname}')

    def changeHostname_permanently(self, hostname):
        os.system(f'bash {self.PATH_CONFIG}permanently/set.sh {hostname}')
    
    def restore_permanently(self):
        os.system(f'bash {self.PATH_CONFIG}permanently/restore.sh')

    def restart(self):
        os.system(f'bash {self.PATH_CONFIG}restart.sh')

if __name__=='__main__':
    hostname = 'mohammad'
    # host = HostnameConfiguratoin()
    # host.changeHostname_temporary()
    # host.changeHostname_permanently()
    # host.restore_permanently()
    # host.restart()