import urllib.request
#conn = urllib.request.urlopen('http://thinkpython.com/secret.html')
#for line in conn.fp:
 #   print(line.strip())
def getzipinfo(x):
    zipurl = urllib.request.urlopen('http://www.uszip.com/zip/'+ x)
    for line in zipurl.fp:
            print(line.strip())
            
getzipinfo('05478')