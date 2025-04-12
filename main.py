# import
from tkinter import *
from PIL import ImageTk, Image


# global variable
coin = 0
plant_stage = 1


# main window
win = Tk()
win.title("PlantClicker!")
win.geometry("600x700")
win.resizable(width=False, height=False)
win['background'] = "white"

# images list
stage_images = {
    1: ImageTk.PhotoImage(Image.open("img/plant_stage1.png")),
    2: ImageTk.PhotoImage(Image.open("img/plant_stage2.png")),
    3: ImageTk.PhotoImage(Image.open("img/plant_stage3.png")),
}

# click function
def on_click(event):
    global coin
    coin += 1
    print(f"coin: {coin}")

# watering function
def get_coins():
    global coin, plant_stage
    if coin >= 10:
        if plant_stage < 3:
            coin -= 10
            plant_stage += 1
            label.config(image=stage_images[plant_stage])
            label.image = stage_images[plant_stage]
            print(f"The plant has grown to the stage {plant_stage}!")
        else:
            print("The plant is now fully grown!")
    else:
        print("Not enough coins")

# Creating a frame
frame = Frame(win, bg="white")
frame.place(x=70, y=100)

# Create an image tag
label = Label(frame, image=stage_images[plant_stage], bg="white")
label.pack()

label.bind("<Button-1>", on_click)

# Water button
button = Button(win, text="Water!💦", command=get_coins)
button.place(x=260, y=650)

win.mainloop()