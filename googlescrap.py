import random
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import colorama
import sys
from selenium.webdriver.chrome.service import Service
from progress.bar import Bar
from colorama import Back, Fore, Style
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Banner():
    colorama.init(autoreset=True)
    print(Fore.RED + """                                                                      
 @@@@@@    @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@   
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
!@@       !@@       @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!       !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!!@@!!    !@!       @!@!!@!   @!@!@!@!  @!@@!@!   @!!!:!    @!@!!@!   
 !!@!!!   !!!       !!@!@!    !!!@!!!!  !!@!!!    !!!!!:    !!@!@!    
     !:!  :!!       !!: :!!   !!:  !!!  !!:       !!:       !!: :!!   
    !:!   :!:       :!:  !:!  :!:  !:!  :!:       :!:       :!:  !:!  
:::: ::    ::: :::  ::   :::  ::   :::   ::        :: ::::  ::   :::  
:: : :     :: :: :   :   : :   :   : :   :        : :: ::    :   : :  
                                                     coded by KHASEY               
        """)

def Start(driver):
    try: driver.get("https://swisscows.com")
    except: print("Problem with the custom header")  

def Wait():
    time.sleep(3)
        
def Search(driver, current):
    try:
        search_box = driver.find_element(By.XPATH,'/html/body/div/div/header/div[3]/div[2]/form/div/div/input')
        search_box.send_keys(current) # Attendez un bref moment entre chaque caractère
        
        Wait()
        driver.find_element(By.XPATH,'/html/body/div/div/header/div[3]/div[2]/form/div/div/input').send_keys(Keys.ENTER)
    except:
        print("pas de recherche")
  

def Write(driver):
    try:
        cites = driver.find_elements(By.TAG_NAME, 'a')
        with open('websitegoogle.txt', 'a+') as f:  # Open the file in 'a+' mode to read and append
            existing_links = f.read().splitlines()  # Read the existing content and split it into lines
            for cite in cites:
                if cite.text.startswith("ww"):
                    parts = cite.text.split(' ', 1)
                    # modified_text = '\n'.join(parts)
                    # link = modified_text.split('\n', 1)[0]  # Get the link part before the newline
                    if parts not in existing_links:  # Check if the link is not already in the file
                        f.write("%s\n" % parts[0])
                     
    except:
        print("pas de file")


                
        

def Next(driver):
    try:
        page_number = 1  # Initialiser le numéro de page
        max_count = 100  # Définir une valeur max pour la barre de progression
        bar = Bar(Fore.RED + 'Pages =>', max=max_count, fill='#')
        while page_number <= max_count:
            try:
                # Choisir le sélecteur CSS en fonction de la page
                css_selector = '.named' if page_number == 1 else 'li.named:nth-child(7)'
                ret_elements = driver.find_element(By.CSS_SELECTOR, css_selector)
            except NoSuchElementException:
                print("pas de next")
                break  # Si le bouton n'est pas trouvé, sortir de la boucle

            Write(driver)  # Écrire les données de la page actuelle
            time.sleep(1)  # Attendre avant de cliquer
            ret_elements.click()  # Cliquer sur le bouton de pagination
            bar.next()  # Mettre à jour la barre de progression
            page_number += 1  # Incrementer le numéro de page
            time.sleep(1.5) # Attendre avant de continuer (supposant que Wait est une fonction définie ailleurs)
    except:
        print(Fore.GREEN + "Scrap is over")

Banner()

if len(sys.argv) < 2:
    print("usage => python3 <prog name> <args>")
    exit()

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',  # Tor Browser for Windows and Linux
    'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',  # Tor Browser for Android
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '

    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
]

options = FirefoxOptions()
options.add_argument(f'user-agent={random.choice(user_agents)}')

driver = webdriver.Firefox(service=Service('./geckodriver'), options=options)
first = True
for current in sys.argv[1:]:
    print("Processing argument: " + current)
    Start(driver)
    Wait()
    # if (first):
    #     driver.find_element(By.XPATH, '//*[@id="L2AGLb"]').click()
    #     first = False
    # # Wait()
    Search(driver, current)
    Wait()
    Next(driver)
driver.quit()

