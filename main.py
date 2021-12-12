import cv2
import easygui
import numpy as np
import sys
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import *

import os

top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

def upload():
    image = easygui.fileopenbox()
    cartoonify(image)


def cartoonify(image):


    original_img = cv2.imread(image) #converted into an 3D numpy array
    print(original_img.shape)

    original_img_2 = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)  #an RGB color is stored in a structure or unsigned integer with Blue occupying the least significant “area”
    # print(original_img_2.shape)
    # ReSized1 = cv2.resize(original_img_2, (800, 1000))
    # plt.imshow(original_img_2)
    # plt.show(block=True)
    # plt.interactive(False)
    # if original_img_2 is None:
    #     print("Couldn't find Image")
    #     sys.exit()


    #convert the image into grayscale
    grayscaleimage = cv2.cvtColor(original_img_2, cv2.COLOR_BGR2GRAY)
    print(grayscaleimage.shape)
    # ReSized2 = cv2.resize(grayscaleimage, (800, 1000))
    # plt.imshow(grayscaleimage)
    # plt.show(block=True)


    #Smoothening the grayscale images by applying median blur,
    # the center pixel is assigned a mean value of all the pixels which fall under the kernel. In turn, creating a blur effect.
    smoothgrayimage = cv2.medianBlur(grayscaleimage,3)
    # ReSized3 = cv2.resize(smoothgrayimage, (800, 1000))
    # print(smoothgrayimage.shape)
    # plt.imshow(smoothgrayimage)
    # plt.show(block=True)


    #Retriving the edges of the grayscale image

    getedge = cv2.adaptiveThreshold(smoothgrayimage, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 9)
    # ReSized4 = cv2.resize(getedge , (800, 1000))
    # print(ReSized4.shape)
    # plt.imshow(getedge)
    # plt.show(block=True)

    #prepring a mask from the original image to we can use over the edge, Bilaretal filter removes noise
    colorImage = cv2.bilateralFilter(original_img_2, 9, 500, 500)
    # ReSized5 = cv2.resize(colorImage, (800, 1000))
    # plt.imshow(colorImage)
    # plt.show(block=True)

    #final giving the catoon effect
    cartoonimage = cv2.bitwise_and(colorImage,colorImage,mask = getedge)
    # ReSized6 = cv2.resize(colorImage, (800, 1000))
    # plt.imshow(cartoonimage)
    # plt.show(block=True)

    images=[original_img_2, grayscaleimage, smoothgrayimage, getedge, colorImage, cartoonimage]
    fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    #save button code
    plt.show()
    # save(cartoonimage, image)
    save1 = Button(top, text="Save cartoon image", command=lambda: save(cartoonimage, image), padx=30, pady=5)
    save1.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    save1.pack(side=TOP, pady=50)

def save(cartoonimage, image):
    imagename = "cartoonified"
    path1 = os.path.dirname(image)
    extension = os.path.splitext(image)[1]
    path = os.path.join(path1,imagename+extension)
    print(path)
    cv2.imwrite(path,cv2.cvtColor(cartoonimage,cv2.COLOR_RGB2BGR))

    # I = "Image saved by name " + newName + " at " + path
    # tk.messagebox.showinfo(title=None, message=I)



upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)

top.mainloop()











