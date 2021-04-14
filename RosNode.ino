/*
 * rosserial Publisher Example
 * Prints "hello world!"
 */
//Se incluyen las librerias de Ros y Los mensajes
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Bool.h>

// Se declaran las variables a implementar
const int Pin_Bool = 2;
const int PWM_Pin = 6;
float msg_rec = 0;
ros::NodeHandle  nh;
int cont = 1;
bool sensor_Bool = false;
int sensor_Int = 0;
float sensor_Float = 0.0;

// Funcion de recepcion
void callback_ros( std_msgs::Float32& Vel_msg){
  msg_rec = Vel_msg.data;
}

std_msgs::Bool msg_Bool;
std_msgs::Int16 msg_Int;
std_msgs::Float32 msg_Float;

// Inicializacion de los canales de comunicacion
ros::Publisher chatter_A_Bool("chatter_A_Bool", &msg_Bool);
ros::Publisher chatter_A_int("chatter_A_int", &msg_Int);
ros::Publisher chatter_A_float("chatter_A_float", &msg_Float);
ros::Subscriber<std_msgs::Float32> chatter_H_Arduino("chatter_H_Arduino", callback_ros);

void setup()
{
  //Configuracion del nodo
  pinMode(Pin_Bool, INPUT);
  pinMode(PWM_Pin, OUTPUT);
  nh.initNode();
  nh.advertise(chatter_A_Bool);
  nh.advertise(chatter_A_int);
  nh.advertise(chatter_A_float);
  nh.subscribe(chatter_H_Arduino);
}

void loop()
{
  //Condicion de transmision de la informacion
  if (cont == 5){
  sensor_Bool = digitalRead(Pin_Bool);
  sensor_Int = (analogRead(A0)/2 + sensor_Int)/5;
  sensor_Float = (analogRead(A1)*5.00/10.23 + sensor_Float)/5.0;  
  msg_Bool.data = sensor_Bool;
  msg_Int.data = sensor_Int;
  msg_Float.data = sensor_Float;
  chatter_A_Bool.publish( &msg_Bool );
  chatter_A_int.publish( &msg_Int );
  chatter_A_float.publish( &msg_Float ); 
  cont = 1;
  sensor_Int = 0;
  sensor_Float = 0.0;
}
  else{
  sensor_Int = analogRead(A0)/2 + sensor_Int;
  sensor_Float = analogRead(A1)*5.00/10.23 + sensor_Float; 
  cont = cont + 1;
}
 //Escritura del valor de PWM
  analogWrite(PWM_Pin,int(msg_rec));
  nh.spinOnce();
  delay(100);
}
