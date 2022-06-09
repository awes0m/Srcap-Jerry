link= "https://www.google.com/search?q=donald+trump&oq=donald+trump&aqs=chrome..69i57j0i433i512l2j0i512j0i433i512l2j46i433i512j0i433i512l2j0i512.3248j0j7&sourceid=chrome&ie=UTF-8"

from os import startfile 
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get(link)

with open('googleresults.csv','w') as f:
    f.write('Tittle,Link.Detail')
    for element in driver.find_elements_by_xpath('//div[@class="g"]'):
        title=element.find_element_by_xpath('.//h3').text
        link=element.find_element_by_xpath('.//div[@class="TbwUpd NJjxre"]/cite').text
        short=element.find_element_by_xpath('.//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"]/span').text
        f.write(title.replace(',','|')+','+link.replace(',','|')+','+short.replace(',','|')+"\n")
        
