#!/usr/bin/env python
# NODO DEL STRING BOOLEANO

#Se importan las librerias de ROS
import rospy	
from std_msgs.msg import String		

#Se declaran variables globales
Data_EH = ""
Data_Aux = ""
String_Aux = "Alto=False/Bajo=True"
Data_String = String_Aux.split("/")
#Adquisicion de los datos
for i in [0,1]:
   Data_Aux = Data_String[i].split("=")
   if Data_Aux[0] == "Alto":
      Alto = Data_Aux[1]
   if Data_Aux[0] == "Bajo":
      Bajo = Data_Aux[1]

# Funcion de recepcion String Bool
def callback(data):
    global Data_String 
    rospy.loginfo(rospy.get_caller_id() + ':I heard %s', data.data)
    Data_String = data.data.split("/")   #Almacenamiento del Bool en variable auxiliar

def E():
    global Data_EH
    global Data_Aux
    global Data_String 

    #Declaracion del nodo y canales subscriber y publisher
    rospy.init_node('E', anonymous=False)
    rospy.Subscriber('chatter_BE', String, callback)
    pub_E = rospy.Publisher('chatter_EH', String, queue_size=10) 

    rate = rospy.Rate(0.5)  # Frecuencia de 0.5 Hz
    while not rospy.is_shutdown():
	#Adquisicion de los datos
        for i in [0,1]:
           Data_Aux = Data_String[i].split("=")
           if Data_Aux[0] == "Alto":
              Alto = Data_Aux[1]
           elif Data_Aux[0] == "Bajo":
              Bajo = Data_Aux[1]
	#Condicion del string
    	if Alto == "True" and Bajo == "False":    
            Data_EH = "A"
	else:
	    Data_EH = "B"
        #Transmision de la informacion	
    	pub_E.publish(Data_EH)	
    	rospy.loginfo(Data_EH)
    	rate.sleep()

if __name__ == '__main__':
	try:
		E()
	except rospy.ROSInterruptException:
		pass	
