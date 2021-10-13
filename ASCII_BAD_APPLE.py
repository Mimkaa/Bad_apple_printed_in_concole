from PIL import Image
from time import sleep
import os
from pathlib import Path
import pygame

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

time_sleep = 0.0294117 # for ordinary using
# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return (characters)

def main(new_width=100):
    if input("Write the file or play file?\n\n>>> ").lower() == "write":
        frames = []
        for framenum in range(6568):
            try:
                image=Image.open(f'frames\Bad_apple{framenum}.jpg')
            except:
                print("It isn`t a valid pathname to an image.")
                return
            # convert image to ascii
            new_image_data = pixels_to_ascii(grayify(resize_image(image)))

            # format
            pixel_count = len(new_image_data)
            frame = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

            # put the frames into the list
            frames.append(frame)
            print(f"The frame bad_apple{framenum}.jpg processed successfully.")
            # save result to file
        with open("memory.txt", "w") as f:
            for frame in frames:
                print("Frame writed!")
                f.write(str(frame) + ">")
    else:

        # read the frames from the memory file
        with open("memory.txt", "r") as f:
            memory = f.read()
        frames=memory.split(">")

        # music
        pygame.mixer.init()
        pygame.mixer.music.load("Bad Apple [JubyPhonic].ogg")
        pygame.mixer.music.play()

        # printing the frames
        for frame in frames:
            print(frame)
            sleep(time_sleep)
        if input("Exit-Yes?,repeat-anything else:").lower() == "yes":
            raise SystemExit(0)
        else:
            # music
            pygame.mixer.init()
            pygame.mixer.music.load("Bad Apple [JubyPhonic].ogg")
            pygame.mixer.music.play()

            # printing the frames
            for frame in frames:
                print(frame)
                sleep(time_sleep)
# run program
main()
