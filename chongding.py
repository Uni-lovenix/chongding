# coding=utf-8
import os
import time
import re
import shutil
from PIL import Image
import wda
import pytesseract
import webbrowser
import urllib
import jieba


i = 1
isusingjieba = False
r = re.compile(r'[0-9]\.*.?')
c = wda.Client()
s = c.session()
screenshot_backup_dir = 'screenshot_backups/'
if not os.path.isdir(screenshot_backup_dir):
    os.mkdir(screenshot_backup_dir)

    
def baidu_search(word):
	p = {'wd':word}
	url = 'http://www.baidu.com/s?' + urllib.parse.urlencode(p)
	webbrowser.open(url)

def google_search(word):
	p_g = {'q':word}
	url_g = 'https://www.google.co.jp/search?' + urllib.parse.urlencode(p_g)
	webbrowser.open(url_g)

def usingjieba(word):
	cuts = jieba.cut(word, cut_all=False)
	w = ''
	for i  in cuts:
	    # print(c)
	    w += i +' '
	return word

def bakpng():
	name = time.time()
	shutil.copyfile('./1.png', './screenshot_backups/'+str(name)+'.png')


def main():
	while(True):
		q = input('input:')
		start = time.time()
		if q.startswith('q'):
			break
		c.screenshot('1.png')
		s = pytesseract.image_to_string(Image.open('1.png'), lang='chi_sim')
		print(s)
		l = s.split('\n\n')
		for i in range(len(l)):
		    s = l[i]
		    s = ''.join(s.split('\n'))
		    l[i] = s
		# print(l)

		word = ''
		for i in range(len(l)):
		    g = r.match(l[i])
		    if g != None:
		        # print(l[i])
		        try:
		        	word = l[i] + l[i+1]
		        except:
		        	word = l[i]
		        break

		if isusingjieba:
			word = usingjieba(word)

		baidu_search(word)
		# google_search(word)

		end = time.time()
		print('using time:', end-start)
		bakpng()

if __name__ == '__main__':
	main()