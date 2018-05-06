from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_Url = ("http://agmarknet.gov.in/agnew/namticker.aspx")

Client = uReq(my_Url)
html = Client.read()
Client.close()


# Using BEAUTIFUL SOUP to fetch the webapage
page_soup= soup(html , "html.parser")

#Fetching the table with id - DataListTracker  in the webapage
table = page_soup.find_all('table',{'id':'DataListTicker'})


#Creating a CSV file to write all the datas into.
filename = "products.csv"
f = open(filename,"w")

#Headers of the CSV File
headers = "Product, ProductType, MinPrice, MaxPrice\n"
f.write(headers)

#Iterating through all the data inside the table
for i in table:

    #Fetching <tr> tag inside the table
    tr = i.find_all('tr')

    #Again Iterating through <tr> tag and finding possible things inside
    for y in tr:

        # Found the <td> tag that consists all the details of the products.
        td = y.find_all('td')

        # Found the number of elements inside it
        elements =  (len(td))

#
#iterating through the last value of "elements" to grab all the details
for i in  range(0,elements):

        idProductType = "DataListTicker_lblTicker_" + str(i)
        idProductTypeSub = "DataListTicker_lblTitle_" + str(i)
        idMinPrice = "DataListTicker_lblminprice_" + str(i)
        idMaxPrice = "DataListTicker_lblMaxprice_" + str(i)

#Fetching products
        ProductType = page_soup.findAll('span', {'id': idProductType})
#Fetching subProducts
        ProductTypeSub = page_soup.findAll('span', {'id': idProductTypeSub})
#Fetching MinPrice
        MinPrice = page_soup.findAll('span', {'id': idMinPrice})
#Fetching MaxPrice
        MaxPrice = page_soup.findAll('span', {'id': idMaxPrice})

        print(ProductType[0].text,
              ProductTypeSub[0].text,
              '\nMin Price :', MinPrice[0].text,
              '\nMax Price :', MaxPrice[0].text),"\n\n"



        f.write(ProductType[0].text + "," + ProductTypeSub[0].text + "," + MinPrice[0].text + "," + MaxPrice[0].text +"\n")
f.close()



































