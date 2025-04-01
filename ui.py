import tkinter as tk
from tkinter import scrolledtext, font
from chatbot import chat_with_model 

historial_conversacion = []

def enviar_mensaje():
    user_message = entrada_usuario.get().strip()
    
    if user_message:
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "Usuario: " + user_message + "\n", 'usuario')
        chat_display.insert(tk.END, "Cargando...\n", 'sistema')
        chat_display.config(state=tk.DISABLED)
        ventana.update_idletasks()
        
        response = chat_with_model(user_message)
        
        chat_display.config(state=tk.NORMAL)
        chat_display.delete('end-2l', 'end-1l') 
        chat_display.insert(tk.END, "IA: " + response + "\n\n", 'ia')
        chat_display.config(state=tk.DISABLED)
        
        chat_display.yview(tk.END)
        
        entrada_usuario.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Chatbot Jurídico")
ventana.geometry("800x650")  
ventana.configure(bg="#49111C")  

fuente_base = font.nametofont("TkDefaultFont")
ventana.option_add("*Font", fuente_base)

chat_display = scrolledtext.ScrolledText(
    ventana,
    width=110,
    height=30,
    wrap=tk.WORD,
    state=tk.DISABLED,
    bg="#F2F4F3",  
    fg="#0A0908",  
    bd=5,
    relief=tk.RAISED,
    padx=10,
    pady=10
)
chat_display.grid(row=0, column=0, padx=40, pady=40, columnspan=2)

chat_display.tag_configure('usuario', foreground='#0A0908', font=(fuente_base.actual()['family'], 12, 'bold'))
chat_display.tag_configure('ia', foreground='#0A0908', font=(fuente_base.actual()['family'], 12))
chat_display.tag_configure('sistema', foreground='#0A0908', font=(fuente_base.actual()['family'], 12, 'italic'))

fuente_negrita = font.Font(family=fuente_base.actual()['family'], size=12, weight='bold')

label_entrada = tk.Label(
    ventana,
    text="Escribe tu consulta:",
    bg="#49111C",
    fg="#F2F4F3",
    font=fuente_negrita
)
label_entrada.grid(row=1, column=0, padx=40, pady=0, sticky="w")

entrada_usuario = tk.Entry(
    ventana,
    width=60,
    bg="#F2F4F3", 
    fg="#0A0908",  
    bd=5,
    relief=tk.RAISED,
    font=fuente_negrita 
)
entrada_usuario.grid(row=2, column=0, padx=5, pady=5)

enviar_button = tk.Button(
    ventana,
    text="Enviar",
    command=enviar_mensaje,
    bg="#F2F4F3",  
    fg="#0A0908",  
    bd=5,
    relief=tk.RAISED,
    font=fuente_base
)
enviar_button.grid(row=2, column=1, padx=5, pady=5)

ventana.mainloop()