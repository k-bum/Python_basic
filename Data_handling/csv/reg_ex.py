import urllib.request
import re

url = "https://finance.naver.com/item/main.naver?code=005930"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))

stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_results[0]
print(samsung_stock)
samsung_index = samsung_stock[1]
print(samsung_index)

index_list = re.findall("(\<dd\>)([\s\S]+?)(\<dd\>)", samsung_index)
print(index_list)
for index in index_list :
    print(index[1])