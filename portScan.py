#!/usr/bin/python3

from socket import *
import sys
import argparse
import ipaddress
from pwn import *

def valid_ipaddres(ip_string):
    ip_valid=False

    try:
        ip_object = ipaddress.ip_address(ip_string)
        ip_valid=True
    except ValueError:
       print('The IP address %s is not valid' % ip_string)
    return ip_valid

def arguments():
    parser=argparse.ArgumentParser(description='Enumeration Ports')
    parser.add_argument('-i','--ip',dest='ip', required=True, help='Ip for scan')
    args=parser.parse_args()
    
    return args
    #print(args.ip)

def scanPort(ip_scan):
    t_IP=gethostbyname(ip_scan)
    print('\t[+] Host: %s ' %(t_IP))
    p=log.progress('Scaning')

    for i in range(1,65536):
        p.status('\nDiscovering port %s' %i)
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn=s.connect_ex((t_IP,i))

        if(conn==0):
            print('\t[+] Port %d : OPEN' %(i))
        s.close()
    
if __name__=='__main__':
    ip_address=arguments()
    ip_scan=ip_address.ip
    if(valid_ipaddres(ip_scan)):
        scanPort(ip_scan)

