# coding: utf-8

import sys, os
import lxml.html
import requests
import csv
 
TARGET_URLS = [
  "http://www.data.jma.go.jp/sakura/data/sakura003_01.html",
  "http://www.data.jma.go.jp/sakura/data/sakura003_02.html",
  "http://www.data.jma.go.jp/sakura/data/sakura003_03.html",
  "http://www.data.jma.go.jp/sakura/data/sakura003_04.html",
  "http://www.data.jma.go.jp/sakura/data/sakura003_05.html",
  "http://www.data.jma.go.jp/sakura/data/sakura003_06.html"]
CSV_FILENAME = "./sakura.csv"
CSV_HEADER = ['YEAR', 'MONTH', "DAY"]

output_datas = []
for url in TARGET_URLS:
  response = requests.get(url)
  response.encoding = 'utf-8'
  text = lxml.html.fromstring(response.text)
  text = text.xpath('//div[@class="indent"]/pre')
  lines = text[0].text_content().split(u'\n')
  #print (lines)
  print len(lines)

  years = []
  material = []

  for line in lines:
    #print (line)
    #sys.exit()
    if line.find(u"地点名") >= 0:
      #pass
      y_tmp = line.split(' ')
      for y in y_tmp:
        if y.isdigit():
          years.append(y)
      break

  for line in lines:
    #print (line)
    #sys.exit()
    if line.find(u"東京") >= 0:
      #pass
      m_tmp = line.split(' ')
      for m in m_tmp:
        if m.isdigit():
          material.append(m)

  print (years)
  print (material)

  m_index = 0
  for y_val in years:
    month = material[m_index]
    day = material[m_index + 1]
    
    print("year = " + y_val + " : month = " + month + " : day = " + day)
    output_datas.append([int(y_val), int(month), int(day)])
    m_index += 2

print(output_datas)


f = open(CSV_FILENAME, 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerow(CSV_HEADER) # ヘッダーを書き込む
writer.writerows(output_datas)
f.close

