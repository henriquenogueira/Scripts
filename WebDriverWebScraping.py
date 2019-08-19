import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('SEU SITE')
time.sleep(15) # Let the user actually see something!
search_box = driver.find_element_by_name('username')
search_box.send_keys('SEU USUARIO')
search_box = driver.find_element_by_name('password')
search_box.send_keys('SEU SITE')
search_box.submit()
time.sleep(5)
driver.get('SEU SITE')
time.sleep(35)

# BUSCA UNIDADES INICIO

elements = []


num_elementos = driver.execute_script('return document.getElementsByClassName("ubntLink ng-binding").length')
print(type(num_elementos))

for i in range(0, num_elementos):
    elemento = driver.execute_script(f'return document.getElementsByClassName("ubntLink ng-binding").item({i}).text')
    elements.append(elemento)
    

unidades1 = list(dict.fromkeys(elements))
qtd_unidades = len(unidades1)

# BUSCA UNIDADES FIM


for i in range(1, 4):
    unidades = list(dict.fromkeys(elements))
    entra = driver.find_element_by_link_text(f'{unidades[i]}')
    entra.click()
    time.sleep(10)
        
    url = driver.current_url
    ir = url[:60]
    config = ir + '/settings/wlans'
    driver.get(config)
    time.sleep(20)

    unidades = driver.find_elements_by_xpath('//*[@id="wirelessNetworksTable"]/tbody/tr[1]/td[5]/button[1]')[0]
    unidades.click()

    unidades = driver.find_elements_by_xpath('//*[@id="wirelessNetworkSettings"]/div[2]/div/form/fieldset/div[1]/div[6]/div[2]/div/div/a')[0]
    unidades.click()

    unidades1 = driver.execute_script('return document.getElementsByName("wirelessNetworkName").item(0).value')
    unidades2= driver.execute_script('return document.getElementsByName("wirelessNetworkWpaPskKey").item(0).value')
    time.sleep(20)

    print(unidades1,unidades2) 

    driver.get('https://bodytech.unifi.zoox.com.br:8443/manage/overview/sites')
    time.sleep(40)

    txt = open("senhas.txt","w+")
    txt.write("Unidade: " + entra + "SSID: " + unidades1 + " " + "Senha: " + unidades2)
    txt.close()