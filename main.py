import feedparser as feedparser
import re

def inputIsUrl(url):

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    validated_url = re.findall(regex, url)

    if not validated_url:
        print("Did not input an url.")
    else:
        return feedparser.parse(url)


def printRSS(url):
    try:
        for item in url["entries"]:
            print(item['title'])
            print(item['link'])
            print(item['description'])
    except:
        print("Not a functional url.")


def getInput():
    userInput = input()
    return userInput  

url = inputIsUrl("https://hackaday.com/blog/feed/")
printRSS(url)
#https://www.mangago.me/r/rsslink/sachiiro_no_one_room.xml
#https://hackaday.com/blog/feed/
#d = feedparser.parse("http://feedparser.org/docs/examples/atom10.xml")
#print(d['feed']['title'])

