import requests
import urllib
import webbrowser
from art import *


tprint("IP_CHECK", font="random")

	
end = False
while not end:
    ip_address = input("IP check: ")
    check_ip = list(ip_address)
    ip_score = 0

    for i in check_ip:
        if i == ".":
            ip_score+=1
    if ip_score !=3:
        print("wrong ip address")
    elif ip_score ==3:
        end=True



chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'


if chrome_path == 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' :

    web_1 = "https://www.ip-tracker.org/lookup.php?ip=" + ip_address
    web_2 = "https://scamalytics.com/ip/" + ip_address
    web_3 = "https://www.virustotal.com/gui/ip-address/" + ip_address
    web_4 = "https://exchange.xforce.ibmcloud.com/ip/" + ip_address
    web_5 = "https://www.abuseipdb.com/check/" + ip_address


    webbrowser.get(chrome_path).open(web_1)
    webbrowser.get(chrome_path).open(web_2)
    webbrowser.get(chrome_path).open(web_3)
    webbrowser.get(chrome_path).open(web_4)
    webbrowser.get(chrome_path).open(web_5)

     
else:
    webbrowser.open(web_1)
    webbrowser.open(web_2)
    webbrowser.open(web_3)
    webbrowser.open(web_4)
    webbrowser.open(web_5)









