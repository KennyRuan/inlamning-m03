#frågar om din lön
lön = int(input("ange din månadslön: "))
#variabler
k_skatt = 0.2136
l_skatt = 0.1148
Årslön = lön * 12
s_skatt = 0.25

print("utskrift:")
print("Månadslön", lön, "kr", "(årslön:", Årslön, "kr)" )

# om lönen är mindre än 19257 så betalas ingen skatt
if Årslön < 19257:
    print("ingen skatt betalas")

#om lönen är något annat så kommer du behöva betala skatt
else:
    print ("kommunalskatt", int(lön * k_skatt), "kr" )
    print ("Landstingsskatt", int(lön * l_skatt), "Kr")
#om årslönen är 469700 eller mer så betalas statlig skatt
if Årslön > 468700:
        print("statlig skatt", int(lön * s_skatt), "kr")

#variabler
kvar_efter_skatt1 = lön * l_skatt 
kvar_efter_skatt2 = lön * k_skatt
kvar_efter_skatt3 = lön * s_skatt

kvar_efter_skatt4 = kvar_efter_skatt1 + kvar_efter_skatt2 + kvar_efter_skatt3
kvar_efter_skatt5 = lön - kvar_efter_skatt4


#skriver ut vad du har efter skatt
if lön < 19247:
    print("kvar efter skatt", int(lön) ,"kr")

else:
    print ("kvar efter skatt" ,int(kvar_efter_skatt4), "kr" )

