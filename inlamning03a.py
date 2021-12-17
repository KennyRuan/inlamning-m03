#frågar efter din lön
lön = int(input("ange din månadslön: "))
#variabler
k_skatt = 0.2136
l_skatt = 0.1148


#skriver ut vad du betalar i kommunalskatt, landstingsskatt och i vad du har i månadslön
print("utskrift:")
print("Månadslön", lön, "kr")
print ("kommunalskatt", int(lön * k_skatt), "kr" )
print ("Landstingsskatt", int(lön * l_skatt), "Kr")

#variabler
kvar_efter_skatt1 = lön * l_skatt 
kvar_efter_skatt2 = lön * k_skatt

kvar_efter_skatt3 = kvar_efter_skatt1 + kvar_efter_skatt2
kvar_efter_skatt4 = lön - kvar_efter_skatt3

#skriver ut din lön efter skatt
print ("kvar efter skatt" ,int(kvar_efter_skatt4), "kr" )