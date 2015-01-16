#beginning of Romer Code
import sys #part of standard library
import requests #pip install requests
import re #part of standard library
import csv #part of standard library
from bs4 import BeautifulSoup #pip install beautifulsoup4

def scrape_class():
    url = "http://www.cazy.org/"

    # spoof some headers so the request appears to be coming from a browser, not a bot
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

    # make the request to the search url, passing in the the spoofed headers.
    r = requests.get(url, headers=headers)  # assign the response to a variable r

    # check the status code of the response to make sure the request went well
    if r.status_code != 200:
        print("request denied")
        return
    else:
        print("scraping " + url)

    soup = BeautifulSoup(r.text)

#end of Romer Code

#need to figure out how to specifically pull out the links :/
    #get titles    
    #links = soup.find_all(href=re.compile(".html"))
    links = soup.select("a[href]")

    output_classes = open('1.csv', "wb")
    writer_classes = csv.writer(output_classes, delimiter=',')

    #print headers
    for link in links:
        print (link.text)

    writer_classes.write('')
    output_classes = open('1.csv', "ab")
    
#write links to file here

    output_classes.close()

scrape_class()
