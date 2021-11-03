import csv
import time
from bs4.element import TemplateString
from selenium import webdriver
from bs4 import BeautifulSoup as bs

starturl = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("C:\Users\rohit\Downloads\chromedriver_win32")
browser.get(starturl)
time.sleep(10)
def scrap():
    Headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data = []
    for i in range(0,92) :
        soup = bs(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs = {"class","exoplanet"}):
            litags = ultag.find_all("li")
            temp = []
            for index,litags in enumerate(litags):
                if index == 0 :
                    temp.append(litags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp.append(litags.contents[0])
                    except:
                        temp.append("")
            planet_data.append(temp)
        browser.find_element_by_xpath('//*[@id="results"]/ul[2]/li[1]/a').click()
     with open("scrapper_1.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(Headers)
        csvwriter.writerows(planet_data)
scrape()