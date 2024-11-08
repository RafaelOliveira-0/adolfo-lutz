from tkinter import *
class Login():
    def __init__ (self):
        self.janelaPrincipal = Tk()
        self.janelaPrincipal.title('Login')
        self.janelaPrincipal.geometry("800x450")
        # self.janelaPrincipal.configure(bg_color='#C5E7FF')
        self.janelaPrincipal.iconbitmap('images/icon_logo.ico') #ícone da barra de título
        self.janelaPrincipal._set_appearance_mode('light') #passando a janela para o modo claro
        self.janelaPrincipal.wm_state('zoomed') #maximiza a janela
        self.janelaPrincipal.update()

       

        self.lblUsuarioLogin = Label(self.frmEntry, text="Usuário", text_color="#042F48", font=("Roboto", 15, "bold"))
        self.lblUsuarioLogin.place(relx=0, rely=0.05, anchor="w")

        self.cxaUsuarioLogin = Entry(self.frmEntry, fg_color="#C5E7FF", text_color="#042F48", font=("Roboto", 17),
                                        border_width=0)
        self.cxaUsuarioLogin.place(rely=0.1, relwidth=1, relheight=0.15)

        self.lblSenhaLogin = Label(self.frmEntry, text="Senha", text_color="#042F48", font=("Roboto", 15, "bold"))
        self.lblSenhaLogin.place(relx=0, rely=0.4, anchor="w")

        self.cxaSenhaLogin = Entry(self.frmEntry, fg_color="#C5E7FF", text_color="#042F48", font=("Roboto", 17, "bold"),
                                      border_width=0, show="*")
        self.cxaSenhaLogin.place(relx=0, rely=0.45, relwidth=1, relheight=0.15)

        self.btnEsqueceuSenha = Button(self.frmEntry, text="Esqueceu a senha?", text_color="#666666", fg_color="#FFFFFF",
                                          hover_color="#FFFFFF", font=self.underline_font, command=lambda:self.EsqueceuSenha())
        self.btnEsqueceuSenha.bind("<Enter>", self.on_enter) 
        self.btnEsqueceuSenha.bind("<Leave>", self.on_leave)
        self.btnEsqueceuSenha.place(relx=1, rely=0.65, relwidth=0.50, relheight=0.1, anchor="e")

        self.btnEntrar = Button(self.frmEntry, text="Entrar", text_color="#B3D1E7", fg_color="#1672A7",
                                   font=("Arial", 15, "bold"))
        self.btnEntrar.place(relx=0.5, rely=1, relwidth=0.35, relheight=0.12, anchor="s")

        self.janelaPrincipal.bind("<Configure>", lambda event: (self.AjustarFonte(event), self.AjustarImagem(event)))
        
        self.janelaPrincipal.mainloop()

    def EsqueceuSenha(self):
        self.frmLogin.place_forget()
        self.frmEsqueceu = Frame(self.janelaPrincipal, fg_color="#FFFFFF", corner_radius=20)
        self.frmEsqueceu.place(relx=0.50, rely=0.50, relwidth=0.30, relheight=0.70, anchor="center")

    def AjustarImagem(self, event):
        #image_redimensionada = self.logo.resize((int(self.janelaPrincipal.winfo_width()*0.72), int(self.janelaPrincipal.winfo_width()*0.72)), Image.LANCZOS)
        self.image_ctk = Image(self.logo, size=(int(self.janelaPrincipal.winfo_width()*0.080), int(self.janelaPrincipal.winfo_width()*0.080)))
        self.imgLogo.configure(image=self.image_ctk)
        self.imgLogo.image = self.image_ctk

    def AjustarFonte(self, event):
        escala = self.janelaPrincipal.winfo_width() / 1366
        self.lblAdolfo.configure(font=("Roboto", escala*32, "bold"))
        self.lblLutz.configure(font=("Roboto", escala*32, "bold"))
        self.lblClinica.configure(font=("Roboto", escala*15))
        self.lblUsuarioLogin.configure(font=("Roboto", escala*15, "bold"))
        self.cxaUsuarioLogin.configure(font=("Roboto", escala*17))
        self.lblSenhaLogin.configure(font=("Roboto", escala*15, "bold"))
        self.cxaSenhaLogin.configure(font=("Roboto", escala*17, "bold"))
        self.underline_font.configure(size=int(escala*12))
        self.btnEsqueceuSenha.configure(font=self.underline_font)
        self.btnEntrar.configure(font=("Arial", escala*15, "bold"))


    def on_enter(self, event):
        self.btnEsqueceuSenha.bind("<Enter>", self.btnEsqueceuSenha.configure(text_color="#042F48"))
    
    def on_leave(self, event):
        self.btnEsqueceuSenha.bind("<Leave>", self.btnEsqueceuSenha.configure(text_color="#666666"))


Login()
