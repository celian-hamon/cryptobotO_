from PIL import Image
from os import remove

def get_img_lead(c1,c2,c3,c4,c5):
    try:
        remove("images/merged.png")
    except :
        pass
    c1= str("images/color/"+c1+".png")
    c2 = str("images/color/"+c2+".png")
    img_crypto1 = Image.open(c1)
    img_crypto2 = Image.open(c2)
    img_crypto1_size = img_crypto1.size
    img_crypto2_size = img_crypto2.size
    new_image = Image.new('RGB',(2*img_crypto2_size[0], img_crypto1_size[1]), (250,250,250))
    new_image.paste(img_crypto1,(0,0))
    new_image.paste(img_crypto2,(img_crypto1_size[0],0))
    new_image.save("images/merged.png","png")
    return 

