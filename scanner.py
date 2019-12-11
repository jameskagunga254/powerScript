import scapy.all as scapy




def scanner(ip):


    arp_request=scapy.ARP(pdst=ip)

    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")


    arp_request_broadacat=broadcast/arp_request


    answered_list=scapy.srp(arp_request_broadacat,timeout=2,verbose=False)[0]

    client_list=[]


    
    for element in answered_list:


        
        client_dict={'ip address':element[1].psrc ,'mac address':element[1].hwsrc}


        client_list.append(client_dict)


        return client_list

def output(result):

    print("ip address \t \t mac address\n -------------------------------------------------")

    for element in result:

        print(element['ip address'] + "\t\t" + element["mac address"])





result=scanner("192.168.8.0/24")


output(result)