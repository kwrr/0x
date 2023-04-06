# 0542264052
# دق على هدى
import requests 

url = 'http://ipinfo.io/json'
re = requests.get(url).json()
Rr = re["country"]
number = input('\n\n'"[+]أدخل الرقم : ")
url = f'https://devappteamcall.site/data/search_name?country={Rr}'
headers = {
'Authorization': 'Basic YWEyNTAyOnp1enVBaGgy',
'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G977N Build/LMY49I)',
'Host': 'devappteamcall.site',
'Connection': 'close',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '23',
}
data = f'&phoneNumber={number}'
r = requests.post(url,headers=headers,data=data).json()

print("")
if r["errorDesc"] == "no data found":
 print("[#]There is no information on the number at the moment")
 #print(r['result'])
else:
	a = r['result']
	print(a)
 	
