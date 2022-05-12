from selenium import webdriver
from selenium.webdriver.firefox.options import Options

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
driver = webdriver.Firefox(profile)

driver.get('https://check.torproject.org/')

