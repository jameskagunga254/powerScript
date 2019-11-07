
#!/usr/bin/env/python


import scapy.all as scapy

import optparse


def user_handler():
    parser=optparse.OptionParser()


    parser.add_option("--t","--target",dest="target",help="enter the ip address you want to scan")


    (User_input,target)=parser.parse_args()


    if not target:


        parser.error("please include the ip address in your argument")


    else:

        return target



def scan(ip):

    #algorithm to scan the network and find the ip addresses and mac address

    #first part is to send an arp request

    arp_request=scapy.ARP()

    arp_request.pdst=ip


    #here we create the broadcast frame

    broadcast=scapy.Ether()

    broadcast.dst="ff:ff:ff:ff:ff:ff"


    #we combine both packets 


    arp_request_broadcast=broadcast/arp_request

    #we get the result of the arp request in form of two list one for answered and for unswered



    answered=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]


    #now we use the list of element

    #now let iterate over the element in the list


   


    client_list=[]

    for element in answered:


        client_dict={"ip address":element[1].psrc,"mac_address":element[1].hwsrc}


        client_list.append(client_dict)


       
        

# we achieved what we wanted to have the ip address and mac address

#return the result to be used by another function
    return client_list
        




def out_put(client_query):


     print("ip address \t\t mac address \n--------------------------------------------------------")


     for client_element in client_query:


         print(client_element["ip address"] + "\t\t" + client_element["mac_address"])
   



client_info=scan(user_handler())

out_put(client_info)