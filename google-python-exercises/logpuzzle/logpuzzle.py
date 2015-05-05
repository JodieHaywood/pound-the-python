import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    with open(filename, 'r') as f:
        l = f.readlines()
    urls = sorted(list(set(['http://code.google.com'+s[s.find('GET ')+4:s.find('.jpg')+4] for s in l if ('.jpg' in s) and ('puzzle' in s)])))
    urls = [x[1] for x in sorted([(s[s.find('.jpg')-4:],s) for s in urls])]
    return urls
  

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    os.mkdir('./'+dest_dir)
    name_list = []
    i = 0 
    for url in img_urls:
    #     name = url[url.find('.jpg')-6:url.find('.jpg')]
        name = './'+dest_dir+'/image'+str(i)
        name_list.append('image'+str(i))
        print name
        yay = urllib.urlretrieve(url, name)
        i += 1
        
    html_str = """
    <verbatim>
    <html>
    <body>
    """
    for name in name_list:
        html_str += '<img src="'+name+'">'
    html_str += """
    </body>
    </html>"""
    with open('./'+dest_dir+'/index.html', 'w') as f:
        f.write(html_str)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
