import webbrowser
import requests

pages = {}
pageurl = 'https://pjwstk.edu.pl'
dates = ["20230126", "20220820", "20210122"]
for date in dates:
    url = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+date
    response = requests.get(url)
    d = response.json()
    if "closest" in d["archived_snapshots"]:
        pages[date] = d["archived_snapshots"]["closest"]["url"]
    else:
        print(f"No archive for {date}")
print(pages)
for page in pages:
    webbrowser.open(page)
