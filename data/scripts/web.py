#Imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import csv

## MODIFY
INPUT_URL_FILE = 'Desktop/Test/url.txt'
OUTPUT_FILE = 'Desktop/Test/data.csv'

#Setup Broweser in Ghost mode
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

#Output file
out = open(OUTPUT_FILE, mode='w')
out_writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#Loop through URLs
tempTable = dict()
checkKeys = ["Bottle Size", "Date Published","User Avg Rating","Importer"]
tempWrite = []

with open(INPUT_URL_FILE) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       
       #scrap
       driver.get(line)
       content = driver.page_source
       soup = BeautifulSoup(content,features="html.parser")
       attrs = soup.find_all("div", "info-label small-7 columns")
       values = soup.find_all("div","info small-9 columns")

       tempWrite.append(line[:-1])

       for i in range(0, len(attrs)):
           tempTable[attrs[i].text.strip()] = values[i].text.strip()
        
       for key in checkKeys:
           if(key in tempTable):
              tempWrite.append(tempTable[key])
           else:
              tempWrite.append("")

       taster = soup.find_all("span", "taster-area")
       if len(taster)>0:
           tempWrite.append(taster[0].text)
       else:
           tempWrite.append("")
       
       out_writer.writerow(tempWrite)
       tempWrite = []
       tempTable.clear()
       line = fp.readline()
       cnt += 1

driver.quit()
