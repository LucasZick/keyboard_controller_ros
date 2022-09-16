import os
import sys
import time

#-----------------------------------------

def close():
    os.system("clear")
    print("Closing application...")
    time.sleep(2)
    os.system("clear")
    sys.exit(0)

#-----------------------------------------

def mov_linear_frente():
    print("mov_linear_frente")

def mov_linear_tras():
    print("mov_linear_tras")

def mov_angular_anti():
    print("mov_angular_anti")

def mov_angular_hor():
    print("mov_angular_hor")

def mov_linear_frente_giro_anti():
    print("mov_linear_frente_giro_anti")

def mov_linear_tras_giro_anti():
    print("mov_linear_tras_giro_anti")

def mov_linear_frente_giro_hor():
    print("mov_linear_frente_giro_hor")

def mov_linear_tras_giro_hor():
    print("mov_linear_tras_giro_hor")

def parado():
    print("parado")

def inc_vel_linear():
    print("inc_vel_linear")

def dec_vel_linear():
    print("dec_vel_linear")

def inc_vel_angular():
    print("inc_vel_angular")

def dec_vel_angular():
    print("dec_vel_angular")

def fecha_no():
    print("fecha_no")
    close()

option_dict = {
    "w": ["Movimento linear para frente", mov_linear_frente],
    "x": ["Movimento linear para trás", mov_linear_tras],
    "a": ["Movimento angular anti-horário", mov_angular_anti],
    "d": ["Movimento angular horário", mov_angular_hor],
    "q": ["Movimento linear para frente com giro anti-horário", mov_linear_frente_giro_anti],
    "z": ["Movimento linear para trás com giro anti-horário", mov_linear_tras_giro_anti],
    "e": ["Movimento linear para frente com giro horário", mov_linear_frente_giro_hor],
    "c": ["Movimento linear para trás com giro horário", mov_linear_tras_giro_hor],
    "s": ["Parado", parado],
    "1": ["Incrementa a velocidade linear", inc_vel_linear],
    "2": ["Decrementa a velocidade linear", dec_vel_linear],
    "3": ["Incrementa a velocidade angular", inc_vel_angular],
    "4": ["Decrementa a velocidade angular", dec_vel_angular],
    "p": ["Fecha o nó", fecha_no],
}
