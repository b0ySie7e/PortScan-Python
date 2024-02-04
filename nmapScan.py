#!/usr/bin/python3

import nmap

import sys
import argparse

ports=[21,22, 23,25,53,80,110,139,143,443,445,3389,3306,5900,8080,111,135,137,138,139,161,389,512,513,514,587,993,995,2049]

if __name__=='__main__':
    
    if len(sys.argv)<4:    
        parser=argparse.ArgumentParser(description='Enumeration commons ports')
        parser.add_argument('--ipaddress', '-i', help='ip address target')
        args=parser.parse_args()
        
        target=args.ipaddress
        
        if target:
            try:
                scan_v=nmap.PortScanner()
                for port in ports:
                    portScan=scan_v.scan(target,str(port),timeout=5)
                    print("[+] %s is %s" %(str(port),portScan['scan'][target]['tcp'][port]['state']))   
            except KeyError:
                print("Error, timeout ")
            except Exception as e:
                print("Ocurrio un error %s" %e)
                
                