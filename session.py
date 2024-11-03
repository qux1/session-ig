import requests
import os
import time
import subprocess


print("—"*20)
print("[~] Coded By MrDeNsor")
print("[~] Instagram : 6gr8")
print("[~] Telegram : RRRBG , DENS0R")
print("—"*20)

# Make It Better

# 
# 

c = input("[1] - INFO SESSIONID \n[2] - EXIT\n")

if c == "1":
   sessionid = input("[+] Enter Sessionid : ")
   url = "https://www.instagram.com/api/v1/accounts/edit/web_form_data/"
   headers = {
       "Host": "www.instagram.com",
       "X-ASBD-ID": "129477",
       "X-Requested-With": "XMLHttpRequest",
       "X-IG-App-ID": "936619743392459",
       "Accept-Language": "en-GB,en;q=0.9",
       "Accept-Encoding": "gzip, deflate, br",
       "Accept": "*/*",
       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.4 Safari/605.1.15",
       "Referer": "https://www.instagram.com/accounts/edit/",
       "X-IG-WWW-Claim": "hmac.AR3bTgOL-VtppUkzwF_bO_HHLX7VEIeHWQyFv3BzZlrd434X",
       "Connection": "close",
       "Cookie": f"csrftoken=nHKrrCu0R9gHl2ZRETw10fTSpKwTxEeH; ds_user_id=7991290622; rur=\"LLA\\0547991290622\\0541754919949:01f7be56a2cd72ca42a6ed80b75753181027d3aca17fea9c597553de587a403ed8da992b\"; wd=768x873; sessionid={sessionid}; shbid=\"19193\\0547991290622\\0541754910340:01f789e90ed48dfab87cfb668421e213e1d5d67153ba0f1697aa26348e0f85c2cdd704ae\"; shbts=\"1723374340\\0547991290622\\0541754910340:01f736bdbf056887973295ff1018938d7c97a0f125ad77825c54d3339aefa6f7d25ff6fc\"; mid=ZriaVgAEAAHWfpmzgnQ4pAcjHbcR; datr=t1yMZlnu_939ZPaCrgOrdR5H; ig_did=1415ECAC-AEAA-40D4-BBC3-33DF7B8D6900; ig_nrcb=1",
       "X-CSRFToken": "nHKrrCu0R9gHl2ZRETw10fTSpKwTxEeH"
       }
   try:
      req = requests.get(url, headers=headers)
      print("[-]",req.status_code)
      # print(req.text)
      if '"status"' in req.text:
         getuser = req.json()['form_data']['username']
         getbday = req.json()['form_data']['birthday']
         getemail = req.json()['form_data']['email']
         getnum = req.json()['form_data']['phone_number']
         getconfirmed = req.json()['form_data']['is_email_confirmed']
         getconfirmed2 = req.json()['form_data']['is_phone_confirmed']
         print(f"[-] Username : {getuser}")
         print(f"[-] Birthday : {getbday}")
         print(f"[-] Email : {getemail}")
         print(f"[-] PhoneNum : {getnum}")
         print(f"[-] Is Email Confirmed : {getconfirmed}")
         print(f"[-] Is PhoneNum Confirmed : {getconfirmed2}")
         # print(f"[-] Email : {email['email_address']}")
         print("[-] SessionId : GOOD")
      else:
         print("[-] SessionId : BAD")
   except ValueError:
      print("[X] ERROR !")

else:
   exit(0)
