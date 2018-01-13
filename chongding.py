# coding=utf-8
import os
import time
from PIL import Image
import wda
import pytesseract
import re
import webbrowser
import urllib

r = re.compile(r'[0-9]\.*.?')

c = wda.Client()
s = c.session()
screenshot_backup_dir = 'screenshot_backups/'
if not os.path.isdir(screenshot_backup_dir):
    os.mkdir(screenshot_backup_dir)

def pull_screenshot():
    c.screenshot('1.png')

while(True):
	q = input('input:')
	start = time.time()
	if q.startswith('q'):
		break
	pull_screenshot()
	s = pytesseract.image_to_string(Image.open('./1.png'), lang='chi_sim')
	print(s)
	l = s.split('\n\n')
	for i in range(len(l)):
	    s = l[i]
	    s = ''.join(s.split('\n'))
	    l[i] = s
	print(l)

	word = ''
	for s in l:
	    g = r.match(s)
	    if g != None:
	        print(s)
	        word = s
	        break
	p = {'wd':word}
	url = 'http://www.baidu.com/s?' + urllib.parse.urlencode(p)
	webbrowser.open(url)
	end = time.time()
	print('using time:', end-start)
