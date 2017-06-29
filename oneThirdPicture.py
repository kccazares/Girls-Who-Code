from PIL import Image


myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)



### Functions

def bW(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    avg = int((red + blue + green)/3)

    newRed = avg
    if newRed > 255:
        newRed = avg
    newGreen = avg
    if newGreen > 255:
        newGreen = avg
    newBlue = avg
    if newBlue > 255:
        newBlue = avg

    p = (newRed,newGreen,newBlue)

    newPixelList.append(p)



def doubleRed(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed = red*2
    if newRed > 255:
        newRed = 255


    p = (newRed,green,blue)

    newPixelList.append(p)


def doubleBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255


    p = (red,green,newBlue)

    newPixelList.append(p)    




### RUNNING CODE

newPixelList = []

length = len(pixelList)
oneThird = length//3

twoThird = (oneThird*2)

counter = 0

for pixel in pixelList:



#pixel manipulation

    if(counter < oneThird): #this is the top half of the photo
        doubleRed(pixel)

    elif(counter < twoThird): ##this is the middle of the photo
        bW(pixel)

        
    else: # this is the bottom half of the photo
        
        
        doubleBlue(pixel)

    counter = counter + 1

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()


    




    


