'''
@author     : Ananthakrishnan G

source:     : https://medium.com/featurepreneur/selenium-c78e87cc8c4a

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv


header = ['name','url','price','category','store','ratings','fivestar','fourstar','threestar','twostar','onestar']
data    = []


driver = webdriver.Chrome(ChromeDriverManager().install())




def write_csv():
    
    with open('data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)




def scrape(link):

    try:

        driver.get(link)
        title       =   driver.find_element(By.XPATH,'//*[@id="productTitle"]').text
        category    =   driver.find_element(By.XPATH,'//*[@id="nav-subnav"]/a[1]/span').text
        price       =   driver.find_element(By.XPATH,'//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]').text
        store       =   driver.find_element(By.XPATH,'//*[@id="merchant-info"]/a[1]/span').text

        rate     =   driver.find_element(By.XPATH,'//*[@id="acrCustomerReviewText"]').text
        fivestar    =   driver.find_element(By.XPATH,'//*[@id="histogramTable"]/tbody/tr[1]/td[3]/span[2]/a').text
        fourstar    =   driver.find_element(By.XPATH,'//*[@id="histogramTable"]/tbody/tr[2]/td[3]/span[2]/a').text
        threestar   =   driver.find_element(By.XPATH,'//*[@id="histogramTable"]/tbody/tr[3]/td[3]/span[2]/a').text
        twostar     =   driver.find_element(By.XPATH,'//*[@id="histogramTable"]/tbody/tr[4]/td[3]/span[2]/a').text
        onestar     =   driver.find_element(By.XPATH,'//*[@id="histogramTable"]/tbody/tr[5]/td[3]/span[2]/a').text

    
        ratings     = int(rate[:-8].replace(",", ""))

        # For the NUMBER of individual star ratings

        # five_star   = int((ratings*int(fivestar[:-1])) /100)
        # four_star   = int((ratings*int(fourstar[:-1])) /100)
        # three_star  = int((ratings*int(threestar[:-1]))/100)
        # two_star    = int((ratings*int(twostar[:-1]))  /100)
        # one_star    = int((ratings*int(onestar[:-1]))  /100)



        # For the PERCENTAGE of individual star ratings

        five_star   = int(fivestar[:-1])
        four_star   = int(fourstar[:-1])
        three_star  = int(threestar[:-1])
        two_star    = int(twostar[:-1])
        one_star    = int(onestar[:-1])



        info_dict = {
            "name"          : title,
            "url"           : link,
            "price"         : price,
            "category"      : category,
            "store"         : store,
            "ratings"       : ratings,
            "fivestar"      : five_star,
            "fourstar"      : four_star,
            "threestar"     : three_star,
            "twostar"       : two_star,
            "onestar"       : one_star
        }
        
        data.append(info_dict)

    except:
        pass


def link():
    file = open("links.csv", "r")
    for link in file.readlines():
         scrape(link)

if __name__ == '__main__':
    link()
    write_csv()