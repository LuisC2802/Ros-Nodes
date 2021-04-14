#!/usr/bin/env python
# NODO DEL BOOLEANO

#Se importan las librerias de ROS y Valores Bool
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool

#Se declaran variables globales
Data_Aux = False
Data_BE = ""

# Funcion de recepcion de los datos Booleanos
def callback(data): 
    global Data_Aux 
    rospy.loginfo(rospy.get_caller_id() + ':I heard %s', data.data)
    Data_Aux = data.data  #Almacenamiento del Bool en variable auxiliar	

def B():
    global Data_Aux
    global Data_BE
    
    #Declaracion del nodo y canales subscriber y publisher
    rospy.init_node('B', anonymous=False)
    rospy.Subscriber('chatter_AB', Bool, callback)
    pub_B = rospy.Publisher('chatter_BE', String, queue_size=10) 
    
    rate = rospy.Rate(1)    # Frecuencia de 1 Hz
    while not rospy.is_shutdown():
 	#Condicion del booleano
    	if Data_Aux == True:
	   Data_BE = "Alto=True/Bajo=False"
	else:
	   Data_BE = "Alto=False/Bajo=True"
        #Transmision de la informacion
    	pub_B.publish(Data_BE)	
    	rospy.loginfo(Data_BE)
    	rate.sleep()

	
if __name__ == '__main__':
	try:
		B()
	except rospy.ROSInterruptException:
		pass
