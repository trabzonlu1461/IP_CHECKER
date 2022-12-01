import requests
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

web_dic = {

"web_1" :"https://www.ip-tracker.org/lookup.php?ip=",
"web_2" :"https://scamalytics.com/ip/",
"web_3" :"https://www.virustotal.com/gui/ip-address/",
"web_4" :"https://exchange.xforce.ibmcloud.com/ip/",
"web_5" :"https://www.abuseipdb.com/check/" 
    }

for web in web_dic:
	web_dic[web]+=ip_address



def open_url(ip_address,web_dic):

	if chrome_path == 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' :
		for url in web_dic:
			webbrowser.get(chrome_path).open(web_dic[url])
	else:
		for url in web_dic:
			webbrowser.open(web_dic[url])


open_url(ip_address,web_dic)
