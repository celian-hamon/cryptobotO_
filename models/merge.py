from PIL import Image
from os import remove

def get_img_lead(c1,c2,c3,c4,c5):
    try:
        remove("images/merged.png")
    except :
        pass
    c1 = str("images/color/"+c1+".png")
    c2 = str("images/color/"+c2+".png")
    c3 = str("images/color/"+c3+".png")
    c4 = str("images/color/"+c4+".png")
    c5 = str("images/color/"+c5+".png")
    img_crypto1 = Image.open(c1)
    img_crypto2 = Image.open(c2)
    img_crypto3 = Image.open(c3)
    img_crypto4 = Image.open(c4)
    img_crypto5 = Image.open(c5)
    img_crypto1_size = img_crypto1.size
    img_crypto2_size = img_crypto2.size
    new_image = Image.new('RGB',(5*img_crypto2_size[0], img_crypto1_size[1]), (250,250,250))
    new_image.paste(img_crypto1,(0,0))
    new_image.paste(img_crypto2,(128,0))
    new_image.paste(img_crypto3,(256,0))
    new_image.paste(img_crypto4,(384,0))
    new_image.paste(img_crypto5,(512,0))
    new_image.save("images/merged.png","png")
    return 

get_img_lead("doge","eth","btc",'html',"xrp")

