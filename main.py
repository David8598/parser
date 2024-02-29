import requests

# headers= {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
#     ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
# }
url = "https://1xbit-ua.com/LiveFeed/Get1x2_VZip?sports=1&count=50&gr=29&mode=4&country=2&partner=65&getEmpty=true"
champs = url.split('/')
print(champs)
params = {
    'sports': '1',
    'champs': '2048450',
    'lng': 'en',
    'gr': '29',
    'country': '2',
    'partner': '65',
    'virtualSports': 'true',
    'groupChamps': 'true',
}
    

req = requests.get(url, headers=params)
result = req.json()
print(result)
# print(src)
    
