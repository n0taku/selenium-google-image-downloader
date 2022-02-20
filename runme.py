from scraper import Scraper

scraper = Scraper("C:\\selenium\\chromedriver.exe")
img_list = scraper.getImageList("pikachu",10)
print(img_list)
scraper.quit()