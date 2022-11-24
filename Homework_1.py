from selenium import webdriver
import time
from fake_useragent import UserAgent

url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path='chromedriver.exe',
    options=options
)

try:
    driver.get(url=url)
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()