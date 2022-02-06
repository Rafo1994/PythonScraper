import requests
payload = {'api_key': '0ad5cbd610bf4d2f9a32995f2804791d', 'url': 'https://www.njuskalo.hr/iznajmljivanje-stanova?geo%5BlocationIds%5D=6566%2C6638%2C6643%2C6610%2C6578%2C6582&price%5Bmax%5D=450'}


r = requests.post('http://api.scraperapi.com', params=payload, data={"id":36585146})



file = open("scraped.txt", "w+")

file.write(r.text)
