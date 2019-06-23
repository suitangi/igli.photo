# -*- coding: utf-8 -*-
"""
to generate the html codes


img list



https://imgur.com/a/pBppXzY
https://imgur.com/a/BjzGDmF
https://imgur.com/a/InDfXB5


"""
import random

imglist = ["https://i.imgur.com/PlADHjnr.jpg", "https://i.imgur.com/35nyo2rr.jpg", "https://i.imgur.com/Dvtkcwjr.jpg", "https://i.imgur.com/8CvJkJpr.jpg", "https://i.imgur.com/0GgMB3xr.jpg", "https://i.imgur.com/yYw9pNsr.jpg", "https://i.imgur.com/4tBMZ3sr.jpg", "https://i.imgur.com/kUxiHHNr.jpg", "https://i.imgur.com/Yslxp8fr.jpg", "https://i.imgur.com/v9v5CC5r.jpg", "https://i.imgur.com/03jSlOTr.jpg", "https://i.imgur.com/Bsc7ZhQr.jpg", "https://i.imgur.com/xJVC8FBr.jpg"]
imglist.extend(["https://i.imgur.com/wN8DPMjr.jpg", "https://i.imgur.com/lybV3fNr.jpg", "https://i.imgur.com/0fAaqStr.jpg", "https://i.imgur.com/uQcGxYjr.jpg", "https://i.imgur.com/J8eDuOQr.jpg", "https://i.imgur.com/oUIfRs7r.jpg", "https://i.imgur.com/1NiwAuwr.jpg", "https://i.imgur.com/iHkkrK4r.jpg", "https://i.imgur.com/AxuJDarr.jpg", "https://i.imgur.com/qVI0tvZr.jpg", "https://i.imgur.com/cuImmKDr.jpg", "https://i.imgur.com/rPbv5jcr.jpg", "https://i.imgur.com/Q5uZSc5r.jpg", "https://i.imgur.com/UOk2fJir.jpg", "https://i.imgur.com/4uyx5Ojr.jpg", "https://i.imgur.com/6JnzuTlr.jpg", "https://i.imgur.com/yUoXny1r.jpg", "https://i.imgur.com/CWUUhVnr.jpg", "https://i.imgur.com/XTpaVwQr.jpg", "https://i.imgur.com/zBIy5xBr.jpg", "https://i.imgur.com/rQAOayjr.jpg", "https://i.imgur.com/nV6a9s8r.jpg", "https://i.imgur.com/NhrWJsjr.jpg", "https://i.imgur.com/19wP3uEr.jpg", "https://i.imgur.com/C3J2G6Wr.jpg", "https://i.imgur.com/4a4VbS8r.jpg", "https://i.imgur.com/TlPdO9Jr.jpg", "https://i.imgur.com/cAJFtSar.jpg", "https://i.imgur.com/516gzxRr.jpg", "https://i.imgur.com/M9fDUmTr.jpg", "https://i.imgur.com/LB1gFyVr.jpg", "https://i.imgur.com/t31m5ysr.jpg", "https://i.imgur.com/p4UNlrWr.jpg", "https://i.imgur.com/nrR9e6Wr.jpg", "https://i.imgur.com/imuKMvsr.jpg"])


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