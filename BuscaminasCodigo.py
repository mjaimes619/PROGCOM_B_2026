import tkinter as tk
from tkinter import messagebox
import random

class Buscaminas:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscaminas")
        
        # Configuración del juego
        self.filas = 10
        self.columnas = 10
        self.minas = 14
        self.botones = []
        self.minas_posiciones = []
        self.celdas_descubiertas = 0
        
        # Crear el tablero
        self.crear_tablero()
        self.colocar_minas()
        
    def crear_tablero(self):
        # Frame para el tablero
        frame_tablero = tk.Frame(self.root)
        frame_tablero.pack(pady=10)
        
        # Crear botones en una cuadrícula
        for i in range(self.filas):
            fila_botones = []
            for j in range(self.columnas):
                boton = tk.Button(
                    frame_tablero,
                    width=4,
                    height=2,
                    font=("Arial", 12, "bold"),
                    command=lambda f=i, c=j: self.descubrir_celda(f, c)
                )
                boton.grid(row=i, column=j, padx=1, pady=1)
                
                # Bind para click derecho
                boton.bind("<Button-3>", lambda e, f=i, c=j: self.marcar_celda(f, c))
                
                fila_botones.append(boton)
            self.botones.append(fila_botones)
        
        # Botón de reinicio
        boton_reinicio = tk.Button(
            self.root,
            text="Nuevo Juego",
            font=("Arial", 10),
            command=self.reiniciar_juego
        )
        boton_reinicio.pack(pady=5)
        
        # Label para información
        self.info_label = tk.Label(
            self.root,
            text=f"Minas: {self.minas} | Click izquierdo: descubrir | Click derecho: marcar",
            font=("Arial", 9)
        )
        self.info_label.pack(pady=5)
        
    def colocar_minas(self):
        # Reiniciar posiciones de minas
        self.minas_posiciones = []
        self.tablero_numeros = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]
        
        # Colocar minas aleatoriamente
        while len(self.minas_posiciones) < self.minas:
            fila = random.randint(0, self.filas - 1)
            col = random.randint(0, self.columnas - 1)
            if (fila, col) not in self.minas_posiciones:
                self.minas_posiciones.append((fila, col))
                self.tablero_numeros[fila][col] = -1  # -1 representa mina
        
        # Calcular números para celdas sin minas
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero_numeros[i][j] != -1:
                    self.tablero_numeros[i][j] = self.contar_minas_vecinas(i, j)
    
    def contar_minas_vecinas(self, fila, col):
        contador = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_fila = fila + i
                nueva_col = col + j
                if 0 <= nueva_fila < self.filas and 0 <= nueva_col < self.columnas:
                    if (nueva_fila, nueva_col) in self.minas_posiciones:
                        contador += 1
        return contador
    
    def descubrir_celda(self, fila, col):
        boton = self.botones[fila][col]
        
        # Si la celda ya está descubierta o marcada, no hacer nada
        if boton["state"] == "disabled" or boton["text"] == "🚩":
            return
        
        # Si es una mina, game over
        if (fila, col) in self.minas_posiciones:
            boton.config(text="💥", bg="red", fg="white")
            self.mostrar_todas_minas()
            messagebox.showinfo("Game Over", "💥 ¡BOOM! Has perdido.")
            self.deshabilitar_todos_botones()
            return
        
        # Descubrir la celda
        numero = self.tablero_numeros[fila][col]
        self.mostrar_celda(boton, numero)
        boton.config(state="disabled", relief=tk.SUNKEN)
        self.celdas_descubiertas += 1
        
        # Si la celda está vacía (0), descubrir automáticamente las vecinas
        if numero == 0:
            self.descubrir_vecinas(fila, col)
        
        # Verificar si ganó
        celdas_sin_minas = (self.filas * self.columnas) - self.minas
        if self.celdas_descubiertas == celdas_sin_minas:
            messagebox.showinfo("¡Victoria!", "🎉 ¡Felicidades! Has ganado. 🎉")
            self.deshabilitar_todos_botones()
    
    def mostrar_celda(self, boton, numero):
        if numero == 0:
            boton.config(text=" ", bg="lightgray")
        else:
            colores = {1: "blue", 2: "green", 3: "red", 4: "purple", 
                      5: "maroon", 6: "turquoise", 7: "black", 8: "gray"}
            boton.config(text=str(numero), fg=colores.get(numero, "black"), bg="lightgray")
    
    def descubrir_vecinas(self, fila, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_fila = fila + i
                nueva_col = col + j
                if 0 <= nueva_fila < self.filas and 0 <= nueva_col < self.columnas:
                    boton_vecino = self.botones[nueva_fila][nueva_col]
                    if boton_vecino["state"] != "disabled" and boton_vecino["text"] != "🚩":
                        self.descubrir_celda(nueva_fila, nueva_col)
    
    def marcar_celda(self, fila, col):
        boton = self.botones[fila][col]
        
        # Solo marcar si no está descubierta
        if boton["state"] == "normal":
            if boton["text"] == "":
                boton.config(text="🚩", fg="red")
            elif boton["text"] == "🚩":
                boton.config(text="")
    
    def mostrar_todas_minas(self):
        for fila, col in self.minas_posiciones:
            self.botones[fila][col].config(text="💣", bg="red", fg="white")
    
    def deshabilitar_todos_botones(self):
        for fila in self.botones:
            for boton in fila:
                boton.config(state="disabled")
    
    def reiniciar_juego(self):
        # Limpiar el frame del tablero
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Reiniciar variables
        self.botones = []
        self.celdas_descubiertas = 0
        
        # Crear nuevo tablero
        self.crear_tablero()
        self.colocar_minas()

# Crear ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    juego = Buscaminas(root)
    root.mainloop()