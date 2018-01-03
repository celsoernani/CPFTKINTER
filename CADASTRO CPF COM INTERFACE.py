from tkinter import *
import os 
bancodedados= {}
class app:
    def __init__(self,cont):
        self.cesta=Frame(cont,padx=100,pady=50,bg="black")
        self.cesta.pack()
        self.label=Label(self.cesta,bg= "black", fg="pink",text="Nome:",font=("Cosmic Sans", 10))
        self.label.pack()
        self.entrada1= Entry(self.cesta,bg= "white", fg="black")
        self.entrada1.focus_force()
        self.entrada1.pack()
        self.label1=Label(self.cesta,bg= "black", fg="pink",text="CPF:",font=("Cosmic Sans", 10))
        self.label1.pack()
        self.entrada2= Entry(self.cesta,bg= "white", fg="black",font=("Cosmic Sans", 10))
        self.entrada2.pack()
        self.label2=Label(self.cesta,bg= "black", fg="pink",font=("Cosmic Sans", 10),text= "")
        self.label2.pack(side= TOP)
        
#BOTAGRAVAR
        self.botao= Button(self.cesta, text="CADASTRAR", bg= "black", fg="pink",font=("Cosmic Sans", 10))
#BOTAPROCURAR
        self.botao1= Button(self.cesta, text="PROCURAR", bg= "black", fg="pink",font=("Cosmic Sans", 10))
#BOTAOSALVARARQ
        self.botao3= Button(self.cesta,text="SALVAR", bg= "black", fg="pink",font=("Cosmic Sans", 10))
#BOTÃ0SAIR
        self.botao2= Button(self.cesta, text="SAIR", bg= "black", fg="pink",font=("Cosmic Sans", 10), command=self.sair)

        self.botao2.pack(side= RIGHT)
        self.botao3.pack(side= RIGHT)
        self.botao1.pack(side= RIGHT)
        self.botao.pack(side= RIGHT)
        self.botao.bind("<Button-1>", self.gravar)
        self.botao1.bind("<Button-1>", self.procurar)
        self.botao3.bind("<Button-1>", self.salvar)
    def sair(self):
        os._exit(1)
    def gravar(self, event):
         if  self.entrada1.get() in bancodedados.keys():
             self.label2["text"]= "Usuario já cadastrado "
         else:
            bancodedados[self.entrada1.get()]= self.entrada2.get()
            self.label2["text"]= "Usuario cadastrado"
    print(bancodedados)
    def procurar(self,event):
        if  self.entrada1.get() in bancodedados.keys():
            self.label2["text"]= bancodedados[self.entrada1.get()]
    def salvar(self,event):
        arq = open("Arquivo.txt", "w")
        arq.write("Contatinhos 2017\n")
        for i,j in bancodedados.items():
            arq.write(str(i))
            arq.write(" ")
            arq.write(str(j))
            arq.write("\n")
        arq.close()
        print("Arquivo gravado com sucesso!")
            
                            
                


raiz = Tk(None, None, "Cadastro")
ap = app(raiz)
raiz.mainloop()
