#!/usr/bin/python3

import sys
import requests
import socket
import json
from urllib.parse import urlparse
import argparse

def case_url(url):
    parsed_url=urlparse(url)
    domain=parsed_url.netloc
    return domain

def case_domain(domain):
    r_gethost=socket.gethostbyname(domain)
    return r_gethost

def case_ip(ip):
    r_getInfo_ip=requests.get("https://ipinfo.io/"+ip+"/json")
    resp_infoIp=json.loads(r_getInfo_ip.text)
    return resp_infoIp

if __name__=='__main__':
    
    if len(sys.argv)<4:
        parser=argparse.ArgumentParser(description="enumeration information")
        parser.add_argument('--url','-u', help='url website')
        parser.add_argument('--domain','-d',help='domain name')
        parser.add_argument('--ipaddress','-i',help='ip Address')
    
        #get info url, domain, ip

        args=parser.parse_args()
        url=args.url
        domain=args.domain
        ipaddress=args.ipaddress
        
        if url:
            # Url case
            jsonInfo=(case_ip(case_domain(case_url(url))))
            for data in jsonInfo:
                print(data +" : " +jsonInfo[data])
        elif domain:
            # domain case
            jsonInfo=(case_ip(case_domain(domain)))
            for data in jsonInfo:
                print(data +" : " +jsonInfo[data])
        elif ipaddress:
            # ip address case
            jsonInfo=(case_ip(ipaddress))
            for data in jsonInfo:
                print(data +" : " +jsonInfo[data])            
    else:
        print("[+] incorrect parameters")

