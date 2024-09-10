from tkinter import *
from tkinter import ttk

class JuegoDelGato:
    def __init__(self):
        self.reiniciar()
    
    def reiniciar(self):
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.jugador_actual = "X"
    
    def cambiar_turno(self):
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def realizar_movimiento(self, fila: int, columna: int) -> bool:
        if self.tablero[fila][columna] == "":
            self.tablero[fila][columna] = self.jugador_actual
            return True
        return False

    def verificar_ganador(self):
        combinaciones = [
            [self.tablero[0][0], self.tablero[0][1], self.tablero[0][2]],
            [self.tablero[1][0], self.tablero[1][1], self.tablero[1][2]],
            [self.tablero[2][0], self.tablero[2][1], self.tablero[2][2]],
            [self.tablero[0][0], self.tablero[1][0], self.tablero[2][0]],
            [self.tablero[0][1], self.tablero[1][1], self.tablero[2][1]],
            [self.tablero[0][2], self.tablero[1][2], self.tablero[2][2]],
            [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]],
            [self.tablero[2][0], self.tablero[1][1], self.tablero[0][2]],
        ]
        for linea in combinaciones:
            if linea[0] == linea[1] == linea[2] != "":
                return linea[0]
        return None

    def verificar_empate(self):
        return all(self.tablero[r][c] != "" for r in range(3) for c in range(3))


class InterfazGrafica:
    def __init__(self, juego: JuegoDelGato):
        self.juego = juego
        self.root = Tk()
        self.root.title("Juego Gato y Ratón")
        self.turno = StringVar(value=f"Turno de {self.juego.jugador_actual}")
        self.ganador = StringVar()
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        
        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        ttk.Label(mainframe, textvariable=self.turno).grid(column=0, row=0, columnspan=3)
        ttk.Label(mainframe, textvariable=self.ganador).grid(column=0, row=4, columnspan=3)
        
        for r in range(3):
            for c in range(3):
                self.botones[r][c] = ttk.Button(mainframe, text="", command=lambda r=r, c=c: self.jugar(r, c))
                self.botones[r][c].grid(column=c, row=r+1, sticky=(W, E))
        
        self.boton_reiniciar = ttk.Button(mainframe, text="Reiniciar Juego", command=self.reiniciar)
        self.boton_reiniciar.grid(column=0, row=5, columnspan=3, sticky=(W, E))
        
        self.root.mainloop()

    def jugar(self, fila, columna):
        if self.juego.realizar_movimiento(fila, columna):
            self.actualizar_interfaz()
            ganador = self.juego.verificar_ganador()
            if ganador:
                self.ganador.set(f"¡{ganador} gana!")
                self.boton_reiniciar.config(state=NORMAL)  
            elif self.juego.verificar_empate():
                self.ganador.set("¡Empate!")
                self.boton_reiniciar.config(state=NORMAL) 
            else: 
                self.juego.cambiar_turno()
                self.turno.set(f"Turno de {self.juego.jugador_actual}")
    
    def actualizar_interfaz(self):
        for r in range(3):
            for c in range(3):
                self.botones[r][c].config(text=self.juego.tablero[r][c])
    
    def reiniciar(self):
        self.juego.reiniciar()
        self.actualizar_interfaz()
        self.ganador.set("")
        self.turno.set(f"Turno de {self.juego.jugador_actual}")
        self.boton_reiniciar.config(state=DISABLED) 


juego = JuegoDelGato()
InterfazGrafica(juego)
def cambiar_turno(self): self.jugador_actual = "O" if self.jugador_actual == "X" else "X"



