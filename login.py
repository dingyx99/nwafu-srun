import sys, getopt
from nwafu_login import NwafuLogin

def main():
    username = ''
    passwd = ''
    argv = sys.argv[1:]
    if len(argv) != 4:
        print("Usage:\npython3 login.py -u <username> -p <password> \npython3 login.py --username=<username> --password=<password>\n")
        sys.exit(2)
    else:
        try:
            opts, args = getopt.getopt(argv, "hu:p:", ["username=", "password="])
        except getopt.GetoptError:
            print("Usage:\npython3 login.py -u <username> -p <password> \npython3 login.py --username=<username> --password=<password>\n")
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print("Usage:\npython3 login.py -u <username> -p <password> \npython3 login.py --username=<username> --password=<password>\n")
                sys.exit()
            elif opt in ['-u', '--username']:
                username = arg
            elif opt in ['-p', '--password']:
                passwd = arg
    
    NwafuLogin(username=username, password=passwd).log_out()
    NwafuLogin(username=username, password=passwd).log_in()

main()