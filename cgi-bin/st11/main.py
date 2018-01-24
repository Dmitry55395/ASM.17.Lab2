from .items import *
import cgi

def main(q, selfurl):
	It=Items(q, selfurl)
	print ("Content-type: text/html; charset=utf-8\n\n")
	if 'action' in q:
		if (q['action'].value=="1"): 
			It.read()
		if (q['action'].value=="2"):
			It.write()
		if (q['action'].value=="3"):
			It.delete()
	else: 
		It.write()
