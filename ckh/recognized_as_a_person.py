from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach",True)
options.add_argument("--disalbe-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

driver.get("https://mvnrepository.com/search?q=what")