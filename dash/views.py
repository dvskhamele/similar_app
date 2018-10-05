from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


# Create your views here.
def similar_list(request):
	context={}
	if request.GET:
		if request.GET["appid"]:
			page = requests.get("https://play.google.com/store/apps/details?id=com.facebook.orca")
			soup = BeautifulSoup(page.content, 'html.parser')
			similink=soup.find_all('a', class_='LkLjZd')[0]["href"]

			browser = webdriver.Chrome('dash/chromedriver.exe')

			browser.get(similink)
			time.sleep(1)

			elem = browser.find_element_by_tag_name("body")

			no_of_pagedowns = 20

			while no_of_pagedowns:
				elem.send_keys(Keys.PAGE_DOWN)
				time.sleep(0.2)
				no_of_pagedowns-=1

			post_elems = browser.find_elements_by_class_name("square-cover")

			r=0
			d=[]
			for post in post_elems:
				r=r+1
				d.append(post.get_attribute("data-docid"))
				print(post.get_attribute("data-docid"))
				if r==250:
					break

			context['lis']=d
			context['l']=request.GET["appid"]



	return render(request, 'front.html', context)