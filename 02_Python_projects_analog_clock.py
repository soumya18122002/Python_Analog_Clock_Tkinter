import tkinter as ui
import time
import math
window = ui.Tk()
window.geometry("750x750")


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))
    # updating seconds hand per second
    second_x = second_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    second_y = -1 * second_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(second_hand, center_x, center_y, second_x, second_y)
    window.after(1000, update_clock)
    
    # updating minutes hand per minute
    minute_x = minute_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minute_y = -1 * minute_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minute_hand, center_x, center_y, minute_x, minute_y)

    # updating hours hand per hour
    hour_x = hour_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hour_y = -1 * hour_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hour_hand, center_x, center_y, hour_x, hour_y)

    

canvas = ui.Canvas(window, width=750, height=750, bg="black")
canvas.pack(expand=True, fill="both")
# create background
bg = ui.PhotoImage(file="roman_clk.png")
canvas.create_image(375, 375, image=bg)

# create clock hands
center_x = 375
center_y = 375
second_hand_len = 180 #240 for normal.png
minute_hand_len = 160#220 for normal.png
hour_hand_len = 120 # 170 for normal.png

# create clock hands
# second hand
second_hand = canvas.create_line(
    375, 375, 375+second_hand_len, 375+second_hand_len,
    width=2, fill="red")
# minute hand
minute_hand = canvas.create_line(
    375, 375, 375+minute_hand_len, 375+minute_hand_len,
    width=6, fill="gold")
# hour hand
hour_hand = canvas.create_line(
    375, 375, 375+hour_hand_len, 375+hour_hand_len,
    width=10, fill="white")


update_clock()
ui.mainloop()
