from bs4 import BeautifulSoup
import requests
#import cookielib
import json
import re
import os
import urllib.request
#https://github.com/AxelAli/Picture-Quest

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')


query = input("What do i search for? ")#you can search for single words like "monkey" or "Horse", but you can also search dalmatian dog" or "red car"
image_type="anime"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print (url)
#we store them in DIR/query , ex. data/horse
DIR="data"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print("there are total" , len(ActualImages),"images")


ActualImages=[]# gets full resolution images, not thumbnails
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print ("I Found" , len(ActualImages)," images!")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
for i , (img , Type) in enumerate( ActualImages):
    try:
        req = urllib.request.Request(img, headers={'User-Agent' : header})
        raw_img = urllib.request.urlopen(img).read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print (cntr)
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            print("Nein")
            #f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : "+img)
        print (e)

#python C:\Users\I342505\Desktop\Tensorflow-Image-Classification-master\image_retraining\retrain.py --bottleneck_dir=./processed-data/bottlenecks --how_many_training_steps 1000  --model_dir=./processed-data/inception --output_graph=./processed-data/retrained_graph.pb --output_labels=./processed-data/retrained_labels.txt --image_dir  C:\Users\I342505\Desktop\Tensorflow-Image-Classification-master\data\




