import requests
import sys
import argparse
import signal


def parser():
    parser = argparse.ArgumentParser(description='this script lists the subdomains')
    parser.add_argument("-w", "--wordlist", help="path dictionary")
    parser.add_argument('-d', '--domain', help='website domain') 
    return parser

def signal_handler(signal, frame):
    print("\n[+] Exiting.")
    sys.exit(0)
    
if __name__ == '__main__':
    args = parser().parse_args()
    signal.signal(signal.SIGINT, signal_handler)
    if len(sys.argv) == 5:
        domain = args.domain
        path_wordlist = args.wordlist

        with open(path_wordlist, 'r') as file:
            subdomain_list = [line.strip() for line in file if not line.startswith("#")]

        for word in subdomain_list:
            if word:
                url_to_check = f"http://{word}.{domain}"
                #print(url_to_check)

                try:
                    requests.get(url_to_check)
                except requests.ConnectionError:
                    pass
                else:
                    print(f"Valid subdomain: {url_to_check}")

    else:
        parser().print_help()