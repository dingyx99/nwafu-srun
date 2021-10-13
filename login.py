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
    
    NwafuLogin(username=username, password=passwd).log_out()
    NwafuLogin(username=username, password=passwd).log_in()

if __name__ ==  "__main__":
    main(sys.argv[1:])