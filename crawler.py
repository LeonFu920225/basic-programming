import urllib.request as req
def getdata(url):
    request = req.Request(url, headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink = root.find("a", string = "‹ 上頁")
    return nextLink["href"]
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count<3:
    pageURL = "https://www.ptt.cc" + getdata(pageURL)
    count+=1