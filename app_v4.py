#date of release: 2021 01 15
#version 4

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageFont,ImageDraw
import PIL
from tkinter.filedialog import asksaveasfile
from variables import *

#main window format
main = tk.Tk()
main.iconbitmap(main,default='img/app_menu_icon.ico') 
main.title('Mil Symb 4')
main.geometry('600x600+250+250')
main.resizable(False,False)

#main menu
menubar=tk.Menu(main)
img_mnu=tk.Menu(menubar,tearoff=0)
about_mnu=tk.Menu(menubar,tearoff=0)
img_mnu.add_command(label='Clear Image',command=lambda:reset())
img_mnu.add_command(label='Save Image',command=lambda:save_img())
img_mnu.add_command(label='Exit',command=lambda:exit_app())
menubar.add_cascade(label='Image',menu=img_mnu)
about_mnu.add_command(label='About',command=lambda:about_app())
menubar.add_cascade(label='About',menu=about_mnu)
main.config(menu=menubar)

#text entry validation variables
amp_t_in=tk.StringVar() 
amp_m_in=tk.StringVar() 

#instantiate imagery imported list images to PhotoImage
for x in range(len(imagery_10)):
    imagery_10[x]=tk.PhotoImage(file=imagery_10[x])

#functions
def about_app():
    msgbx1=messagebox.showinfo(title='Mil Symb Program 4.0',
                             message='Military Unit Symbol Icon\n'
                             +'December 2020\n'
                             +'version: 4.0\n'
                             +'Creator: Instagram @ instazragcladiv')

def save_img():
    file=asksaveasfile(mode='w',defaultextension='.jpg',
                       filetypes=[('JPEG','.jpg')])
    if not file:
        return

    save_img=Image.open('img/icon_product.png') 
    s_f=save_img.load() 
    save_img.save(file)

def exit_app():
    msgbx2=messagebox.askquestion('Exit Application',
                                'Are you sure?',icon='warning')
    if msgbx2=='yes':
        main.destroy()
    else:
        return

def reset():
    cmb_01.current(0)
    cmb_02.current(0)
    cmb_03.current(0)
    cmb_04.current(0)
    ent_05.delete(0,'end')
    ent_06.delete(0,'end')
    
    clear_img()

def clear_img():
    out_img=Image.new('RGB',(275,250),(255,255,255))
    o_f=out_img.load()
   
    for y in range(250):
        for x in range(275):
            o_f[x,y]=(255,255,255)

    out_img.save('img/icon_product.png')
    imagery_10[1]=Image.open('img/icon_product.png')
    imagery_10[1]=tk.PhotoImage(file='img/icon_product.png')
    lbl_icon.config(image=(imagery_10[2]))

def set_img(a,b): 
    out_img=Image.open('img/icon_product.png') 
    o_f=out_img.load() 
    in_img=Image.open(b[a])
    i_f=in_img.load()

    for y in range(250):
        for x in range(275):
            if o_f[x,y]!=(0,0,0) and i_f[x,y]!=(255,255,255):
                o_f[x,y]=(0,0,0)
   
    out_img.save('img/icon_product.png')

def set_txt(a,b,c):
    font=ImageFont.truetype(font='arialbd.ttf',size=14)
    im=Image.open('img/icon_product.png')
    draw=ImageDraw.Draw(im)

    if b==80:
        w,h=draw.textsize(a)
        draw.text(((b-w),c),a,(0,0,0),font=font)
        del draw
    else:
        draw.text((b,c),a,(0,0,0),font=font)
        del draw
        
    im.save('img/icon_product.png')
    
def set_icon():
    clear_img()    

    v_01=(unit_val.index(cmb_01.get()))
    set_img(v_01,imagery_11)    
    #v_02=future use, needs dependency on other inputs
    #v_03=future use, needs dependency on other inputs    
    v_04=(bd_amp.index(cmb_04.get()))
    set_img(v_04,imagery_14)
    v_05=set_txt(amp_t_in.get(),80,145)
    v_06=set_txt(amp_m_in.get(),188,145)

    imagery_10[1]=Image.open('img/icon_product.png')
    imagery_10[1]=tk.PhotoImage(file='img/icon_product.png')  
    lbl_icon.config(image=(imagery_10[1]))

def validate1(input):
    if len(input)>3:
        return False
    elif input == '':
        return True
    else:
        return True

def validate2(input):
    if len(input)>8:
        return False
    elif input == '':
        return True
    else:
        return True

#main frame
main_frame = tk.Frame(main, height=600, width=600)
main_frame.place(relwidth=1.0,relheight=1.0)

#main background
bkgrd_img = tk.PhotoImage(file='img/app_bg.png')
bkgrd_lbl = tk.Label(main_frame, image=bkgrd_img)
bkgrd_lbl.place(relwidth=1.0,relheight=1.0)

#register text validation for modifiers M and T, tie to function validate
val_ent1=main.register(validate1)
val_ent2=main.register(validate2)

#labels & selection input boxes
lbl_01=tk.Label(main_frame,text='MAIN ICON',background='#ededed',
                relief='raised')
lbl_02=tk.Label(main_frame,text='Modifier 1',background='#ededed',
                relief='raised')
lbl_03=tk.Label(main_frame,text='Modifier 2',background='#ededed',
                relief='raised')
lbl_04=tk.Label(main_frame, text='B/D (Amplifier)',background='#ededed',
                relief='raised')
lbl_05=tk.Label(main_frame, text='T (Amplifier)',background='#ededed',
                relief='raised')
lbl_06=tk.Label(main_frame, text='M (Amplifier)',background='#ededed',
                relief='raised')

cmb_01=ttk.Combobox(main_frame,values=unit_val,state='readonly')
cmb_02=ttk.Combobox(main_frame,values=mod_one,state='disabled')
cmb_03=ttk.Combobox(main_frame,values=mod_two,state='disabled')
cmb_04=ttk.Combobox(main_frame,values=bd_amp,state='readonly')

ent_05=ttk.Entry(main_frame,textvariable=amp_t_in,
                 validate='key',validatecommand=(val_ent1,'%P'),
                 width=25)
ent_06=ttk.Entry(main_frame,textvariable=amp_m_in,
                 validate='key',validatecommand=(val_ent2,'%P'),
                 width=25)

lbl_01.place(height=25,width=110,x=25,y=85)
lbl_02.place(height=25,width=110,x=436,y=47)
lbl_03.place(height=25,width=110,x=436,y=111)
lbl_04.place(height=25,width=110,x=230,y=100)
lbl_05.place(height=25,width=110,x=25,y=290)
lbl_06.place(height=25,width=110,x=442,y=286)

cmb_01.place(height=25,width=110,x=25,y=115)
cmb_01.current(0)
cmb_02.place(height=25,width=110,x=436,y=77)
cmb_02.current(0)
cmb_03.place(height=25,width=110,x=436,y=141)
cmb_03.current(0)
cmb_04.place(height=25,width=110,x=230,y=130)
cmb_04.current(0)

ent_05.place(height=25,width=110,x=25,y=320)
ent_06.place(height=25,width=110,x=442,y=316)

#main icon set button
btn_01=tk.Button(main_frame,text='CREATE', bg='#a6a8c2',
                 command=lambda:set_icon())
btn_01.place(height=25,width=110,
             x=170,y=470)

btn_02=tk.Button(main_frame,text='RESET',bg='#a6a8c2',
                 command=lambda:reset())
btn_02.place(height=25,width=110,
             x=295,y=470)

btn_03=tk.Button(main_frame,text='SAVE SYMBOL',bg='#a6a8c2',
                 command=lambda:save_img())
btn_03.place(height=25,width=110,
             x=230,y=505)

#main icon graphic label
lbl_icon=ttk.Label(main_frame,image=imagery_10[2],
                   anchor='center',padding=2,background='White')
lbl_icon.place(height=245,width=270,
          x=148,y=190)

main.mainloop()

'''notes below...


'''
