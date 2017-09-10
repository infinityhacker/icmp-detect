#!/usr/bin/env python
#coding:utf-8

import sys

from scapy.all import *


def usage():
    print "Error!                      "
    print "Example ./scapy-icmp.py [ip addr]"
    print "Try again,Good luck"
    sys.exit()
def main():
    if len(sys.argv[1:])!=1:
        usage()
    prefix=sys.argv[1]
    ip=prefix.split(".")[0]+"."+prefix.split(".")[1]+"."+prefix.split(".")[2]+"."
    for addr in range(1,254):
        answer=sr1(IP(dst=ip+str(addr))/ICMP(),timeout=0.1,verbose=0)
        if answer!=None:
            print ip+str(addr)
main()
