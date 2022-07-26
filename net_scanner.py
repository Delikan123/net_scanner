import scapy.all as scapy
import optparse



opt_object=optparse.OptionParser()

def get_user_input():
    opt_object.add_option("-i","--ip",dest="ip_address",help="""
     - i or --ip use 192.168.1.0/24
    """)
    (user_input,args)=opt_object.parse_args()
    if  not user_input.ip_address:
        print("Enter ip address!")
    return user_input

def scan_ip(ip_range):
    arp_request=scapy.ARP(pdst=ip_range)

    broad_cast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combination=broad_cast/arp_request

    (answer_list,unanswered_list)=scapy.srp(combination,timeout=1)

    answer_list.summary()


user_ip=get_user_input()
scan_ip(user_ip.ip_address)