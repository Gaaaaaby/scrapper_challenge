import requests
from bs4 import BeautifulSoup

FIRST_WEBSITE_URL = 'https://www.hiperlibertad.com.ar/'
WEBSITE_URL = 'https://www.hiperlibertad.com.ar/lavarropas-carga-frontal-drean-7kg-900-rpm-next-7-09-eco-blanco/p'

try:
    r = requests.get(WEBSITE_URL)
    if r.ok: 
        print("Sucessfull connection")
    else:
        print('Bad request for:', WEBSITE_URL, r.status_code)
except requests.exceptions.ConnectionError as exc:
            #print('No se pudo conectar a la pagina', WEBSITE, r.status_code)
            print(exc)

soup = BeautifulSoup(r.content, 'html.parser')

name = soup.find("div", {'class':'productName'}).text
price = soup.find("input", {'id':'___rc-p-dv-id'})['value']
branch_office = soup.find("div", {'id':'stores-data'})
print(branch_office)

#javascript 

#const productName = $("div[class='styles__Container-sc-1ovmlws-1 cannud'] h1").text()
print("hi")
print(89)
class Product():
    def __init__(self, url):
        self.raw_html = url
        soup = BeautifulSoup(url, 'html.parser')
        self.name = soup.find("div", {'class':'productName'}).text
        price = soup.find("input", {'id':'___rc-p-dv-id'})['value']
        price_ = price.replace(',', '.')
        self.price = float(price_)

    def __str__(self):
        return "Name: {}\nPrice: {}".format(self.name, self.regular_price)
    
"""  def check_url(self):
        try:
            r = requests.get(WEBSITE_URL)
            if r.ok and r[-1,-3] == "/p": 
                print("Sucessfull connection")
            else:
                print('Bad request for: {}'.format( WEBSITE_URL, r.status_code)
        except requests.exceptions.ConnectionError as exc:
            #print('No se pudo conectar a la pagina', WEBSITE, r.status_code)
            print(exc) """
        


p1 = Product('<html>,</html>')
p1.name 
          

class ProductData():
    def __init__(self, name, regular_price):
          self.name = name
          price_ = regular_price.replace(',', '.')
          self.regular_price = float(price_)
    """self.regular_price = regular_price
          self.published_price = published_price
          self.category = category
          self.sku = sku
          self.url = url
          self.stock = stock
          self.description = description """
    
    def __str__(self):
        return "Name: {}\nPrice: {}".format(self.name, self.regular_price)



pq1 = ProductData(name, price)



print(str(pq1))



      