# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:20:24 2022

@author: VIHAAN KATHURIA
"""

import random
from tkinter import *

import random
root = Tk()
root.title("Lucky friend Wheel")
root.geometry("400x400") 



input_friend = Entry(root)
input_friend.pack()

friend_list = Label(root)

random_number_label=Label(root)
lucky_friend = Label(root)
list1 = []

def start():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"]=str(random_no)
    friend=list1[random_no]
    lucky_friend["text"] = "Your lucky friend is " + str(friend)
    print(friend)
    
def addfriend():
    friend_name = input_friend.get()
    list1.append(friend_name)
    friend_list["text"] = "Your friend is " + str(list1)

btn1 = Button(root, text = "Who is your lucky friend?", command=start)
btn2 = Button(root, text = "Add to the friend list", command=addfriend)

friend_list.pack()
btn2.pack()
random_number_label.pack()
btn1.pack()
lucky_friend.pack()

root.mainloop() 

