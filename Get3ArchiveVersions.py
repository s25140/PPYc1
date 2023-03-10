import webbrowser
import requests

pages = {}
pageurl = 'https://google.com'
dates = [20230126, 20220820, 20210122]
for date in dates:
    url = "http://archive.org/wayback/availableurl="+pageurl+"&timestamp="+str(date)
    print(url)
    response = requests.get(url)
    d = response.json()
    pages[date] = d["archived_snapchots"]["closest"]["url"]
print(pages)
#webbrowser.open(pages)
