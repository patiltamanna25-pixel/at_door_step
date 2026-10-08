import requests as r
# import requests
# data = requests.get()
# data = data.json()
# response = data["articles"][0]
# print(response["title"])
# response = data
# print(response)
data=r.get("https://newsapi.org/v2/everything?q=tesla&from=2026-08-29&sortBy=publishedAt&apiKey=e1dd2e3054b04c41835c93e40109a664")
data.json 
response = data
print(response)


