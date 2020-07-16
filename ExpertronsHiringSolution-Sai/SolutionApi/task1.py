from newsapi import NewsApiClient
#token wont work once i upload it to github because github might revoke it
api = NewsApiClient(api_key='5f69eeeef42a48b9b32a59713bfe1e30')
x=int(input("choose option"))
if(x==1):
	bitcoin=api.get_top_headlines(q='bitcoin')
	print(bitcoin)
if(x==2):
	techcrunch=api.get_top_headlines(sources='techcrunch')
	print(techcrunch)
else:
	print('invalid option')