from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from auth_data import username, password
import time
import random


#def login(username, password):

#	browser = webdriver.Chrome('D:\\Project\\Python\\bot_for_inst\\chromedriver\\chromedriver')

#	try:

#		browser.get('https://www.instagram.com/')
#		time.sleep(random.randrange(1, 5))

#		username_input = browser.find_element_by_name('username')
#		username_input.clear()
#		username_input.send_keys(username)

#		time.sleep(3)

#		password_input = browser.find_element_by_name('password')
#		password_input.clear()
#		password_input.send_keys(password)

#		password_input.send_keys(Keys.ENTER)

#		time.sleep(10)

#		browser.close()
#		browser.quit()
#	except Exception as ex:
#		print(ex)
#		browser.close()
#		browser.quit()



#login(username, password)

def hashtag_search(username, password, hashtag):
	browser = webdriver.Chrome('D:\\Project\\Python\\bot_for_inst\\chromedriver\\chromedriver')

	try:

		browser.get('https://www.instagram.com/')
		time.sleep(random.randrange(1, 5))

		username_input = browser.find_element_by_name('username')
		username_input.clear()
		username_input.send_keys(username)

		time.sleep(3)

		password_input = browser.find_element_by_name('password')
		password_input.clear()
		password_input.send_keys(password)

		password_input.send_keys(Keys.ENTER)
		time.sleep(10)

		try:
			browser.get(f'https://www.instagram.com/explore/tags/{hashtag}')
			time.sleep(5)

			for i in range(1, 4):
				browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
				time.sleep(random.randrange(3, 5))

			hrefs = browser.find_elements_by_tag_name('a')

			post_urls = [item.get_attribute('href') for item in hrefs if'/p/' in item.get_attribute('href')]	

			for url in post_urls[0:1]:
				try:
					browser.get(url)
					like_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
					time.sleep(5)
				except Exception as ex:
					print(ex)
					browser.close()
					browser.quit()


			browser.close()
			browser.quit()
		except Exception as ex:
			print(ex)
			browser.close()
			browser.quit()

	except Exception as ex:
		print(ex)
		browser.close()
		browser.quit()

hashtag_search(username, password, 'Python')