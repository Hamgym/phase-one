from urllib import request as req
from bs4 import BeautifulSoup as bs
import csv

# 回傳網頁物件
def soup(url):
  request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
  })
  with req.urlopen(request) as res:
    data = res.read().decode("utf-8")
  
  soup = bs(data, "html.parser")
  return soup

# 回傳文章時間
def article_time(url):
  span = soup(url).find("span", string="時間")
  if span != None:
    return span.next_sibling.string
  else:
    return None

# 擷取網頁資訊
arr_page_info = []
def page_info(url):
  root = soup(url)
  articles = root.find_all("div", class_="r-ent")
  for article in articles:
    row = []
    if (article.a != None):        
      row.append(article.a.string)
      if (article.span != None):      
        row.append(article.span.string)
      else:
        row.append(0)      
      link = 'https://www.ptt.cc' + article.a["href"]
      row.append(article_time(link))
      print(row)
      arr_page_info.append(row[:])
  
  next_link = root.find("a", string="‹ 上頁")
  return 'https://www.ptt.cc' + next_link["href"]


# 網頁網址
url = 'https://www.ptt.cc/bbs/Lottery/index.html'
# 網頁數量
num_of_pages = 3
# 擷取網頁內容
for i in range(num_of_pages):
  url = page_info(url)
# 將內容寫入檔案
with open("article.csv", mode="w", newline="", encoding="utf-8") as file:
  writer = csv.writer(file)
  writer.writerows(arr_page_info)