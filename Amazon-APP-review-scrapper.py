import urllib2

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.data = []
  def handle_starttag(self, tag, attrs):
    if tag == 'span':
      for name, value in attrs:
        if name == 'data-hook' and value == 'review-body':
		  self.recording = 1


  def handle_endtag(self, tag):
    if tag == 'span' and self.recording:
      self.recording -=1

  def handle_data(self, data):
    if self.recording:
      print data
      self.data.append(data)

for x in range(1, 257):
	url='''https://www.amazon.com/<App Name>/product-reviews/<APP ID>/ref=cm_cr_getr_d_paging_btm_256?ie=UTF8&reviewerType=all_reviews&pageNumber=%d'''%(x)
	try: f = urllib2.urlopen(url)
	except: page=""
	p = MyHTMLParser()
	html = f.read()
	p.feed(html)
	p.close()
