from selenium import webdriver  

class Bot :
	def __init__(self):
		self.driver = webdriver.Firefox()
		self.navigate()

	def navigate(self):
		self.driver.get('https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=-1&room1=1&room2=1')

		button = self.driver.find_elements_by_xpath('//button[@class="button_component-button-eCvYMNeIZGW button_component-S-53KhykMSdyY button_component-default-55Cf8OHDN6g button_component-primary-5MrtQPVeXCA c6e8ba5398-button--3NqeV c6e8ba5398-simplified-button--2Iboi"]')
		for i in range(len(button)):
			button[i].click()
			i = i + 1

		numbers = self.driver.find_elements_by_xpath('//div[@class="c6e8ba5398-text--2b1-6 c6e8ba5398-simplified-text--1mkqT"]')
		names = self.driver.find_elements_by_xpath('//div[@class="c6e8ba5398-name--29wcs c6e8ba5398-agent-section--wMjBq"]')
		for i in range(len(numbers)):
			print(numbers[i].text)
			print(names[i].text)
			i = i + 1

def main():
	b = Bot()


if __name__ == '__main__':
	main()