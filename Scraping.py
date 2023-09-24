from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Creating a WebDriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://www.wikipedia.org/')

search_input = driver.find_element(By.ID, 'searchInput')
search_input.send_keys('ASD')

search_button = driver.find_element(by=By.CLASS_NAME, value='pure-button')

driver.execute_script("arguments[0].click();", search_button)

link_element = driver.find_element(By.LINK_TEXT, 'Adaptive software development')

driver.execute_script("arguments[0].click();", link_element)

p_tags = driver.find_elements(By.TAG_NAME, 'p')

text_lines = ''
for p in p_tags:
    text_lines += p.text

print(text_lines)

elems = driver.find_elements(by=By.CSS_SELECTOR, value='li a')
print(elems)

list_dict = {}
for elem in elems:
    list_dict[elem.text] = elem.get_attribute('href')

print(list_dict)
