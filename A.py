#!/usr/bin/env python
# NODO DE RECEPCION DE ARDUINO

#Se importan las librerias de ROS y Valores Bool, int, float
import rospy	
from std_msgs.msg import String		
from std_msgs.msg import Int16
from std_msgs.msg import Float32
from std_msgs.msg import Bool

#Se declaran variables globales
Data_AB = False
Data_AC = 0
Data_AD = 0

# Funcion de recepcion de los datos Booleanos
def callback_Bool(data_Bool): 
    global Data_AB
    rospy.loginfo(rospy.get_caller_id() + ':I heard %s', data_Bool.data)	
    Data_AB = data_Bool.data  #Almacenamiento del Bool en variable auxiliar

# Funcion de recepcion de los datos Enteros
def callback_Int(data_Int): 
    global Data_AC
    rospy.loginfo(rospy.get_caller_id() + ':I heard %s', data_Int.data)
    Data_AC = data_Int.data  #Almacenamiento del Int en variable auxiliar  

# Funcion de recepcion de los datos Flotantes
def callback_Float(data_Float):
    global Data_AD
    rospy.loginfo(rospy.get_caller_id() + ':I heard %s', data_Float.data) 
    Data_AD = data_Float.data	 #Almacenamiento del Float en variable auxiliar

def A():
    global Data_AB
    global Data_AC
    global Data_AD   

    #Declaracion del nodo y canales subscriber y publisher
    rospy.init_node('A', anonymous=False)
    rospy.Subscriber('chatter_A_Bool', Bool, callback_Bool) 
    rospy.Subscriber('chatter_A_int', Int16, callback_Int) 
    rospy.Subscriber('chatter_A_float', Float32, callback_Float) 
    pub_B = rospy.Publisher('chatter_AB', Bool, queue_size=10)
    pub_C = rospy.Publisher('chatter_AC', Int16, queue_size=10)	
    pub_D = rospy.Publisher('chatter_AD', Float32, queue_size=10)
    
    rate = rospy.Rate(10)    # Frecuencia de 10 Hz
    while not rospy.is_shutdown():
    # Publicar la informacion
    	pub_B.publish(Data_AB)	
    	pub_C.publish(Data_AC)	
    	pub_D.publish(Data_AD)
    	rospy.loginfo(Data_AB)
    	rospy.loginfo(Data_AC)
    	rospy.loginfo(Data_AD)
        rate.sleep() 
	
if __name__ == '__main__':
	try:
		A()
	except rospy.ROSInterruptException:
		pass
