from PIL import Image


myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []



### Functions

def darkBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    red = 0
    green = 51
    blue = 76

  
    newPixelList.append(p)



def red(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]


   

    newPixelList.append(p)


def lightBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

   


    p = (red,green,blue)

    newPixelList.append(p)    

def yellow(pixel)



### RUNNING CODE

newPixelList = []




for pixel in pixelList:

    intensity = pixel[0] + pixel[1] + pixel[2]



#pixel manipulation

    if intensity < 182:
        darkBlue(pixel)
    

#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()


    




    



