import customtkinter as ctk
import function
clicar = function.clique
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')
app = ctk.CTk()
app.geometry("500x500")
app.title('Calculadora')
botao1 = ctk.CTkButton(master = app, text="clique", command=clicar)
botao1.pack(pady=10)
app.mainloop()