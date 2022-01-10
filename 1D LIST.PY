from tkinter import *
import random 

root=Tk()
root.tittle("Luck friend Wheel")
root.geometry("500x500")

enter_name = Entry(root)
enter_name.place(relx= 0.5,rely = 0.2, anchor =CENTER)

friend_list = Label(root)
random_number_label = label(root)
lucky_friend = label(root)

list1 = []
def addfriend():
    friend_name = enter_name.get()
    list1.append(friend_name)
    friend_list["text"] = "Your friendlist : " + str(list1)

def random_number():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1(random_no)
    lucky_friend["text"] = "your Lucky friend is: "+ str(generated_random_number)