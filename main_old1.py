import ttkbootstrap as ttk 
from ttkbootstrap.constants import *


class DataEntryForm(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20,10))
        self.pack(fill=BOTH, expand=YES)

        # forms variables
        self.descricao = ttk.StringVar(value="")
        self.preco = ttk.StringVar(value="")

        # Form header
        hdr_text = "Digite para buscar o produto"
        hdr = ttk.Label(master=self, text=hdr_text, width=50)
        hdr.pack(fill=X, pady=10)

        # forms entries
        self.create_form_entry('Descricao', self.descricao)
        self.create_form_entry('Preço', self.preco)

        self.create_buttonbox()

    def create_form_entry(self, label, variable):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent =   ttk.Entry(master=container, text=label.title(), width=10)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)


    def create_buttonbox(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Buscar",
            command=self.on_submit,
            bootstyle= SUCCESS,
            width=6
        )

        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()


        cnl_btn = ttk.Button(
            master=container,
            text='Cancelar',
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6
        )

        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        print('Descricao', self.descricao.get())

        return self.descricao.get()
    

    def on_cancel(self):
        self.quit()


if __name__ == '__main__':
    app = ttk.Window('Etiquetario', "superhero", resizable=(False, False))
    DataEntryForm(app)
    app.mainloop()






