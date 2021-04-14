#!/usr/bin/env python
# NODO DE TRANSMISION AL ARDUINO

#Se importan las librerias de ROS
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32

#Se declaran variables globales
pub_H = rospy.Publisher('chatter_H_Arduino', Float32, queue_size=10)
D_EH = ""
D_FH = ""
D_GH = ""
D_H_Arduino = 0.0
Resolucion = 15

# Funcion de recepcion Caracter Bool
def callback_EH(data_EH):
    global D_EH 
    rospy.loginfo(rospy.get_caller_id() + ':I heard(EH): %s', data_EH.data)
    D_EH = data_EH.data

# Funcion de recepcion Caracter Int
def callback_FH(data_FH):
    global D_FH 
    rospy.loginfo(rospy.get_caller_id() + ':I heard(FH): %s', data_FH.data)
    D_FH = data_FH.data

def callback_GH(data_GH):   
    global D_GH
    rospy.loginfo(rospy.get_caller_id() + ':I heard(GH): %s', data_GH.data)
    D_GH = data_GH.data 

# Funcion de recepcion Caracter Float
def H():
    global D_EH 
    global D_FH
    global D_GH
    global D_H_Arduino

    #Declaracion del nodo y canales subscriber y publisher
    rospy.init_node('H', anonymous=False)
    rospy.Subscriber('chatter_EH', String, callback_EH) 
    rospy.Subscriber('chatter_FH', String, callback_FH) 
    rospy.Subscriber('chatter_GH', String, callback_GH)

    rate = rospy.Rate(0.2)   # Frecuencia de 0.2 Hz
    while not rospy.is_shutdown():
        #Arbol de posibilidades para velocidad del motor
        if D_EH == "B" and D_FH == "B" and D_GH == "B":  
           D_H_Arduino = 0*Resolucion
        elif D_EH == "B" and D_FH == "B" and D_GH == "M":  
           D_H_Arduino = 1*Resolucion
        elif D_EH == "B" and D_FH == "B" and D_GH == "A":  
           D_H_Arduino = 2*Resolucion
        elif D_EH == "B" and D_FH == "M" and D_GH == "B":  
           D_H_Arduino = 3*Resolucion
        elif D_EH == "B" and D_FH == "M" and D_GH == "M":  
           D_H_Arduino = 4*Resolucion
        elif D_EH == "B" and D_FH == "M" and D_GH == "A":  
           D_H_Arduino = 5*Resolucion
        elif D_EH == "B" and D_FH == "A" and D_GH == "B":  
           D_H_Arduino = 6*Resolucion
        elif D_EH == "B" and D_FH == "A" and D_GH == "M":  
           D_H_Arduino = 7*Resolucion
        elif D_EH == "B" and D_FH == "A" and D_GH == "A":  
           D_H_Arduino = 8*Resolucion
        elif D_EH == "A" and D_FH == "B" and D_GH == "B":  
           D_H_Arduino = 9*Resolucion
        elif D_EH == "A" and D_FH == "B" and D_GH == "M":  
           D_H_Arduino = 10*Resolucion
        elif D_EH == "A" and D_FH == "B" and D_GH == "A":
           D_H_Arduino = 11*Resolucion
        elif D_EH == "A" and D_FH == "M" and D_GH == "B":  
           D_H_Arduino = 12*Resolucion
        elif D_EH == "A" and D_FH == "M" and D_GH == "M":  
           D_H_Arduino = 13*Resolucion
        elif D_EH == "A" and D_FH == "M" and D_GH == "A":  
           D_H_Arduino = 14*Resolucion
        elif D_EH == "A" and D_FH == "A" and D_GH == "B":  
           D_H_Arduino = 15*Resolucion
        elif D_EH == "A" and D_FH == "A" and D_GH == "M":  
           D_H_Arduino = 16*Resolucion
        elif D_EH == "A" and D_FH == "A" and D_GH == "A":  
           D_H_Arduino = 17*Resolucion
        #Transmision de la informacion
        pub_H.publish(D_H_Arduino)
        rospy.loginfo(D_H_Arduino)
        rate.sleep() 

if __name__ == '__main__':
	try:
		H()
	except rospy.ROSInterruptException:
		pass
