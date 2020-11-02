from tkinter import *
window=Tk()
window.title("FILE HANDLING EXERCISE")

window.geometry("700x500")
window.configure(background="cyan")



'''Functions'''
#Create function
def create_txt():
    file=open('/home/user/Desktop/my_weekend_activities.txt','w')


#Display
def disp():
    file=open('/home/user/Desktop/my_weekend_activities.txt','r')
    file1=file.read()
    text_it.insert(END, file1)
    file.close()






#Append function
def append():
    file=open('/home/user/Desktop/my_weekend_activities.txt','a')
    file.writelines(text_it.get("1.0","end-1c")+"\n")




#Clear function
def clear():
    text_it.delete("1.0","end-1c")

#Exit
def exit():
    window.destroy()

#Head label
lblname1=Label(window, text="My weekend Activities")
lblname1.grid(row=0, column=3)

#Entry
text_it=Text(window,height=5, width=40, )
text_it.configure()
text_it.grid(row=2,column=3)
#Buttons
b_create=Button(window, text="Create TEXT file",command=create_txt)
b_create.grid(row=7,column=2)

b_append=Button(window,text="Append Data",command=append)
b_append.grid(row=7,column=3)

b_read=Button(window,text="Display",command=disp)
b_read.grid(row=7,column=4)

clear_button=Button(window,text="Clear",command=clear)
clear_button.grid(row=7, column=5)

exit_b=Button(window,text="Exit", command=exit)
exit_b.grid(row=7,column=6)




window.mainloop()
