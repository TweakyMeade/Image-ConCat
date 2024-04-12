from PIL import Image


def imageConCat(front, back):
    fImage = Image.open(front).convert("RGBA")
    bImage = Image.open(back).resize(fImage.size).convert("RGBA")
    
    alphaPixel = []

    for p in fImage.getdata():
        if p[0] == 255 and p[1] == 255 and p[2] == 255:
             alphaPixel.append((255, 255, 255, 0))
        else:
            alphaPixel.append(p)

    fImage.putdata(alphaPixel)
    conCat = Image.alpha_composite(bImage, fImage)
    conCat.show()

imageConCat("a.jpeg", "b.jpeg")

