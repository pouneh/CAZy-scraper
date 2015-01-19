#beginning of Romer Code
import sys #part of standard library
import requests #pip install requests
import re #part of standard library
import csv #part of standard library
from bs4 import BeautifulSoup #pip install beautifulsoup4

base = "http://www.cazy.org/"
    # spoof some headers so the request appears to be coming from a browser, not a bot
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "accept-encoding": "gzip,deflate,sdch",
    "accept-language": "en-US,en;q=0.8",
}

def scrape_class1():
    # make the request to the search url, passing in the the spoofed headers.
    r = requests.get(base, headers=headers)  # assign the response to a variable r

    # check the status code of the response to make sure the request went well
    if r.status_code != 200:
        print("request denied")
        return
    else:
        print("scraping " + base)

    soup = BeautifulSoup(r.text)

#end of Romer Code

    links = soup.find_all('a')

    #list for specific links
    wanted_links=[]

    for i in range(1,6):
        wanted_links.append((links[i]).get('href'))

    out = open('1a.txt', 'w')
    #writer_one= csv.writer(output_one)

    for link in wanted_links:
       out.write(base+link) #full URL for each class
       out.write('\n')
    
    out.close()

def scrape_class2():
    #files created in this class: 
        #CSV with CAZy Classes intro and mechanism
        #URL file for each class with the URLs for each of the family groups

    #create list with all full links
    classURL_file=open('1a.txt', 'r')#open 1a.txt
    classURL_list=classURL_file.readlines()#read in each line into URL list
    for url_el in classURL_list:
        url_el=url_el[0:len(url_el)-1] #gets rid of '\n' character
        print (url_el)


    
      


scrape_class1()
scrape_class2()
