link= 'https://www.imdb.com/list/ls079327063/'

import os
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get(link)
Heading=driver.find_element_by_xpath('//div[@class="article listo"]/h1').text
with open('ImdbScrapper.csv','w') as f:
    f.write(Heading+'\n \n')
    f.write('Index no,Movie Name,Movie Link,Movie Poster \n')
    for element in driver.find_elements_by_xpath('//div[@class="lister-item mode-detail"]'):
        indexNo=element.find_element_by_xpath('.//span[@class="lister-item-index unbold text-primary"]').text
        movieName=element.find_element_by_xpath('.//h3[@class="lister-item-header"]/a').text
        pageLink=element.find_element_by_xpath('.//h3[@class="lister-item-header"]/a').get_attribute('href')
        movieposter=element.find_element_by_xpath('.//div[@class="lister-item-image ribbonize"]/a/img').get_attribute('src')

        f.write(indexNo.replace(',','|')+','+movieName.replace(',','|')+','+pageLink.replace(',','|')+','+movieposter.replace(',','|')+'\n')
        
driver.close()
    

    
    


