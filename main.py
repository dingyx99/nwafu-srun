import sys, getopt
from nwafu_login import NwafuLogin

def guide(argv):
    print("Usage:\n"+argv+" -u <username> -p <password> \n"+argv+" --username=<username> --password=<password>\n")

def main(argv):
    username = ''
    passwd = ''
    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["username=", "password="])
    except getopt.GetoptError as err:
        guide(sys.argv[0])
        sys.exit(2)
    username = None
    passwd = None
    for opt, arg in opts:
        if opt == '-h':
            guide(sys.argv[0])
            sys.exit()
        elif opt in ['-u', '--username']:
            username = arg
        elif opt in ['-p', '--password']:
            passwd = arg
    if username == None or passwd == None:
        guide(sys.argv[0])
        sys.exit(2)

    a = NwafuLogin(username=username, password=passwd)
    while 1:
        print('\n{: ^28}'.format('NWAFU SRUN Authentication Utility'))
        print('{:-^31}'.format(''))
        print('{: ^15}'.format('1') + '-' + '{: ^15}'.format('Login'))
        print('{: ^15}'.format('2') + '-' + '{: ^15}'.format('Logout'))
        print('{: ^15}'.format('3') + '-' + '{: ^15}'.format('Status'))
        print('{: ^15}'.format('4') + '-' + '{: ^15}'.format('Exit'))
        print('{:-^31}\n'.format(''))
        command = str(input(''))
        if command == '1':
            a.log_in()
        elif command == '2':
            a.log_out()
        elif command == '3':
            a.get_login_info()
        elif command == '4':
            exit()
        else:
            print('\n{: ^28}'.format('Input error!'))

if __name__ ==  "__main__":
    main(sys.argv[1:])