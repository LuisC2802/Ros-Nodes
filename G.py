#!/usr/bin/env python
# NODO DEL STRING FLOAT

#Se importan las librerias de ROS
import rospy	
from std_msgs.msg import String		
from std_msgs.msg import Float32

#Se declaran variables globales
Data_GH = ""
Alto=0.0
Medio=0.0
Bajo=0.0
String_Aux = "Alto=0.0/Medio=0.0/Bajo=0.0"
Data_String = String_Aux.split("/")
for i in [0,1,2]:
   Data_Aux = Data_String[i].split("=")
   if Data_Aux[0] == "Alto":
      Alto = float(Data_Aux[1])
   if Data_Aux[0] == "Medio":
      Medio = float(Data_Aux[1])
   if Data_Aux[0] == "Bajo":
      Bajo = float(Data_Aux[1])

# Funcion de recepcion String Float
def callback(data): 
    global Data_String
    rospy.loginfo(rospy.get_caller_id() + ':I heard %s', data.data) 
    Data_String = data.data.split("/")  #Separa la cadena y almacena en variable auxiliar

def G():
    global Data_GH
    global Data_String
    global Data_Aux
    global Alto
    global Medio
    global Bajo

    #Declaracion del nodo y canales subscriber y publisher
    rospy.init_node('G', anonymous=False)
    rospy.Subscriber('chatter_DG', String, callback) 
    pub_G = rospy.Publisher('chatter_GH', String, queue_size=10)

    rate = rospy.Rate(0.5)  # Frecuencia de 0.5 Hz
    while not rospy.is_shutdown():
	#Adquisicion de los datos
        for i in [0,1,2]:
           Data_Aux = Data_String[i].split("=")
           if Data_Aux[0] == "Alto":
              Alto = float(Data_Aux[1])
           elif Data_Aux[0] == "Medio":
              Medio = float(Data_Aux[1])
           elif Data_Aux[0] == "Bajo":
              Bajo = float(Data_Aux[1])
	#Condiciones para el envio del caracter
    	if Alto >= Medio and Alto >= Bajo:    
            Data_GH = "A"
	elif Medio >= Bajo and Medio > Alto:
            Data_GH = "M"
	elif Bajo > Alto and Bajo > Medio:
            Data_GH = "B"
        #Transmision de la informacion
    	pub_G.publish(Data_GH)	
    	rospy.loginfo(Data_GH)
    	rate.sleep()

if __name__ == '__main__':
	try:
		G()
	except rospy.ROSInterruptException:
		pass	
