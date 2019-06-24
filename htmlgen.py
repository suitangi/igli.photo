# -*- coding: utf-8 -*-
"""
to generate the html codes


img list



https://imgur.com/a/npgOh4n
https://imgur.com/a/InDfXB5


"""
import random

imglist = [("https://i.imgur.com/PlADHjn.jpg", "Travel Animals"), ("https://i.imgur.com/35nyo2r.jpg", "Travel Landscape"), ("https://i.imgur.com/Dvtkcwj.jpg", "Travel Architecture"), ("https://i.imgur.com/8CvJkJp.jpg", "City"), ("https://i.imgur.com/0GgMB3x.jpg", "Architecture Travel"), ("https://i.imgur.com/yYw9pNs.jpg", "People Travel"), ("https://i.imgur.com/4tBMZ3s.jpg", "Animals"), ("https://i.imgur.com/HCI7i9o.jpg", "Animals"), ("https://i.imgur.com/W0WDF0t.jpg", "Nature Landscape"), ("https://i.imgur.com/oDSU4Xe.jpg", "Nature B&W"), ("https://i.imgur.com/BDTCipi.jpg", "Nature")]
imglist.extend([("https://i.imgur.com/J8eDuOQ.jpg", "People"), ("https://i.imgur.com/oUIfRs7.jpg", "Travel"), ("https://i.imgur.com/1NiwAuw.jpg", "B&W"), ("https://i.imgur.com/iHkkrK4.jpg", "People Travel"), ("https://i.imgur.com/AxuJDar.jpg", "Travel"), ("https://i.imgur.com/uQcGxYj.jpg", "Nature Landscape"), ("https://i.imgur.com/lybV3fN.jpg", "People"), ("https://i.imgur.com/0fAaqSt.jpg", "Nature"), ("https://i.imgur.com/wN8DPMj.jpg", "Architecture"), ("https://i.imgur.com/qVI0tvZ.jpg", "People"), ("https://i.imgur.com/cuImmKD.jpg", "Nature"), ("https://i.imgur.com/rPbv5jc.jpg", "B&W"), ("https://i.imgur.com/Q5uZSc5.jpg", "People"), ("https://i.imgur.com/UOk2fJi.jpg", "People"), ("https://i.imgur.com/4uyx5Oj.jpg", "People"), ("https://i.imgur.com/6JnzuTl.jpg", "Panorama City"), ("https://i.imgur.com/yUoXny1.jpg", "Animals"), ("https://i.imgur.com/CWUUhVn.jpg", "People Performance"), ("https://i.imgur.com/XTpaVwQ.jpg", "People Performance"), ("https://i.imgur.com/zBIy5xB.jpg", "People Performance"), ("https://i.imgur.com/rQAOayj.jpg", "Performance People"), ("https://i.imgur.com/nV6a9s8.jpg", "People B&W"), ("https://i.imgur.com/NhrWJsj.jpg", "Performance"), ("https://i.imgur.com/19wP3uE.jpg", "Architecture Travel"), ("https://i.imgur.com/C3J2G6W.jpg", "Animals"), ("https://i.imgur.com/4a4VbS8.jpg", "Travel People"), ("https://i.imgur.com/TlPdO9J.jpg", "Architecture Travel"), ("https://i.imgur.com/cAJFtSa.jpg", "Architecture Travel"), ("https://i.imgur.com/516gzxR.jpg", "Travel People Performance"), ("https://i.imgur.com/M9fDUmT.jpg", "City Travel"), ("https://i.imgur.com/LB1gFyV.jpg", "Travel"), ("https://i.imgur.com/t31m5ys.jpg", "City B&W"), ("https://i.imgur.com/p4UNlrW.jpg", "Travel"), ("https://i.imgur.com/nrR9e6W.jpg", "Food"), ("https://i.imgur.com/imuKMvs.jpg", "Food"), ("https://i.imgur.com/66WvbYQ.jpg", "Panorama City"), ("https://i.imgur.com/XEjOVe5.jpg", "Panorama City Travel")])


random.shuffle(imglist)

cut = int(len(imglist)/4)
cols = ["\n<div class=\"column\">", "\n</div>\n<div class=\"column\">", "\n</div>\n<div class=\"column\">", "\n</div>\n<div class=\"column\">"]

imglist1 = []
deslist = []
str1 = "<div class= \"row\">"
for i, img in enumerate(imglist):
    cols[i%4] += "\n<img src=\"" + img[0] + "\" onclick=\"openModal();currentSlide(" + str(i + 1) + ")\" class=\"hover-shadow " + img[1] + "\" data-aos=\"fade-up\">"
    imglist1.append(img[0])
    deslist.extend(img[1].split(" "))
str1 += "".join(cols)
str1 += "\n</div></div>"

print(str1)

str2 = "<div class=\"mySlides\">\n<img src=\"" + "\" class=\"modal-image\">\n</div>\n<div class=\"mySlides\">\n<img src=\"".join(imglist1) + "\" class=\"modal-image\">\n</div>"

print("\n" + str2)

deslist = set(deslist)
str3 = "<div id=\"myBtnContainer\">\n<button class=\"btn active\" onclick=\"filterSelection('all')\"> All</button>"
for i in deslist:
    str3 += "\n<button class=\"btn\" onclick=\"filterSelection('" + i + "')\">" + i + "</button>"
str3 += "</div>"

print("\n" + str3)
    

