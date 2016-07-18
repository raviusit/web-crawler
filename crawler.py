#! /usr/bin/env python
#
# crawler.py
#
#    This program performs web-crawling to the specified website 
#
# Author:    Ravi Maurya
# Creation:  18 Jul, 2016
#

import re
import urllib2
import BeautifulSoup
import exceptions

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def isValidUrl(url):
    if regex.match(url) is not None:
        strs = url

        # lst = ["twitter","facebook", "google", "messenger",
        #        "mapsmaker", "linkedin", "bit", "youtube",
        #        "mckinsey", "windowsphone", "pac-online", "statcounter" ]
        # matchlst =[]
        # for i in range(len(lst)):
        #     matchlst[i] = re.search(r'\b  \b',strs)

        # match1  = re.search(r'\btwitter\b',strs)
        # match2  = re.search(r'\bfacebook\b',strs)
        # match3  = re.search(r'\bgoogle\b',strs)
        # match4  = re.search(r'\bmessenger\b',strs)
        # match5  = re.search(r'\bmapsmarker\b',strs)
        # match6  = re.search(r'\blinkedin\b',strs)
        # match7  = re.search(r'\bbit\b',strs)
        # match8  = re.search(r'\byoutube\b',strs)
        # match9  = re.search(r'\bmckinsey\b',strs)
        # match10 = re.search(r'\bwindowsphone\b',strs)
        # match11 = re.search(r'\bpac-online\b',strs)
        # match12 = re.search(r'\bstatcounter\b',strs)
        # match13 = re.search(r'\bdesignit\b',strs)
        # match14 = re.search(r'\bdesignitmarcom\b',strs)
        # match15 = re.search(r'\baboutads\b',strs)
        # match16 = re.search(r'\bnetworkadvertising\b',strs)
        match = re.search(r'\bwiprodigital\b',strs)

        if match:
                # or match2 or match3 or match4 \
                # or match5 or match6 or match7 or match8\
                # or match9 or match10 or match11 or match12 or match13\
                # or match14 or match15 or match16:
            return True
        else:
            return False
    return False

def crawler(SeedUrl):
    tocrawl=[SeedUrl]
    crawled=[]
    try:
        print "Started Crawling : HTTPS://wiprodigital.com"
        while tocrawl:
            page=tocrawl.pop()
            if page not in crawled:
                print 'Crawled:'+page
            pagesource=urllib2.urlopen(page)
            s=pagesource.read()
            soup=BeautifulSoup.BeautifulSoup(s)
            links=soup.findAll('a',href=True)
            if page not in crawled:
                for l in links:
                    if isValidUrl(l['href']):
                        tocrawl.append(l['href'])
                crawled.append(page)
        return crawled
    except Exception, detail:
        print Exception
        print str(detail) + "the last requested page was not found"
    else:
        success()          # Display a big fat success message

def success():
  print
  print "+==================================================================+"
  print "|"
  print "|  All pages crawled Successfully!!!"
  print "|"
  print "+==================================================================+"
  print

crawler('http://wiprodigital.com/')
