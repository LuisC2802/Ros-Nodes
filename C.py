#!/usr/bin/env python
# NODO DE VALORES ENTEROS

#Se importan las librerias de ROS y Valores int, float
import rospy
from std_msgs.msg import String	
from std_msgs.msg import Int16
from std_msgs.msg import Float32

#Se declaran variables globales
Data_CF = ""
Bajo = 0
Medio = 0
Alto = 0
Data_Aux = 0

# Funcion de recepcion de los datos Enteros
def callback(data):
    global Data_Aux
    rospy.loginfo(rospy.get_caller_id() + ':I heard %s', data.data)
    Data_Aux = data.data  #Almacenamiento del Int en variable auxiliar	

def C():
    global Data_CF
    global Data_Aux
    global Alto
    global Medio
    global Bajo
    
    #Declaracion del nodo y canales subscriber y publisher
    rospy.init_node('C', anonymous=False)
    rospy.Subscriber('chatter_AC', Int16, callback) 
    pub_C = rospy.Publisher('chatter_CF', String, queue_size=10)   
    
    rate = rospy.Rate(1)  # Frecuencia de 1 Hz
    while not rospy.is_shutdown():
	#Funciones de membresia
    	if Data_Aux >= 0 and Data_Aux <= 100:    
           Bajo = 100.0
	   Medio = 0.0
	   Alto = 0.0
	elif Data_Aux > 100 and Data_Aux <= 150:
           Bajo = -Data_Aux + 200.0
	   Medio = 0.0
	   Alto = 0.0
	elif Data_Aux > 150 and Data_Aux <= 200:
           Bajo = -Data_Aux + 200.0
	   Medio = Data_Aux - 150.0
	   Alto = 0.0
	elif Data_Aux > 200 and Data_Aux <= 250:
           Bajo = 0.0
	   Medio = Data_Aux - 150.0
	   Alto = 0.0
	elif Data_Aux > 250 and Data_Aux <= 300:
           Bajo = 0.0
	   Medio = -Data_Aux + 350.0
	   Alto = 0.0		
	elif Data_Aux > 300 and Data_Aux <= 350:
           Bajo = 0.0
	   Medio = -Data_Aux + 350.0
	   Alto = Data_Aux - 300.0
	elif Data_Aux > 350 and Data_Aux < 400:
           Bajo = 0.0
	   Medio = 0.0
	   Alto = Data_Aux - 300.0
        elif Data_Aux >= 400 and Data_Aux <= 500:
           Bajo = 0.0
	   Medio = 0.0
	   Alto = 100.0
        #Transmision de la informacion
 	Data_CF = "Alto=" + str(Alto) +  "/" + "Medio=" + str(Medio) + "/" + "Bajo=" + str(Bajo)
    	pub_C.publish(Data_CF)	
    	rospy.loginfo(Data_CF)
    	rate.sleep()

	
if __name__ == '__main__':
	try:
		C()
	except rospy.ROSInterruptException:
		pass
