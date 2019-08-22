import time
from selenium import webdriver


driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('xxxxxxx') # site a ser adicionado
time.sleep(15) # Esperar o site ser carregado
search_box = driver.find_element_by_name('username')
search_box.send_keys('xxxxxxxxxxxxxx') # seu usuário para login
search_box = driver.find_element_by_name('password')
search_box.send_keys('xxxxxxxxxxxx') # sua senha para login
search_box.submit()
time.sleep(5)

#lista de unidades
elements = []

# lista total de itens da lista de unidades
totalDeElementosLista = driver.execute_script('return document.getElementsByClassName("appOrgSwitcher__item").length')

# remove os itens não necessários da lista
listaDeUnidades = totalDeElementosLista - 9 

# abre o dropdown
elemento = driver.execute_script('return document.getElementsByClassName("appOrgSwitcher__arrow icon ubnt-icon--pointer-down")')[0]
elemento.click()

# adiciona elementos do menu dropdown e armazena em uma lista
for i in range(1, listaDeUnidades):
       
    elemento = driver.execute_script(f'return document.getElementsByClassName("appOrgSwitcher__item").item({i}).textContent')
    elements.append(elemento) 

# fecha o menu dropDown
time.sleep(10)
elemento = driver.execute_script('return document.getElementsByClassName("appOrgSwitcher__arrow icon ubnt-icon--pointer-down")')[0]
elemento.click()   

# Começa capturar e abrir unidade por unidade

for i in range(0, listaDeUnidades):
    
    # abre o menu dropdown
    elemento = driver.execute_script('return document.getElementsByClassName("appOrgSwitcher__arrow icon ubnt-icon--pointer-down")')[0]
    elemento.click()
    time.sleep(5) 
    
    
    try:
       # busca o primeiro elemento da lista e clica para carregar
        entra = driver.find_element_by_link_text(f'{elements[i]}')
        entra.click()
        time.sleep(5)

        # pega a url atual e adiciona a extensão necessária do settings
        url = driver.current_url
        ir = url[:60]
        config = ir + '/settings/site'
        driver.get(config)
        time.sleep(20)

        # armazena o nome da unidade que está sendo consultado
        site_unidade = driver.execute_script('return document.getElementsByName("siteName").item(0).value')
        
        # pega a url atual e adiciona a extensão necessária para abrir as configs da lan
        url = driver.current_url
        ir = url[:60]
        config = ir + '/settings/wlans'
        driver.get(config)
        time.sleep(10)

        # Verifica quantidade de elementos da tabela de ssid's para tomar ação
        validaRedes = driver.execute_script('return document.getElementsByClassName("wlanName").length')
    
        # verifica se existe a rede tablet e bike 
        if (validaRedes >= 3):

            redeBike = driver.find_elements_by_xpath('//*[@id="wirelessNetworksTable"]/tbody/tr[1]/td[5]/button[1]')[0]
            redeBike.click()
            time.sleep(10)
            
            redeBikeSenha = driver.find_elements_by_xpath('//*[@id="wirelessNetworkSettings"]/div[2]/div/form/fieldset/div[1]/div[6]/div[2]/div/div/a')[0]
            redeBikeSenha.click()
            time.sleep(10)

            ssidBike = driver.execute_script('return document.getElementsByName("wirelessNetworkName").item(0).value')
            senhaBike= driver.execute_script('return document.getElementsByName("wirelessNetworkWpaPskKey").item(0).value')
            time.sleep(15)

            voltar = driver.find_element_by_xpath('//*[@id="wirelessNetworkSettings"]/div[2]/div/form/div/div/button[2]')
            voltar.click()
            time.sleep(15)

            
            redeTablet = driver.find_elements_by_xpath('//*[@id="wirelessNetworksTable"]/tbody/tr[3]/td[5]/button[1]')[0]
            redeTablet.click()
            time.sleep(10)

            redeTabletSenha = driver.find_elements_by_xpath('//*[@id="wirelessNetworkSettings"]/div[2]/div/form/fieldset/div[1]/div[6]/div[2]/div/div/a')[0]
            redeTabletSenha.click()
            time.sleep(10)

            ssidTablet = driver.execute_script('return document.getElementsByName("wirelessNetworkName").item(0).value')
            senhaTablet = driver.execute_script('return document.getElementsByName("wirelessNetworkWpaPskKey").item(0).value')
            time.sleep(10)
        
        elif(validaRedes <= 3):
            
            try:
                redeTabletSenha = driver.find_elements_by_xpath('//*[@id="wirelessNetworkSettings"]/div[2]/div/form/fieldset/div[1]/div[6]/div[2]/div/div/a')[0]
                redeTabletSenha.click()
                time.sleep(10)
            except:
                ssidTablet = driver.execute_script('return document.getElementsByName("wirelessNetworkName").item(0).value')
                senhaTablet = driver.execute_script('return document.getElementsByName("wirelessNetworkWpaPskKey").item(0).value')
                time.sleep(10)
        # imprime as unidade consultadas para acompanhar o funcionamento do programa
        print("Dados da unidade: \n" + site_unidade, ssidBike, senhaBike + "\n" + ssidTablet,senhaTablet) 

        # cria arquivo txt para armazenar senhas e ssid's
        txt = open("senhas.txt","a+")
        txt.write("Unidade: " + site_unidade + "\n" + "Dados das redes: \n" + "SSID: " + ssidBike + " SENHA: " + senhaBike + "\n" + "SSID: " + ssidTablet + " SENHA: " + senhaTablet + "\n" + "--------------------------------------------------------------------------------------------------------------" + "\n") 
        txt.close()
        time.sleep(15)


    except:
        # em caso de erro é recarregado novamente o site para uma nova tentativa do inicio
        driver.get('xxxxxxxxxxxxxx') # digite seu site
        time.sleep(10)
        
        elemento = driver.execute_script('return document.getElementsByClassName("appOrgSwitcher__arrow icon ubnt-icon--pointer-down")')[0]
        elemento.click()
        time.sleep(10)
        
        entra = driver.find_element_by_link_text(f'{elements[i]}')
        entra.click()
        time.sleep(10) 