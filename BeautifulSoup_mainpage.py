import feedparser
 
# Function to fetch the rss feed and return the parsed RSS
def parseRSS( rss_url ):
    return feedparser.parse( rss_url ) 
    
# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        print(newsitem)
        print(newsitem.image)
        img=newsitem["image"][0]["url"]
        try:
            img=newsitem['image'][0]["url"]
            print(img)
        except:
            print("No Image for this story")
    
    return headlines
 
# A list to hold all headlines
allheadlines = []
 
# List of RSS feeds that we will fetch and combine
newsurls = {
    'apnews':      'https://www.yenisafak.com/Rss'
}
 
# Iterate over the feed urls
for key,url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend( getHeadlines( url ) )
 
 
# Iterate over the allheadlines list and print each headline
for hl in allheadlines:
    print(hl)
 
 