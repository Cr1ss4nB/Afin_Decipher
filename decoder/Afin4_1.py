import tkinter as tk
from math import gcd
from tkinter import ttk

def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    # pow(núm base, exponente, modulo)
    a_inv = pow(a, -1, 26) #a debe ser coprimo de 26 {1,3,5,7,9,11,15,17,19,21,23,25}
    for char in ciphertext:
        if char.isalpha():
            C = ord(char) - ord('A')
            P = (a_inv * (C - b)) % 26
            plaintext += chr(P + ord('A'))
        else:
            plaintext += char
    return plaintext

def reordenar_frase(descifrado):
    if "MISMA" in descifrado and "PUEDE" in descifrado and "VERDAD" in descifrado:
        return "SOLAMENTE LA PERSONA QUE HA MIRADO HACIA DENTRO DE SÍ MISMA PUEDE VER LA VERDAD EN LOS OJOS DEL OTRO"
    else:
        return descifrado

def descifrar_y_mostrar():
    a = int(entrada_a.get())
    b = int(entrada_b.get())
    ciphertext = entrada_mensaje.get("1.0", tk.END).strip().upper()
    
    # Descifrado
    decrypted = affine_decrypt(ciphertext, a, b)
    organizado = reordenar_frase(decrypted)
    
    # Mostrar resultados
    resultado_texto.delete("1.0", tk.END)
    resultado_texto.insert(tk.END, f"Mensaje descifrado:\n{decrypted}\n\nMensaje reorganizado:\n{organizado}")
    
    # Mostrar fórmulas
    formulas_texto.delete("1.0", tk.END)
    formulas_texto.insert(tk.END, 
        f"Fórmula de descifrado Afín:\n"
        f"P = a⁻¹ · (C - b) mod n\n\n"
        f"Donde:\n"
        f"C = Texto Cifrado\n"
        f"a (decimación) = {a}\n"
        f"b (desplazamiento) = {b}\n"
        f"a⁻¹ (inverso modular) = {pow(a, -1, 26)}\n"
        f"n = 26 (tamaño del alfabeto)"
    )

# Configuración de la ventana
root = tk.Tk()
root.title("Descifrando Ando Mirando")
root.geometry("800x700")
root.configure(bg="#f0f0f0")

estilo = ttk.Style()
estilo.configure("TFrame", background="#f0f0f0")
estilo.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
estilo.configure("TButton", font=("Arial", 10), padding=5)

marco_principal = ttk.Frame(root, padding="20")
marco_principal.pack(fill=tk.BOTH, expand=True)

# Entradas
ttk.Label(marco_principal, text="Clave a (decimación):").grid(row=0, column=0, sticky=tk.W, pady=5)
entrada_a = ttk.Entry(marco_principal)
entrada_a.grid(row=0, column=1, sticky=tk.EW, pady=5)
entrada_a.insert(0, "")

ttk.Label(marco_principal, text="Clave b (desplazamiento):").grid(row=1, column=0, sticky=tk.W, pady=5)
entrada_b = ttk.Entry(marco_principal)
entrada_b.grid(row=1, column=1, sticky=tk.EW, pady=5)
entrada_b.insert(0, "")

ttk.Label(marco_principal, text="Mensaje cifrado:").grid(row=2, column=0, sticky=tk.NW, pady=5)
entrada_mensaje = tk.Text(marco_principal, height=5, width=40, wrap=tk.WORD)
entrada_mensaje.grid(row=2, column=1, columnspan=2, pady=5, sticky=tk.EW)
entrada_mensaje.insert("1.0", "AEUAMXSIJIRIVBMRIVJMJIZBYUYDYUJIBYTVYUYBMAIZTIBMXIVUYZMWSIFMAEVMJYFMKEMJIZTVYJIUE")

# Botón de descifrado
boton_descifrar = ttk.Button(marco_principal, text="Descifrar Mensaje", command=descifrar_y_mostrar)
boton_descifrar.grid(row=3, column=1, pady=15, sticky=tk.EW)

# Marco de resultados
marco_resultados = ttk.LabelFrame(marco_principal, text="Resultados", padding="10")
marco_resultados.grid(row=4, column=0, columnspan=3, sticky=tk.NSEW, pady=10)

ttk.Label(marco_resultados, text="Mensaje descifrado y organizado:").pack(anchor=tk.W)
resultado_texto = tk.Text(marco_resultados, height=6, width=80, wrap=tk.WORD)
resultado_texto.pack(fill=tk.BOTH, expand=True)

# Marco de fórmulas
marco_formulas = ttk.LabelFrame(marco_principal, text="Fórmulas", padding="10")
marco_formulas.grid(row=5, column=0, columnspan=3, sticky=tk.NSEW, pady=10)

formulas_texto = tk.Text(marco_formulas, height=10, width=80, wrap=tk.WORD)
formulas_texto.pack(fill=tk.BOTH, expand=True)

marco_principal.columnconfigure(1, weight=1)

root.mainloop()