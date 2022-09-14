from PIL import Image

def main():
    '''
    jpeg = Joint Photographic Experts Group
    png = Portable Network Graphics


    Because of their different compression processes, 
    JPEGs contain less data than PNGs — and therefore, 
    are usually smaller in size. Unlike JPEGs, PNGs support transparent backgrounds, 
    making them preferred for graphic design.

    '''
    img = Image.open("village.jpeg")
    img.save('village.png')

    img2 = Image.open('angrybird.png')
    img.save('angrybird.jpg')


if __name__ == "__main__":
    main()
