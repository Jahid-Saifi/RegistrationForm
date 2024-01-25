from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.title("Registration From")
screen.geometry("400x400")
screen.resizable(False,False)

def register():
    name=name_info.get()
    age=age_info.get()
    phone=phone_info.get()
    email=email_info.get()
    
    if name=="":
        messagebox.showerror("Error","plaese enter ypur name")
    elif age=="":
        messagebox.showerror("Error","please enter your age")
    elif phone=="":
        messagebox.showerror("Error","please enter your phone")
         
    elif email=="":
        messagebox.showerror("Error","please enter your email")
        
    else:
        Label(screen,text="Registration Sucessfull",font="20",fg="green").place(x=135, y=285) 
         
        with open(name+"txt","w")as f:
          f.write("name:"+name+"\n")
          f.write("age:"+age+"\n")
          f.write("phone:"+phone+"\n")
          f.write("email:"+email+"\n")
          
          
    
    
def clear():
    name_entery.delete(0,END)
    age_entery.delete(0,END)
    phone_entery.delete(0,END)
    email_entery.delete(0,END)
       
    


#label
Label(screen,text="Registration Form" ,font="ariel 20 bold", bg="red",fg="white").pack(fill="both")

Label(screen,text="Name",font="20").place(x=40,y=75)
Label(screen,text="Age",font="20").place(x=40,y=115)
Label(screen,text="Phone No",font="20").place(x=40,y=155)
Label(screen,text="Email Id",font="20").place(x=40,y=195)

#Entry
name_info=StringVar()
age_info=StringVar()
phone_info=StringVar()
email_info=StringVar()



name_entery=Entry(screen, font="10",bd=4, textvariable=name_info)
name_entery.place(x=140,y=75)
age_entery=Entry(screen, font="10",bd=4, textvariable=age_info)
age_entery.place(x=140,y=115)
phone_entery=Entry(screen, font="10",bd=4, textvariable=phone_info)
phone_entery.place(x=140,y=155)
email_entery=Entry(screen, font="10",bd=4, textvariable=email_info)
email_entery.place(x=140,y=195)

#button

Button(screen,text="Register",font="20", command=register).place(x=185,y=255)
Button(screen,text="clear",font="20",command=clear).place(x=345, y=365)
Button(screen,text="clear",font="20",command=clear).place(x=345, y=365)




mainloop()