# -*- coding: utf-8 -*-
"""
to generate the html codes


img list



https://imgur.com/a/pBppXzY
https://imgur.com/a/InDfXB5


"""
import random

imglist = [("https://i.imgur.com/0GgMB3xg.jpg", "Architecture Travel"), ("https://i.imgur.com/yYw9pNsg.jpg", "People Travel"), ("https://i.imgur.com/4tBMZ3sg.jpg", "Animals"), ("https://i.imgur.com/HCI7i9og.jpg", "Animals"), ("https://i.imgur.com/W0WDF0tg.jpg", "Nature Landscape"), ("https://i.imgur.com/8CvJkJpg.jpg", "City"), ("https://i.imgur.com/35nyo2rg.jpg", "Travel Landscape"), ("https://i.imgur.com/Dvtkcwjg.jpg", "Travel Architecture"), ("https://i.imgur.com/PlADHjng.jpg", "Travel Animals"), ("https://i.imgur.com/oDSU4Xeg.jpg", "Nature B&W"), ("https://i.imgur.com/BDTCipig.jpg", "Nature")]
imglist.extend([("https://i.imgur.com/cAJFtSag.jpg", "Architecture Travel"), ("https://i.imgur.com/516gzxRg.jpg", "Travel People Performance"), ("https://i.imgur.com/M9fDUmTg.jpg", "City Travel"), ("https://i.imgur.com/LB1gFyVg.jpg", "Travel"), ("https://i.imgur.com/t31m5ysg.jpg", "City B&W"), ("https://i.imgur.com/C3J2G6Wg.jpg", "Animals"), ("https://i.imgur.com/4a4VbS8g.jpg", "Travel People"), ("https://i.imgur.com/TlPdO9Jg.jpg", "Architecture Travel"), ("https://i.imgur.com/nV6a9s8g.jpg", "People B&W"), ("https://i.imgur.com/NhrWJsjg.jpg", "Performance"), ("https://i.imgur.com/19wP3uEg.jpg", "Architecture Travel"), ("https://i.imgur.com/XTpaVwQg.jpg", "People Performance"), ("https://i.imgur.com/zBIy5xBg.jpg", "People Performance"), ("https://i.imgur.com/rQAOayjg.jpg", "Performance People"), ("https://i.imgur.com/UOk2fJig.jpg", "People"), ("https://i.imgur.com/4uyx5Ojg.jpg", "People"), ("https://i.imgur.com/6JnzuTlg.jpg", "Panorama City"), ("https://i.imgur.com/yUoXny1g.jpg", "Animals"), ("https://i.imgur.com/CWUUhVng.jpg", "People Performance"), ("https://i.imgur.com/cuImmKDg.jpg", "Nature"), ("https://i.imgur.com/rPbv5jcg.jpg", "B&W"), ("https://i.imgur.com/Q5uZSc5g.jpg", "People"), ("https://i.imgur.com/iHkkrK4g.jpg", "People Travel"), ("https://i.imgur.com/AxuJDarg.jpg", "Travel"), ("https://i.imgur.com/qVI0tvZg.jpg", "People"), ("https://i.imgur.com/uQcGxYjg.jpg", "Nature Landscape"), ("https://i.imgur.com/J8eDuOQg.jpg", "People"), ("https://i.imgur.com/oUIfRs7g.jpg", "Travel"), ("https://i.imgur.com/1NiwAuwg.jpg", ""), ("https://i.imgur.com/wN8DPMjg.jpg", "Architecture"), ("https://i.imgur.com/lybV3fNg.jpg", "People"), ("https://i.imgur.com/0fAaqStg.jpg", "Nature"), ("https://i.imgur.com/p4UNlrWg.jpg", "Travel"), ("https://i.imgur.com/nrR9e6Wg.jpg", "Food"), ("https://i.imgur.com/imuKMvsg.jpg", "Food"), ("https://i.imgur.com/66WvbYQg.jpg", "Panorama City"), ("https://i.imgur.com/XEjOVe5g.jpg", "Panorama City Travel")])


random.shuffle(imglist)

cut = int(len(imglist)/4)
cols = ["\n<div class=\"column\">", "\n</div>\n<div class=\"column\">", "\n</div>\n<div class=\"column\">", "\n</div>\n<div class=\"column\">"]


str1 = "<div class= \"row\">"
for i, img in enumerate(imglist):
    cols[i%4] += "\n<img src=\"" + img + "\" onclick=\"openModal();currentSlide(" + str(i + 1) + ")\" class=\"hover-shadow\" data-aos=\"fade-up\">"
str1 += "".join(cols)
str1 += "\n</div></div>"

print(str1)

str2 = "<div class=\"mySlides\">\n<img src=\"" + "\" style=\"width:100%\" class=\"modal-image\">\n</div>\n<div class=\"mySlides\">\n<img src=\"".join(imglist) + "\" style=\"width:100%\" class=\"modal-image\">\n</div>"

print(str2)
