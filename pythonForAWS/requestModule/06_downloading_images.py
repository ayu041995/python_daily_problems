import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://www.google.com/search?sca_esv=72677fa7495fb346&sxsrf=AE3TifMR_vJqQ3YYMqUOXbrS1qhfpC9pSA:1754172004250&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeioyp3OhN11EY0n5qfq-zEMZldv_eRjZ2XLYc5GnVnMEIxC4WQfoNDH7FwchyAayyj__Ya02jV4FKxd8cIXUGY8AXi8rO7XHG70hwU2BX5CNsJq3rlLBxofvlIB_gImjTxxVP5Vzo6EgIFfUKsYlU345gMkHcA1YHE_ULJj_uRx1mtqvBg&q=images&sa=X&ved=2ahUKEwi3ysD5j-2OAxXTfWwGHRC0GzcQtKgLegQIExAB&biw=1869&bih=1058&dpr=2.2#vhid=kt9a95Fkz4GXzM&vssid=mosaic")

i = Image.open(BytesIO(r.content))

fp = open("image.jpg", "wb")

i.save(fp)

fp.close()