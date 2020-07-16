from nytimesarticle import articleAPI
api = articleAPI('GlYp94UNGXIDKZvjtIYJCF6bnEn9jK4n')
articles = api.search( q = 'indigo')
urls=[]
for i in articles['response']['docs']:
	print(i['web_url'])
	urls.append(i['web_url'])
with open('lol.txt','w') as f:
    for item in urls:
        f.write("%s\n" % item)
f.close()