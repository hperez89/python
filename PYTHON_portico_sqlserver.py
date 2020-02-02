#!/usr/bin/python3
import time
import pyodbc


def update_etiqueta(codigo):
    con = pyodbc.connect('DRIVER=FreeTDS;SERVER=192.168.3.112;PORT=1433;DATABASE=etiquetado_system;UID=spsi2;PWD=Spsi.2018')
    
    cursor = con.cursor()
    #cursor.execute("UPDATE etiqueta SET paso1 = 1 WHERE codigo_ean13 = '"+codigo+"'")
    cursor.execute("UPDATE etiquetado_system.dbo.etiqueta SET etiquetado_system.dbo.etiqueta.paso1 = 1 WHERE etiquetado_system.dbo.etiqueta.codigo_ean13 = '1'")
    con.commit()
    cursor.close()
    con.close()
    


print("")
print("========================================================")
print("         SISTEMA DE CAPTURA DE CAJAS 2.0 - SPSI")
print("========================================================")
print("")



while(True):
    codigo = input()
    update_etiqueta(codigo)
    
    """if(codigo_valido(codigo)):
        print("codigo actualizado con exito")
    else:
        print("codigo ya se proceso")"""
