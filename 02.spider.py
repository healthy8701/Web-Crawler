"""
使用google搜尋圖片並下載儲存

這次使用2個模塊來解決問題
os:建立資料夾
re:使用正則表達式來檢索、替換那些符合某個模式的文字

透過更改url參數在google上搜尋圖片，使用re模塊來分析尋找圖片的url，最後再將圖片下載儲存
"""
import os
import urllib.request
import re

# 搜尋文字
search_item = '周子瑜'
photos = []
# 先確認資料夾是否存在後再建立資料夾
if not os.path.exists('photo\\'+search_item): 
	os.makedirs('photo\\'+search_item)
	
# google搜尋圖片規則 search?q='搜尋文字'
# urllib.request.quote將文字轉換成url編碼	
keyWord = urllib.request.quote(search_item)
url = 'https://www.google.com.tw/search?q='+keyWord+'&hl=zh-TW&biw=1649&bih=872&site=imghp&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiC2o2A1KvMAhWEkJQKHbZ7AocQ_AUIBygC'  #入口頁面
req = urllib.request.Request(url, headers = {
		'Connection': 'Keep-Alive',
		'Host': 'www.google.com.tw',
		'Referer': 'https://www.google.com.tw',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'zh-TW,en-US;q=0.7,en;q=0.3',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.3 Waterfox/40.0.3'
	})	

web_page = urllib.request.urlopen(req , timeout = 5).read().decode('utf-8')
# 設定正則表達式匹配規則，過濾文字取得http或https開頭的網址
web_filter = re.compile("http(.+?)\"")		

# web_filter.findall搜尋web_pag找出網址
for image_url in web_filter.findall(web_page):
	# 過濾副檔名不是圖片格式的網址
	if '.jpg' in image_url.lower() or '.png' in image_url.lower() or '.bmp' in image_url.lower() or '.jpeg' in image_url.lower():
		# 儲存圖片網址
		photos.append('http'+image_url)		

i = 0
# 下載圖片並儲存
for photo in photos:
	try:
		web_page = urllib.request.urlopen(photo, timeout = 5).read()				
	except:
		continue
	else:
		f = open('photo\\'+search_item+'\\'+str(i)+'.jpg', 'wb')
		i += 1
		f.write(web_page)
		f.close()
