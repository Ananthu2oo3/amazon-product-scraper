'''
@author     : Ananthakrishnan G

source:     : https://medium.com/featurepreneur/selenium-c78e87cc8c4a

'''


def startpy():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    count = 0

    keys = open('keys.txt', 'r')
    for key in keys:
        key.replace(" ","+")
        for i in range (1,30):
            try:
                driver.get(f'https://www.amazon.in/s?k={key}&page={i}&ref=sr_pg_{i}')

                all_links = driver.find_elements(By.XPATH,"//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
                
                file = open('links.csv','a')
                for i in all_links:
                    
                    links = i.get_attribute('href')    
                    count+=1
                    file.write(f'{links}\n')
                    count+=1
                

            except:
                pass

            if(count >= 15):
                count = 0
                break
                


if __name__ == '__main__':
    startpy()



