from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

# Configuración del driver
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

# Ir a instagram
sleep(2)
driver.get('https://www.instagram.com/accounts/login/')
sleep(3)

# Aceptar cookies
button_cookies = driver.find_element_by_xpath(
    '/html/body/div[3]/div/div/button[1]')
button_cookies.click()
sleep(3)

# Entrar
username = driver.find_element_by_name('username')
username.send_keys('trecno_')
password = driver.find_element_by_name('password')
password.send_keys('p4$$w0rD')
button_login = driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[3]/button')
button_login.click()
sleep(5)
print('Sesión iniciada')

# Procesar hashtags
hashtag_list = ['perro', 'gato', 'ave']

for hashtag in hashtag_list:
    driver.get('https://www.instagram.com/explore/tags/' + hashtag)
    sleep(5)

    first_thumbnail = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/section/main/article/div[1]/div/div/div[1]/div[1]')
    first_thumbnail.click()
    sleep(5)

    for n in range(5):  # Me gusta y comentario en el post n
        try:
            # Me gusta
            button_like = driver.find_element_by_xpath(
                '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]')
            button_like.click()
            sleep(random.randint(1, 5))

            # Comentario
            reactions = ['😍', '😯', 'Wow!!']
            try:
                input_comment = driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                input_comment.click()
            except:
                pass
            input_comment = driver.find_element_by_xpath(
                '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
            input_comment.send_keys(random.choice(reactions))
            input_comment.send_keys(Keys.ENTER)
            sleep(random.randint(1, 5))

            print('Post ' + str(n) + ' en #' + hashtag)

            # Ir al siguiente post
            button_next = driver.find_element_by_css_selector(
                '.coreSpriteRightPaginationArrow')
            button_next.click()
            sleep(random.randint(3, 5))
        except:
            print('Ocurrió una excepción')
    print('#' + hashtag + ' completado')
