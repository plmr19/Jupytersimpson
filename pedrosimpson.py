#!/usr/bin/env python
# coding: utf-8

# In[ ]:


atemáticas de importación

def  f ( x ): 
    z = ( x ** 2 ) * ( math . exp ( x )) 
    devuelve  z
 
print ( "=============================================== == " ) 
print ( " Cálculo numérico de la regla del simpson " ) 
print ( " =============================== ================== " )




n = int ( input ( "Dame el número de segmentos:" )) 
a = float ( input ( "Dame el valor del límite inferior:" )) 
b = float ( input ( "Dame el valor del límite superior:" ))

print ( "----------------------------------------------- ------------------------------------------------ " ) 
print ( " {0:> 10s} {1:> 20s} {2:> 20s} " . format ( "n" ,  "integral" ,  "et" )) 
print ( "--------- -------------------------------------------------- ------------------------------------ " )

vv =  98.4276

h  =  ( b - a ) / n
 

para  j  en el  rango  ( n ):  
    suma  =  f ( a ) 
    h  =  ( b - a ) / ( j + 1 ) 
    para  i  en el  rango  ( 1 , j , 2 )  : 
        xi = a  +  ( i * h ) 
        suma  =  suma  +  ( 4  *  f ( xi ))  + ( 2  *  f ( xi + h ))
        
        
    sum  =  sum  +  ( 4  *  f ( b - h ))  +  f ( b ) 
    sum  =  h  *  sum / 3 
    et = abs (( vv - sum ) / vv ) * 100 
    print ( " {0: 10d} {1 : 20.9f} {2: 20.9f} " . Formato ( j + 1 ,  suma  ,  et ))
    


print ( "----------------------------------------------- ----------------------------------------------- " )

