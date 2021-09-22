from tkinter import *
import os
import tkinter
tkinter.image_names
from django.utils.translation import ugettext_lazy as _
from PIL import ImageTk,Image


  
def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Başarılı")
  screen3.geometry("150x100")
  Label(screen3, text = "Giriş Başarılı").pack()
  Button(screen3, text = "Tamam", command =delete2).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Başarılı")
  screen4.geometry("150x100")
  Label(screen4, text = "Şifre Yanlış").pack()
  Button(screen4, text = "Tamam", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Başarılı")
  screen5.geometry("150x100")
  Label(screen5, text = "Kullanıcı Bulunamadı").pack()
  Button(screen5, text = "Tamam", command =delete4).pack()

  
def register_user():
 
  
  username_info = username.get()
  password_info = password.get()

 
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Kayıt Başarılı", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Kayıt Ol")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Lütfen Ayrıntıları Giriniz").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Kullanıcı Adı * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Şifre * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Kayıt", width = 10, height = 1, command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Giriş")
  screen2.geometry("300x250")
  Label(screen2, text = "Giriş yapmak için lütfen aşağıya ayrıntıları girin").pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Kullanıcı Adı * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Şifre * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Giriş", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("900x500")
  screen.title("Template")

  Label(text = "Template", bg = "red", width = "600", height = "2", font = ("Calibri", 19)).pack()
  Label(text = "").pack()
  Button(text = "Giriş", height = "4", width = "60", command = login).pack()
  Label(text = "").pack()
  Button(text = "Kayıt Ol",height = "4", width = "60", command = register).pack()

  screen.mainloop()
  
main_screen()
