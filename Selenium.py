from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
browser.get('https://www.google.com')
time.sleep(3)

search_box = browser.find_element_by_name("q")
search_box.send_keys('練馬　美味しい店')
search_box.submit()
time.sleep(3)

for g_h3 in browser.find_elements_by_css_selector(".g h3"):
    print(g_h3.text)
time.sleep(1)


stats = browser.find_element_by_id("resultStats").text
print(stats)
for i, g in enumerate(browser.find_elements(By.CLASS_NAME, "g")):
    print("------ " + str(i+1) + " ------")
    r = g.find_element(By.CLASS_NAME, "r")
    print(r.find_element(By.TAG_NAME, "h3").text)
    print("\t" + r.find_element(By.TAG_NAME, "a").get_attribute("href"))
    r.click()
    s = g.find_element(By.CLASS_NAME, "s")
    print("\t" + s.find_element(By.CLASS_NAME, "st").text)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Gmailのリンクをクリック
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Gmail"))
)

# Macの場合、COMMANDキーを押しながらGmailリンクをクリック
actions = ActionChains(browser)
actions.key_down(Keys.COMMAND)

# Windowsの場合はCTRLキー
# actions.key_down(Keys.CONTROL)

actions.click(element)
actions.perform()

browser.back()
browser.forward()
browser.refresh()
browser.quit()
