import requests, bs4

response = requests.get("http://wufazhuce.com/one/1293")
soup = bs4.BeautifulSoup(response.text, "html.parser")

title = soup.title.string[4:8]
print title

for meta in soup.select('meta'):
	if meta.get('name') == 'description':
		print meta.get('content')

print soup.find_all('img')[1]['src']		
