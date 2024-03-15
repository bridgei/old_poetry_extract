from selenium import webdriver
import time

# Main Function
if __name__ == '__main__':

	# options = webdriver.ChromeOptions()
	# options.add_argument("--start-maximized")
	# options.add_argument('--log-level=3')

	# Provide the path of chromedriver present on your system.
	driver = webdriver.Firefox()

	# Send a get request to the url
	driver.get('https://www.geeksforgeeks.org/')
	time.sleep(60)
	driver.quit()
	print("Done")
