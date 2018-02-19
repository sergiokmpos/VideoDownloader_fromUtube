from tkinter import *
from tkinter import ttk
import tkinter as tk
import pytube
import io
from PIL import Image, ImageTk
from urllib.request import urlopen
from tkinter import messagebox


#=========================================     OK   ============================

# Janela Principal
janela = Tk()
janela["bg"] = 'snow'
janela.title("YouTube Video Downloader Application 1.0" )
janela.geometry('660x467+100+100')
janela.resizable(False, False)
filename = PhotoImage ( file="C:\\Users\\Sergio Campos\\PycharmProjects\\Downloader\\WPFinalUdown.png")
bg_label = Label(janela, image=filename)
bg_label.place(x=0, y=0)

#=========================================     OK   ============================

titulo =""
status ="Aguardando comando"
log = ""
link = ""
yt = ""
fotovideo = ""

#=========================================     OK   ============================

# Entry box para o Link do video
link = StringVar ( )
ibx = ttk.Entry ( textvariable=link )
ibx.place(x=95, y=63,  width=420,)

#Entry Caminho
caminho = str()
ibx2 = ttk.Entry(textvariable=caminho)
ibx2.place(x=65, y=405, width=500)

#=========================================     OK   ============================


# label para exibir  o título do video para validar que irá baixar o correto
lb1 = Label ( janela , text=titulo , fg="blue" , font=12 )
lb1.place ( x=95 , y=93)
lb1[ "bg" ] = 'snow'

# status
lb2 = Label ( janela , text=status , font=6 )
lb2.place ( x=5 , y=442 )
lb2[ "bg" ] = 'turquoise3'

lb3 = Label ( janela , text="Log de downloads:" )
lb3.place ( x=15 , y=170)
lb3[ "bg" ] = 'lavender'

# log
T = Text(janela, height=12, width=80, relief=FLAT)
T.place ( x=10 , y=195 )
T.insert(END, log)

#=========================================     OK   ============================

def tit_lb1(titulo):
    lb1.config(text=titulo)

def sts_lb2(status):
    lb2.config(text=status)

def log_txt(log):
    T.insert(END,log)

def stt_bt():
    bt2.configure(state=NORMAL)

def bt_click1():
    link = str ( ibx.get ( ) )
    if link != "":
        link = str ( ibx.get ( ) )
        yt = pytube.YouTube ( link )
        titulo1 = yt.title
        titulo = str ( (titulo1[ 0:70 ]) + "..." )
        # Exibindo o título no label
        tit_lb1 ( titulo )
        # Status
        status = "Confirme o download se o título estiver correto    "
        # Exibindo o status no label
        lb2.config ( text=status )
        # Botão2
        bt2 = Button ( janela , width=10 , text="Baixar" , foreground="snow" , command=bt_click2 , relief=FLAT ,
                       state=NORMAL )
        bt2.place ( x=240 , y=125 , width=190 )
        bt2[ "bg" ] = 'DeepSkyBlue4'

        imagem = yt.thumbnail_url
        fotovideo = imagem
        pic_url = fotovideo
        my_page = urlopen(pic_url )
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture )
        tk_img = ImageTk.PhotoImage(pil_img)
        label = tk.Label(janela, image=tk_img )
        label.place(x=531, y=4)
        janela.mainloop()

    else:
        messagebox.showerror("Erro", "Digite ou cole o link" )


def bt_click2():
    caminho = str ( ibx2.get ( ) )
    if caminho != "":
        link = str ( ibx.get ( ) )
        yt = pytube.YouTube( link )
        titulo2 = yt.title
        # Status
        status = "O Download do video foi concluido com sucesso"
        # Exibindo o status no label
        sts_lb2 ( status )
        pasta = (caminho)
        yt.streams.all()
        stream = yt.streams.first()
        stream.download(pasta)
        log = (titulo2 + "\n")
        print(log)
        ibx.delete(0, 'end')
        tit_lb1(titulo)
        log_txt(log)
        bt2 = Button ( janela , width=10 , text="Baixar" , foreground="snow" , command=bt_click2 , relief=FLAT ,
                       state=DISABLED)
        bt2.place ( x=240 , y=125 , width=190 )
        bt2["bg"] = 'DeepSkyBlue4'

    else:
        messagebox.showerror("Erro", "Digite ou cole o caminho" )


def bt_click3():
    sts_lb2 ( status )
    tit_lb1 ( titulo )
    ibx.delete ( 0 , 'end' )


# botão 1
bt1 = Button(janela, width=10, text="Validar", foreground="snow", command=bt_click1, relief=FLAT)
bt1.place(x=20, y=125, width=190)
bt1["bg"] = 'SteelBlue4'

# botão 2
bt2 = Button ( janela , width=10 , text="Baixar" , foreground="snow" , command=bt_click2 , relief=FLAT ,
               state=DISABLED)
bt2.place ( x=240 , y=125 , width=190 )
bt2[ "bg" ] = 'gray'

# botão 3
bt2 = Button(janela, width=10, text="Limpar", foreground="snow", command=bt_click3, relief=FLAT )
bt2.place(x=460, y=125, width=190)
bt2["bg"] = 'SpringGreen4'


janela.mainloop ( )