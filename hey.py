
from bs4 import BeautifulSoup
#import requests
import re
import urllib.request
import os
#import cookielib
import json
import os.path

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),"html.parser")


query = input("query image \n")# you can change the query for the image  here
image_type= query #"ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print(url)
#C:\Users\I342505\Desktop\Image-Rec\dataset\test\one
#add the directory for your image here
#C:\Users\I342505\Desktop\Multi-label-Inception-net-master\images\multi-label
DIR="C:\\Users\\I342505\\Desktop\\Tensorflow-Image-Classification-master\\data"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print("there are total" , len(ActualImages),"images")


###print images
for i , (img , Type) in enumerate( ActualImages):
    try:
        req = urllib.request.Request(img, headers={'User-Agent' : header})
        raw_img = urllib.request.urlopen(img).read()
        if not os.path.exists(DIR):
            os.mkdir(DIR)
        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print(cntr)
        #C:\Users\I342505\Desktop\Multi-label-Inception-net-master\image_labels_dir
        textfile = os.path.join(image_type + "_"+ str(cntr)+".jpg"+ ".txt")
        if len(Type)==0:
            f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
            #file = open(textfile, "w")
            #file.write(image_type)
        else :
            f = open(DIR + image_type + "_"+ str(cntr)+"."+Type, 'wb')
            #file = open(textfile, "w")
            #file.write(image_type)

        f.write(raw_img)
        f.close()
    except Exception as e:
        print( "could not load : "+img)
        print( e)