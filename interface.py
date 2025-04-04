import customtkinter as ctk
import function
clicar = function.clique
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')
app = ctk.CTk()
app.geometry("500x500")
app.title('Calculadora')
visor = ctk.CTkLabel(app,text="0", width=100, height=100)
visor.place(x=15,y=15)
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

    botao_9 = ctk.CTkButton(width=15,master = app, text="9", command=clicar)
    botao_9.pack(pady=5)
    botao_9.place(x=100,y=170)

    botao_8 = ctk.CTkButton(width=15,master = app, text="8", command=clicar)
    botao_8.pack(pady=5)
    botao_8.place(x=80,y=170)

    botao_7 = ctk.CTkButton(width=15,master = app, text="7", command=clicar)
    botao_7.pack(pady=5)
    botao_7.place(x=140,y=130)

    botao_6 = ctk.CTkButton(width=15,master = app, text="6", command=clicar)
    botao_6.pack(pady=5)
    botao_6.place(x=120,y=130)

    botao_5 = ctk.CTkButton(width=15,master = app, text="5", command=clicar)
    botao_5.pack(pady=5)
    botao_5.place(x=100,y=130)

    botao_4 = ctk.CTkButton(width=15,master = app, text="4", command=clicar)
    botao_4.pack(pady=5)
    botao_4.place(x=80,y=130)

    botao_3 = ctk.CTkButton(width=15,master = app, text="3", command=clicar)
    botao_3.pack(pady=5)
    botao_3.place(x=140,y=90)

    botao_2 = ctk.CTkButton(width=15,master = app, text="2", command=clicar)
    botao_2.pack(pady=5)
    botao_2.place(x=120,y=90)

    botao_1 =  ctk.CTkButton(width=15,master = app, text="1", command=clicar)
    botao_1.pack(pady=5)
    botao_1.place(x=100,y=90)

    botao_0 = ctk.CTkButton(width=15,master = app, text="0", command=clicar)
    botao_0.pack(pady=5)
    botao_0.place(x=80,y=90)

botoes()
app.mainloop()