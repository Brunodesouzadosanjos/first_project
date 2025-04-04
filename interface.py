import customtkinter as ctk
import function
clicar = function.clique
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')
app = ctk.CTk()
app.geometry("500x500")
app.title('Calculadora')
def botoes():
    botao_adicao = ctk.CTkButton(width=15,master = app, text="+", command=clicar)
    botao_adicao.pack(pady=5)
    botao_adicao.place(x=80,y=50)
    botao_subtracao = ctk.CTkButton(width=15,master = app, text="-", command=clicar)
    botao_subtracao.pack(pady=5)
    botao_subtracao.place(x=100,y=50)
    botao_divisao = ctk.CTkButton(width=15,master = app, text="/", command=clicar)
    botao_divisao.pack(pady=5)
    botao_divisao.place(x=120,y=50)
    botao_multiplicacao = ctk.CTkButton(width=15,master = app, text="*", command=clicar)
    botao_multiplicacao.pack(pady=5)
    botao_multiplicacao.place(x=140,y=50)

botoes()
app.mainloop()