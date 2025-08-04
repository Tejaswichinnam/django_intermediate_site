#from django.shortcuts import render,redirect
import requests

from bs4 import BeautifulSoup
import os
import re
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from login.models import Useradd,Contact
# from django.contrib.auth.decorators import login_required


url="https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DApple"
response=requests.get(url)
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div',class_="KzDlHZ")
#print(names) output in unstructured form ,so
name=[]
for i in names[2:20]:
    d=i.get_text()
    name.append(d)
#print(name)

prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
#print(prices) ..unstructured form
price=[]
for i in prices[2:20]:
    d=i.get_text()
    price.append(d)
#print(price)

links=soup.find_all('a',class_="CGtC98")
link=[]
for i in links[2:20]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)
#print(link)

images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images[2:20]:
    d=i['src']
    image.append(d)
#print(image)

mb_list=zip(name,
            price,
            link,
            image
            )

# def mobiles(request):
#     return render(request,"mobile.html",{'mb_list':mb_list})



#scooters data
url1="https://www.zigwheels.com/scooters"
response=requests.get(url1)
#print(response)

soup=BeautifulSoup(response.content,'html.parser')
names1=soup.find_all('a',class_="b clr c-p txt-ulne")
name1=[]
for i in names1[1:20]:
    d=i.get_text()
    name1.append(d)
#print(name1)
raw_data = [
    '\nSuzuki Access 125\t', '\nTVS Jupiter\t', '\nTVS NTORQ 125\t', '\nBajaj Chetak\t',
    '\nZelio Legender\t', '\nWarivo Motors Nova\t', '\nWarivo Motors Edge\t',
    '\nWarivo Motors Neo\t', '\nHonda X-ADV\t', '\nSuzuki e Access\t', '\nVida VX2\t',
    '\nVida Z\t', '\nKinetic Watts And Volts DX Electric\t', '\nSuzuki Burgman Electric\t',
    '\nBajaj Chetak\t', '\nYulu Wynn\t', '\nTVS iQube\t', '\nHonda Activa e\t', '\nOla S1 Pro\t'
]
cleaned_data = [item.strip() for item in raw_data]
#print(cleaned_data)

if not os.path.exists('downloaded_images'):
    os.makedirs('downloaded_images')
images1=soup.find_all('img',class_="sl-img clr" )
#print(images1)
image1=[]
for i in images1[1:20]:
   d=i['src']
   image1.append(d)
#print(image1)
html_data='''<img alt="Honda Activa 6G" class="sl-img clr" data-track-label="popular-scooter-bike" onclick="goToUrl('/honda-bikes/activa-6g');" src="https://media.zigcdn.com/media/model/2024/Mar/honda-activa-6g-std-right-side-view_270x180.jpg" style="opacity: 1;" title="Honda Activa 6G"/>, <img alt="Suzuki Access 125" class="sl-img clr" data-track-label="popular-scooter-bike" onclick="goToUrl('/suzuki-bikes/access-125');" src="https://media.zigcdn.com/media/model/2025/Jan/suzuki-access-125std-right-side-view_270x180.png" style="opacity: 1;" title="Suzuki Access 125"/>, <img alt="TVS Jupiter" class="sl-img clr" data-track-label="popular-scooter-bike" onclick="goToUrl('/tvs-bikes/jupiter');" src="https://media.zigcdn.com/media/model/2025/Mar/tvs-jupiter-110-std-right-side-view_270x180.jpg" style="opacity: 1;" title="TVS Jupiter"/>, <img alt="TVS NTORQ 125" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/May/tvs-ntorq-125-right-side-view_270x180.jpg" data-track-label="popular-scooter-bike" onclick="goToUrl('/tvs-bikes/ntorq-125');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="TVS NTORQ 125"/>, <img alt="Bajaj Chetak" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jun/bajaj-chetak-3503-right-side-view_270x180.jpg" data-track-label="popular-scooter-bike" onclick="goToUrl('/bajaj-bikes/chetak');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Bajaj Chetak"/>, <img alt="Zelio Legender" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jun/2025-zelio-e-mobility-legender-right-side-view_270x180.jpg" data-track-label="latest-scooter-bike" onclick="goToUrl('/zelio-bikes/legender');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Zelio Legender"/>, <img alt="Warivo Motors Nova" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jun/nova-right-side-view_270x180.jpg" data-track-label="latest-scooter-bike" onclick="goToUrl('/warivo-motors-bikes/nova');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Warivo Motors Nova"/>, <img alt="Warivo Motors Edge" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jun/warivo-edge-right-side-view_270x180.jpg" data-track-label="latest-scooter-bike" onclick="goToUrl('/warivo-motors-bikes/edge');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Warivo Motors Edge"/>, <img alt="Warivo Motors Neo" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jun/warivo-neo-right-side-vieq_270x180.jpg" data-track-label="latest-scooter-bike" onclick="goToUrl('/warivo-motors-bikes/neo');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Warivo Motors Neo"/>, <img alt="Honda X-ADV" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/May/honda-x-adv-right-side-view_270x180.jpg" data-track-label="latest-scooter-bike" onclick="goToUrl('/honda-bikes/x-adv-750');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Honda X-ADV"/>, <img alt="Suzuki e Access" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Mar/suzuki-e-access-right-side-view_270x180.jpg" data-track-label="upcoming-scooters-bike" onclick="goToUrl('/suzuki-bikes/e-access');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Suzuki e Access"/>, <img alt="Vida VX2" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/May/vida-vx2-right-side-view_270x180.jpg" data-track-label="upcoming-scooters-bike" onclick="goToUrl('/vida-bikes/vx2');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Vida VX2"/>, <img alt="Vida Z" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jan/vida-z-abc-right-side-view_270x180.jpg" data-track-label="upcoming-scooters-bike" onclick="goToUrl('/vida-bikes/z');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Vida Z"/>, <img alt="Kinetic Watts And Volts DX Electric" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jun/kinetic-dx-electric-right-side-view_270x180.jpg" data-track-label="upcoming-scooters-bike" onclick="goToUrl('/kinetic-watts-and-volts-bikes/dx-electric');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Kinetic Watts And Volts DX Electric"/>, <img alt="Suzuki Burgman Electric" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2021/Jul/burgman-electric_270x180.jpg" data-track-label="upcoming-scooters-bike" onclick="goToUrl('/suzuki-bikes/burgman-electric');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Suzuki Burgman Electric"/>, <img alt="Bajaj Chetak" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jun/bajaj-chetak-3503-right-side-view_270x180.jpg" data-track-label="best-electric-bike" onclick="goToUrl('/bajaj-bikes/chetak');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Bajaj Chetak"/>, <img alt="Yulu Wynn" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2024/Jul/yulu-wynn-std-right-side-view_270x180.jpg" data-track-label="best-electric-bike" onclick="goToUrl('/yulu-bikes/wynn');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Yulu Wynn"/>, <img alt="TVS iQube" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/May/tvs-iqube-3-5-kwh-right-side-view_270x180.jpg" data-track-label="best-electric-bike" onclick="goToUrl('/tvs-bikes/iqube-electric');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="TVS iQube"/>, <img alt="Honda Activa e" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2024/Nov/honda-activa-e-right-side-view_270x180.jpg" data-track-label="best-electric-bike" onclick="goToUrl('/honda-bikes/activa-electric');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Honda Activa e"/>, <img alt="Ola S1 Pro" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2025/Jan/ola-s1-pro-g3-right-side-view_270x180.jpg" data-track-label="best-electric-bike" onclick="goToUrl('/ola-electric-bikes/2025-s1-pro');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Ola S1 Pro"/>, <img alt="Yamaha RayZR 125 Fi Hybrid" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2024/Apr/yamaha-rayzr-125-right-side-view_270x180.jpg" data-track-label="best-mileage-bike" onclick="goToUrl('/yamaha-bikes/ray-zr-125');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Yamaha RayZR 125 Fi Hybrid"/>, <img alt="TVS XL100" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2024/Mar/tv-x-100-heavy-duty-right-side-view_270x180.jpg" data-track-label="best-mileage-bike" onclick="goToUrl('/tvs-bikes/xl100');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="TVS XL100"/>, <img alt="Yamaha Fascino 125 Fi Hybrid" class="sl-img clr" data-gsll-src="https://media.zigcdn.com/media/model/2024/Apr/yamaha-fascino125-right-side-view_270x180.jpg" data-track-label="best-mileage-bike" onclick="goToUrl('/yamaha-bikes/fascino');" src="https://images.zigcdn.com/images/spacer.png" style="opacity: 1;" title="Yamaha Fascino 125 Fi Hybrid"/>
'''
jpg_links = re.findall(r'https://[^\s"]+\.jpg', html_data)

# Print the .jpg links
for link_1 in jpg_links:
    print(link_1)
prices1=soup.find_all('div',id="zw-cmnSilder")
price1=[]
for i in prices1[1:20]:
    d=i.get_text()
    price1.append(d)
#print(price1)
text='''['\n\n\n\n\nZelio Legender\t\n\nRs. 65,000 \n\n\n\n\nWarivo Motors Nova\t\n\nRs. 55,999 \n\n\n\n\nWarivo Motors Edge\t\n\nRs. 44,999 \n\n\n\n\nWarivo Motors Neo\t\n\nRs. 39,999 \n\n\n\n\nHonda X-ADV\t\n\nRs. 11.90 Lakh \n\n\n\nLatest Scooters\n\n', '\n\n\n\n\nSuzuki e Access\t\n\nRs. 1.10 Lakh \n\n\n\n\nVida VX2\t\n\nRs. 70,000 \n\n\n\n\nVida Z\t\n\nRs. 1.00 Lakh \n\n\n\n\nKinetic Watts And Volts DX Electric\t\n\nRs. 1.10 Lakh \n\n\n\n\nSuzuki Burgman Electric\t\n\nRs. 1.20 Lakh \n\n\n\nUpcoming Bikes\n\n', '\n\n\n\n\nCompare Bikes\n\n\n\n\n\nBike Dealers\n\n\n\n\n\nOffers & Discounts\n\n\n\n\n\nService Centers\n\n\n\n\n\nEMI Calculator\n\n\n\n\n\nBike Recommender\n\n\n\n', '\n\n\n\n\nBajaj Chetak\t\n\nRs. 99,990 \n 123 km\n\n\n\n\nYulu Wynn\t\n\nRs. 55,555 \n 68 km\n\n\n\n\nTVS iQube\t\n\nRs. 94,434 \n 94 km\n\n\n\n\nHonda Activa e\t\n\nRs. 1.17 Lakh \n 102 km\n\n\n\n\nOla S1 Pro\t\n\nRs. 1.16 Lakh \n 242 km\n\n\n\nElectric Scooters\n\n', '\n\n\n\n\nYamaha RayZR 125 Fi Hybrid\t\n\nRs. 86,340 \n 71 kmpl\n\n\n\n\nTVS XL100\t\n\nRs. 46,954 \n 65 kmpl\n\n\n\n\nYamaha Fascino 125 Fi Hybrid\t\n\nRs. 81,180 \n 68 kmpl\n\n\n\nMileage Scooters\n\n', '\n\n\n\n\n\n\n\n\n\n\nSuzuki eAccess Electric Scooter First Ride Review - Has Suzuki Done Enough?\t\n30 May, 2025\n 3185 views\n10:5\n\n\n\n\n\n\n\n\n\nThe Numeros Diplos Max | A Scooter For Everyone | ZigWheels.com\t\n21 Mar, 2025\n 5693 views\n4:00\n\n\n\n\n\n\n\n\n\nHero Xoom 125 First Ride Review | Does It Perform As Good It Looks? | ZigWheels\t\n13 Mar, 2025\n 7166 views\n5:47\n\n\n\n\n\n\n\n\n\n2024 TVS Jupiter First Ride Review | A Modernized Upgrade | ZigWheels\t\n24 Aug, 2024\n 649778 views\n5:20\n\n\n\n\n\n\n\n\n\nBGauss RUV 350 First Ride Review | Too Expensive! | ZigWheels\t\n25 Jun, 2024\n 4412 views\n4:37\n\n\n\n\n\n\n\n\n\nAther Rizta Z First Ride Review - Is It A True Family Electric Scooter | ZigWheels.com\t\n24 May, 2024\n 9173 views\n7:22\n\n\n\n'] required only Rs price data
'''
price_pattern = r'Rs\. ?[\d.,]+(?: Lakh)?'
prices1 = re.findall(price_pattern, text)

# Print the extracted price list
for price1 in prices:
    print(price1)

links1=soup.find_all('a',class_="b clr c-p txt-ulne")
link1=[]
for i in links1[1:20]:
    d="https://www.zigwheels.com"+i['href']
    link1.append(d)
#print(link1)

sc_list=zip(cleaned_data,
            link_1,
            price1,
            link1
            )


# def scooters(request):
#     return render(request,"scooter.html",{'sc_list':sc_list})




#watches data
url2="https://www.flipkart.com/search?q=watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3DTitan"
response=requests.get(url2)
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names2=soup.find_all('div',class_="syl9yP")
# print(names)
name2=[]
# for i in n_names[0:20]:
#     d=i.get_text()
#     name.append(d)

html1 = '''<div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>, <div class="syl9yP">Titan</div>'''

soup1 = BeautifulSoup(html1, 'html.parser')
for div in soup1.find_all('div', class_='syl9yP'):
    d=div.text
    name2.append(d)
#print(name2)
n_name=[]
for i in name[0:20]:
    n_name.append(i)
print(n_name)
prices2=soup.find_all('div',class_="Nx9bqj")
price2=[]
for i in prices2[0:20]:
    d=i.get_text()
    price2.append(d)
#print(price2)
links2=soup.find_all('a',class_="WKTcLC")
#print(links2)
link2=[]
for i in links2[0:20]:
    d="https://www.flipkart.com"+i['href']
    link2.append(d)
#print(link2)
# if not os.path.exists('downloaded_images'):
#     os.makedirs('downloaded_images')
images2=soup.find_all('img',class_="_53J4C-")
#print(images2)
image2=[]
for i in images2[0:20]:
    d=i['src']
    image2.append(d)
#print(image2)

wa_list=zip(n_name,
            price2,
            link2,
            image2
            )
print(list(mb_list))
print(list(wa_list))
print(list(sc_list))

# def watches(request):
#     return render(request,"watch.html",{'wa_list':wa_list})

