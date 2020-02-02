#!/usr/bin/python3
import time
import pigpio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
""" ############### RASPBERRY 2 Sensores ################ """
GPIO.setup(4, GPIO.IN)     
GPIO.setup(17, GPIO.IN)    
GPIO.setup(18, GPIO.IN)  
GPIO.setup(27, GPIO.IN) 
GPIO.setup(22, GPIO.IN) 
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(9, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(7, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)

rasp_2 = pigpio.pi('192.168.3.205')  ##raspberry slave
##print(rasp_2.connected)
def Guardar_Sensores(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28):
    con = pymysql.connect('192.168.3.202','root', 'spsi2018','cintas_santacatalina')
    cursor = con.cursor()
    cursor.execute("UPDATE entradas SET s1= b'"+s1+"',s2= b'"+s2+"',s3= b'"+s3+"',s4= b'"+s4+"',"
                   +"s5= b'"+s5+"',s6= b'"+s6+"',s7= b'"+s7+"',s8= b'"+s8+"',s9= b'"+s9+"',"
                   +"s10= b'"+s10+"',s11= b'"+s11+"',s12= b'"+s12+"',s13= b'"+s13+"',s14= b'"+s14+"',"
                   +"s15= b'"+s15+"',s16= b'"+s16+"',s17= b'"+s17+"',s18= b'"+s18+"',s19= b'"+s19+"',"
                   +"s20= b'"+s20+"',s21= b'"+s21+"',s22= b'"+s22+"',s23= b'"+s23+"',s24= b'"+s24+"',"
                   +"s25= b'"+s25+"',s26= b'"+s26+"',s27= b'"+s27+"',s28= b'"+s28+"' WHERE id = 1")
    con.commit()
    con.close()
    cursor.close()
print(" ")
print("=============================================")
print("           SISTEMA SENSORES SPSI")
print("=============================================")
print(" ")
if(rasp_2.connected):
    print("           INTERFAZ FUNCIONANDO")

while(True):
    Guardar_Sensores(str(rasp_2.read(11)),str(GPIO.input(17)),str(GPIO.input(18)),str(GPIO.input(27)),str(GPIO.input(22)),
                     str(rasp_2.read(8)),str(GPIO.input(24)),str(GPIO.input(10)),str(GPIO.input(9)),str(GPIO.input(25)),
                     str(GPIO.input(11)),str(GPIO.input(8)),str(GPIO.input(7)),str(GPIO.input(5)),str(GPIO.input(6)),
                     str(GPIO.input(12)),str(GPIO.input(13)),str(GPIO.input(19)),str(rasp_2.read(4)),str(rasp_2.read(17)),
                     str(rasp_2.read(18)),str(rasp_2.read(27)),str(rasp_2.read(22)),str(rasp_2.read(23)),str(rasp_2.read(24)),
                     str(rasp_2.read(10)),str(rasp_2.read(7)),str(rasp_2.read(25)),str(rasp_2.read(5)))

    time.sleep(.1)
