import feedparser as feedparser

d = feedparser.parse("https://hackaday.com/blog/feed/")
print(d['feed']['title'])
