from PIL import Image  

print("\nThis program will insert a background image of your choice in a image of your choice!\n")

front_number = input("What image would you like to insert in the front?\n1- A Boat\n2- A Cactus\nEnter the option number: ")
while front_number < "1" or front_number > "2":
    front_number = input("\nWhat image would you like to insert in the front?\n1- A Boat\n2- A Cactus\nEnter the option number: ")

front_image = ""
if front_number == "1":
    front_image = "boat.jpg"
elif front_number == "2":
    front_image = "cactus.jpg"

image_front = Image.open(front_image)
width, height = image_front.size
pixels_front = image_front.load() 


back_number = input("\nWhat image would you like to insert in the background?\n1- A Beach\n2- A Desert\n3- The Earth\n4- A Forest\n5- A Sunset\nEnter the option number: ")
while back_number < "1" or back_number > "5":
    back_number = input("\nWhat image would you like to insert in the background?\n1- A Beach\n2- A Desert\n3- The Earth\n4- A Forest\n5- A Sunset\nEnter the option number: ")

back_image = ""
if back_number == "1":
    back_image = "beach.jpg"
elif back_number == "2":
    back_image = "desert.jpg"
elif back_number == "3":
    back_image = "earth.jpg"
elif back_number == "4":
    back_image = "forest.jpg"
elif back_number == "5":
    back_image = "sunset.jpg"


image_back = Image.open(back_image)
pixels_original = image_back.load()

if front_number == "1":
    for x in range(0, width):
        for y in range(0, height):
            (r, g, b) = pixels_original[x, y] 
            if (51, 102, 51) <= pixels_front[x, y]:
                pixels_front[x, y] = (r, g, b)
elif front_number == "2":
    for x in range(0, width):
        for y in range(0, height):
            (r, g, b) = pixels_original[x, y] 
            if (62, 62, 0) < pixels_front[x, y] and (200, 200, 200) > pixels_front[x, y]:
                pixels_front[x, y] = (r, g, b)
 
            
image_front.show() 

# Saving the new image
save = input("\ndo you want to save the new image?(yes/no) ")
if save.lower() == "yes":
    name = input("What do you want to name this image file? ")
    image_front.save(f'{name}.jpg')
    print("Image Sucessfully saved!\n")
else:
    print("\nSee You!\n")



