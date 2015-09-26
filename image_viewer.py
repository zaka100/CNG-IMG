'''
Notes:
-Requires Pygame
-Pressing the 'X' button does not close the program, it just closes the window, to close it, kill it using the python shell

Created by zaka100

'''


import pygame # Imports pygame, the graphics module
import bz2 # Imports bz2, compression algorithm
from pygame import gfxdraw # Imports pixel drawing method from pygame
import sys # Imports sys, for sys.exit()


inputfile = "wallpaper.cng" # Gets the wallpaper, change it to which cng file you want the program to view

list2 = ['!','"','#','$','%','&',"'",'(',')','*','+','0','1','2','3','4','5','6','7','8','9',':',';','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','~','?','/','{','}',']','|','─','│','┐','┘','├','┤','┬','┴','┼','═','║','╒','╓','╔','╕','╖','╗','╘','╙','╚','╛','╜','╝','╞','╟','╠','╡','╢','╣','╤','╥','╦','╧','╨','╩','╪','╫','╬','ª','À','Ø','Ë','ą','ü','ù','Ğ','ģ','ĵ','İ','Ķ','Ō','ŉ','ń','Ł','Ɗ','Ɔ','Ƈ','ƃ','Ƃ','Ɓ','Ǆ','ǅ','ǆ','Ǉ','ǈ','ǉ','ǳ','Ǭ','ǧ','ǣ','Ǥ','Ƶ','ƶ','Ʒ','Ƹ','ƹ','ƺ','Ʀ','ɣ','ʋ','ɷ','ɶ','ɢ','ʊ','ʉ','ɵ','ɴ','ʈ','ʛ','ɠ','ʚ','ʙ','ɱ','ɝ','ɜ','ɛ','ɚ','ə','ɸ','ɤ','ʠ','ʡ','ʢ','ʣ','ʤ','ʥ','ʦ','ʧ','ʨ','Ḁ','ḁ','Ḃ','ḃ','Ḅ','ḅ','Ḇ','ḇ','Ḉ','ḉ','Ḋ','ḋ','Ḍ','ḍ','Ḏ','ḏ','Ḑ','Ḓ','ḓ','Ḕ','ḕ','Ḗ','ḗ','Ḙ','ḙ','Ḛ','ḛ','Ḝ','ḝ','Ḟ','ḟ','Ḡ','ḡ','Ḣ','ḣ','Ḥ','ḥ','Ḧ','ḧ','Ḩ','ḩ','Ḫ','ḫ','Ḭ','ḭ','Ḯ','ḯ','Ḱ','ḱ','Ḳ','ḳ','Ḵ','ḵ','Ḷ','ḷ','Ḹ','ḹ','Ḻ','ḻ','Ḽ','ḽ','Ḿ']
# ^ Defines what each character is, this goes from 0 to 255 - used for rgb

listalpha = ['0','1','2','3','4','5','6','7','8','9','F']
# ^ Checks alpha, not functional in this version


dec = open(inputfile,'rb') # Opens the CNG file
rtxt = dec.read() # Reads the CNG file
decompress = bz2.decompress(rtxt) # Decompresses the CNG file
lines = decompress.split(b'\n') # Splits the decompressed text into lines


print(lines[0]) # Prints the first line - Contains the resolution
res=lines[0].split(b'x')
width=int(res[0])
height=int(res[1])
screen_size = (width,height) # Gets the image height and width

screen = pygame.display.set_mode(screen_size) # Creates window with height and width of image
screen.fill(pygame.Color(255,255,255)) # Fills the screen with black
pygame.display.set_caption('Image Viewer') # Sets the title

pygame.display.init() # Initializes the window



numloop = 0
num=0
for i in lines: # For every line in the decompressed text
    if num == 0: # Skip the first line as it is not needed
        pass
    else:
        numy=0
        line = bytes.decode(i) # Decode the line
        n = 3
        splitinto3 = [line[i:i+n] for i in range(0, len(line), n)] # Split the line into groups of threes (ie: r, g, b)
        for x1 in splitinto3: # For every group of three
            
            numred = list2.index(x1[0]) # Get red value of character
            numgreen = list2.index(x1[1]) # Get green value of character
            numblue = list2.index(x1[2]) # Get blue value of character
            
            pixels = pygame.surfarray.pixels3d(screen) # Display pixel
            pixels[numy][num-1] = (numred,numgreen,numblue) # Change pixel settings (ie: coordinates, rgb value)
                            
            numy+=1
    num+=1

pygame.display.update() # Update screen to display image


while True:
    try:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: # If someone clicks the close button
            pygame.quit() # Close the
            sys.exit()    #  program
    except:
        pass

