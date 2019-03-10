import re


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleanr = re.compile('&lt;.*?&gt;')
  cleantext = re.sub(cleanr, '', cleantext)
  return cleantext

