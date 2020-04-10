import requests, pandas
from bs4 import BeautifulSoup

""" requests module - allows you to send HTTP requests using Python
    BeautifulSoup - used for pulling data out of HTML and XML files  """


r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
#requests.get() - allows you to send the HTTP Request to the website

c = r.content #.content() - shows the content from the HTTP request
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div",{"class":"propertyRow"}) #finds all data matching the div tag with class attributes matching 'propertyRow'

page_nr = soup.find_all("a", {"class":"Page"})[-1].text #used to scrape the webpage for the page no of search results

""" Create an empty list that will store a dictionary of the extracted data """
el = [] #Empty List

for page in range(0,int(page_nr)*10,10):
    base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
    current_url = base_url+ str(page) + ".html"
    r = requests.get(current_url,headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div",{"class":"propertyRow"})

    """ Use a for loop to iterate over the "All" Resultset to extract the Price, Address, no of Beds, Square Footage, no of Full & Half Baths """
    for i in all:
        d = {} #Empty Dictionary
        d["Price"] = i.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","") #Extracts Price
        d["Address"] = i.find_all("span",{"class","propAddressCollapse"})[0].text #Extracts Street Address
        d["Locality"] = i.find_all("span",{"class","propAddressCollapse"})[1].text #Extracts City, State & Zip Code
        
        """ Due to the absence of some information for some of the results, the code will return a None datatype.
            To avoid an error use try/except to change the None datatype to a String value that returns "None" 
        """
        
        try:
            d["Beds"] = i.find("span",{"class","infoBed"}).find("b").text #Extracts Beds
        except:
            d["Beds"] = None

        try:
            d["Area"] = i.find("span",{"class","infoSqFt"}).find("b").text #Extracts Square Footage
        except:
            d["Area"] = None

        try:
            d["Full Baths"] = i.find("span",{"class","infoValueFullBath"}).find("b").text #Extracts Full Baths
        except:
            d["Full Baths"] = None

        try:
            d["Half Baths"] = i.find("span",{"class","infoValueHalfBath"}).find("b").text #Extracts Half Baths
        except:
            d["Half Baths"] = None
        

        """ Use for loop to iterate over items with the class = columnGroup to extract the featureGroup & featureName objects.
            Within the loop, use another for loop to iterate over the 2 object lists (featureGroup & featureName) and use an
            IF statement to find the featureGroup with the title - "Lot Size". Return the associated featureName for the Lot Size 
            featureGroup """

        for column_group in i.find_all("div",{"class":"columnGroup"}):
            for fg, fn in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in fg.text:
                    d["Lot Size"] = fn.text

        el.append(d) #Append each iteration of the outermost for loop's 'd' dictionary to the list 'el'

df = pandas.DataFrame(el) #Convert the list
df.to_csv("Output.csv")





