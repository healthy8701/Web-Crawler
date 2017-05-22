"""
簡單的爬蟲範例
爬取yahoo首頁並儲存
"""

import urllib

# urllib.request.Request建構HTTP requests所需要的資訊
# url要抓取的網址
# headers 是用來修改User-Agent來偽裝瀏覽器，因為某些HTTP服務器只允許常見的瀏覽器來請求
url = "https://tw.yahoo.com/"
req = urllib.request.Request(url, headers = {
		'Connection': 'Keep-Alive',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-TW,en-US;q=0.7,en;q=0.3',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.3 Waterfox/40.0.3'
	})	

# urllib.request.urlopen打開網頁 
# timeout 請求超出了設置的時間還沒得到響應，就會拋出異常
urlop = urllib.request.urlopen(req, timeout = 2) 
# 讀取網頁
web_page = urlop.read()
# 將網頁轉成utf8編碼並顯示網頁資訊
print(web_page.decode('utf-8'))
# 將網頁儲存下來
f = open('web.html', 'wb')
f.write(web_page)
f.close()