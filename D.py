#!/usr/bin/env python
# NODO DE VALORES FLOTANTES

#Se importan las librerias de ROS y Valores float
import rospy	
from std_msgs.msg import String	
from std_msgs.msg import Float32	

#Se declaran variables globales
Data_DG = ""
Bajo = 0.0
Medio = 0.0
Alto = 0.0
Data_Aux = 0.0

# Funcion de recepcion de los datos Flotantes
def callback(data):
    global Data_Aux 
    rospy.loginfo(rospy.get_caller_id() + ':I heard %s', data.data)
    Data_Aux = data.data   #Almacenamiento del Float en variable auxiliar	 

def D():
    global Data_DG
    global Data_Aux
    global Alto
    global Medio
    global Bajo

    #Declaracion del nodo y canales subscriber y publisher
    rospy.init_node('D', anonymous=False)
    rospy.Subscriber('chatter_AD', Float32, callback)
    pub_D = rospy.Publisher('chatter_DG', String, queue_size=10) 

    rate = rospy.Rate(1)   # Frecuencia de 1 Hz
    while not rospy.is_shutdown():
	#Funciones de membresia
    	if Data_Aux >= 0 and Data_Aux <= 100.0:    
           Bajo = 100.0
	   Medio = 0.0
	   Alto = 0.0
	elif Data_Aux > 100.0 and Data_Aux <= 150.0:
           Bajo = -Data_Aux + 200
	   Medio = 0.0
	   Alto = 0.0
	elif Data_Aux > 150.0 and Data_Aux <= 200.0:
           Bajo = -Data_Aux + 200.0
	   Medio = Data_Aux - 150.0
	   Alto = 0.0
	elif Data_Aux > 200 and Data_Aux <= 250:
           Bajo = 0.0
	   Medio = Data_Aux - 150.0
	   Alto = 0.0
	elif Data_Aux > 250.0 and Data_Aux <= 300.0:
           Bajo = 0.0
	   Medio = -Data_Aux + 350.0
	   Alto = 0.0
	elif Data_Aux > 300.0 and Data_Aux <= 350.0:
           Bajo = 0.0
	   Medio = -Data_Aux + 350.0
	   Alto = Data_Aux - 300.0
	elif Data_Aux > 350.0 and Data_Aux < 400.0:
           Bajo = 0.0
	   Medio = 0.0
	   Alto = Data_Aux - 300
        elif Data_Aux >= 400.0 and Data_Aux <= 500.0:
           Bajo = 0.0
	   Medio = 0.0
	   Alto = 100.0
        #Transmision de la informacion
 	Data_DG = "Alto=" + str(Alto) +  "/" + "Medio=" + str(Medio) + "/" + "Bajo=" + str(Bajo)	
    	pub_D.publish(Data_DG)	
    	rospy.loginfo(Data_DG)
    	rate.sleep()

	
if __name__ == '__main__':
	try:
		D()
	except rospy.ROSInterruptException:
		pass	
