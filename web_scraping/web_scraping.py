from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = "https://www.skalnik.pl/catalogsearch/result/index/?q=zestaw+ekspresow&product_list_order=price"

uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"product-item-info"})

filename = "Ekspresy.csv"
f = open(filename,"w")

headers = "Nazwa, Cena zestawu, Ilość, Cena na sztukę\n"
f.write(headers)

for container in containers:
    product_name = container.a.img["title"]
    
    prize_container = str(container.find("span", {"class":"price"}))
    product_prize = prize_container[prize_container.find(">")+1 : prize_container.rfind("<")].replace(",",".")

    temp = product_name.split(" EKSPRES")[0]
    amount = temp[-1] if temp[-1].isdigit() else product_name[product_name.find("-PAK")-1] if "-PAK" in product_name else 0

    if not amount:
        print(f"error: {product_name}")
        continue

    one_prize = str(round(float(product_prize.split()[0].replace(",",".")) / int(amount), 2))   
    f.write(product_name + "," + product_prize + "," + amount + "," + one_prize + "\n")
    
f.close()    