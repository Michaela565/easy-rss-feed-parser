import feedparser as feedparser
import re

def inputIsUrl(url):

    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    validated_url = re.findall(regex, url)

    if not validated_url:
        print("Did not input an url.")
        return False
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

def main():
    url = getInput()
    while inputIsUrl(url):
        parsedUrl = inputIsUrl(url)
        printRSS(parsedUrl)
        url = getInput()

if __name__ == '__main__':
    main()

