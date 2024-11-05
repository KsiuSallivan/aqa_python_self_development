from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://github.com/KsiuSallivan/aqa_python_self_development')
browser.save_screenshot('1.png')
browser.refresh()
browser.quit()