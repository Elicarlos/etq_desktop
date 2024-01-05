from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time

import ttkbootstrap as ttk 
from ttkbootstrap.constants import *


class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('Sistema Gerenciador')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.config(background="#eff5f6")

        icon = PhotoImage(file='images\\profile.png')
        self.window.iconphoto(True, icon)

        self.header = Frame(self.window, bg="#009df4")
        self.header.place(x=300, y=0, width=1070, height=70)
        self.logout_text = Button(self.header, text='Sair', bg="#32cf8e", 
            font=('', 13, 'bold'), bd=0, fg='white',
            cursor='hand2', activebackground="#32cf8e" )
        
        self.logout_text.place(x=950, y=15)

        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # logo
        self.logoImage = Image.open('images\\profile.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg="#ffffff")
        self.logo.image = photo
        self.logo.place(x=70, y=80)

        # Name of Brand
        self.brand_name = Label(self.sidebar, text="Elicarlos Ferreira",
             bg="#ffffff",font=("", 15, "bold"))
        self.brand_name.place(x=80, y=200)


        # Dashboard
        self.dashboard_image = Image.open('images\\profile.png')
        photo = ImageTk.PhotoImage(self.dashboard_image)
        self.dashboard = Label(self.sidebar, image=photo, bg="#ffffff")
        self.dashboard.image = photo
        self.dashboard.place(x=35, y=289)

       

        self.dashboard_text = Button(self.sidebar, text="Dasboard", bg="#ffffff",
            font=("", 13, 'bold'), bd=0, cursor='hand2', activebackground="#ffffff")
        
        self.dashboard_text.place(x=80, y=291)


         # Manage
        self.manage_image = Image.open('images\\profile.png')
        photo = ImageTk.PhotoImage(self.manage_image)
        self.manage = Label(self.sidebar, image=photo, bg="#ffffff")
        self.manage.image = photo
        self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text='Manage', bg='#ffffff',
            font=("", 13, 'bold'), bd=0, cursor='hand2', activeforeground="#ffffff")
        self.manage_text.place(x=80, y=345 )

        # Settings
        # self.settings_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.settings_image)
        # self.settings = Label(self.sidebar, image=photo, bg="#ffffff")
        # self.settings.image = photo
        # self.settings.place(x=35, y=402)

        # self.settings_text = Button(self.sidebar, text="Settings", 
        #                             font=('', 13, 'bold'),bg="#ffffff",
        #     cursor="hand2",bd=0, activebackground='#ffffff')
        
        # self.settings_text.place(x=80, y=402)


        # Exite
        # self.exit_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.exit_image)
        # self.exit = Label(self.sidebar, image=photo, bg="#ffffff")
        # self.exit.image = photo
        # self.exit.place(x=25, y=452)

        # self.exit_text = Button(self.sidebar, text="Settings", 
        #                             font=('', 13, 'bold'),bg="#ffffff",
        #     cursor="hand2",bd=0, activebackground='#ffffff')
        
        # self.settings_text.place(x=85, y=462)



        self.heading = Label(self.window, text="Dasboard", 
            font=('', 13, 'bold'),
            fg="#0064d3", bg="#eff5f6")
        
        self.heading.place(x=325, y=70)

        

        self.bodyframe1 = Frame(self.window, bg="#ffffff")
        self.bodyframe1.place(x=328, y=110, width=1060, height=540)

        def cadastro_produto():
            self.cadastro_produto_frame = LabelFrame(self.bodyframe1, text="Cadastro Produtos", bd="#fff211")
            self.cadastro_produto_frame.grid(row=0, column=0)

            self.descricao = Label(self.cadastro_produto_frame, text="Descricao")

            

        cadastro_produto()
        # self.bodyframe3 = Frame(self.window, bg='#e21f26')
        # self.bodyframe3.place(x=680, y=495, width=310, height=220)

        # self.bodyframe4 = Frame(self.window, bg='#ffcb1f')
        # self.bodyframe4.place(x=1030, y=495, width=310, height=220)

        # PieChart
        # self.piechart_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.piechart_image)
        # self.piechart = Label(self.bodyframe1, image=photo, bg="#ffffff")
        # self.piechart.image = photo
        # self.piechart.place(x=690, y=70)

        # Graph
        # self.graph_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.graph_image)
        # self.graph = Label(self.bodyframe1, image=photo, bg="#ffffff")
        # self.graph.image = photo
        # self.graph.place(x=40, y=70)

         # Totla Peaple
        # self.total_peaple_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.total_peaple_image)
        # self.total_peaple = Label(self.bodyframe2, image=photo, bg="#ffffff")
        # self.total_peaple.image = photo
        # self.total_peaple.place(x=220, y=0)

        # self.total_peaple_text = Label(self.bodyframe2, text='230', bg="#009aa5",
        #     font=('', 13, 'bold'))
        # self.total_peaple_text.place(x=120,y=100 )


         # Totla Peaple
        # self.total_peaple_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.total_peaple_image)
        # self.total_peaple = Label(self.bodyframe2, image=photo, bg="#ffffff")
        # self.total_peaple.image = photo
        # self.total_peaple.place(x=220, y=0)

        # self.total_peaple_text = Label(self.bodyframe2, text='230', bg="#009aa5",
        #     font=('', 13, 'bold'))
        # self.total_peaple_text.place(x=120,y=100 )


        # Left
        # self.peaple_who_left_image = Image.open('images\\profile.png')
        # photo = ImageTk.PhotoImage(self.peaple_who_left_image)
        # self.peaple_who_left = Label(self.bodyframe3, image=photo, bg="#e21f26")
        # self.peaple_who_left.image = photo
        # self.peaple_who_left.place(x=220, y=0)

        # self.peaple_who_left_text = Label(self.bodyframe3, text='230', bg="#009aa5",
        #     font=('', 13, 'bold'))
        # self.peaple_who_left_text.place(x=5,y=5 )

    
















def win():
    window = Tk()
    Dashboard(window)
    window.mainloop()


if __name__ == '__main__':
    win()


