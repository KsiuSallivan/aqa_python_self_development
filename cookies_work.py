from selenium import webdriver
import pickle

# нужно записвать куки с той страницы, где ты авторизован
browser = webdriver.Chrome()
browser.get('https://github.com/KsiuSallivan/aqa_python_self_development')
pickle.dump(browser.get_cookies(), open('session', 'wb'))
print('Куки сохранены')

for cookie in pickle.load(open('session', 'rb')):
    browser.add_cookie(cookie)
print('Куки загружены')
browser.get('https://github.com/KsiuSallivan/aqa_python_self_development')

browser.refresh()
browser.quit()
