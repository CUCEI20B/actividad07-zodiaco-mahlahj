def signos():
        mes = int(input("mes de nacimiento: " ))
        dia = int(input("dia de nacimiento: " ))

        if ((int(mes)==12 and int(dia) >= 22)or(int(mes)==1 and int(dia)<= 19)):
                signo_zodiacal = ("capricornio")
        elif ((int(mes)==1 and int(dia) >= 20)or(int(mes)==2 and int(dia)<= 17)):
                signo_zodiacal = ("acuario")
        elif ((int(mes)==2 and int(dia) >= 18)or(int(mes)==3 and int(dia)<= 19)):
                signo_zodiacal = ("piscis")
        elif ((int(mes)==3 and int(dia) >= 20)or(int(mes)==4 and int(dia)<= 19)):
                signo_zodiacal = ("aries")
        elif ((int(mes)==4 and int(dia) >= 20)or(int(mes)==5 and int(dia)<= 20)):
                signo_zodiacal = ("tauro")
        elif ((int(mes)==5 and int(dia) >= 21)or(int(mes)==6 and int(dia)<= 20)):
                signo_zodiacal = ("geminis")
        elif ((int(mes)==6 and int(dia) >= 21)or(int(mes)==7 and int(dia)<= 22)):
                signo_zodiacal = ("cancer")
        elif ((int(mes)==7 and int(dia) >= 23)or(int(mes)==8 and int(dia)<= 22)): 
                signo_zodiacal = ("leo")
        elif ((int(mes)==8 and int(dia) >= 23)or(int(mes)==9 and int(dia)<= 22)): 
                signo_zodiacal = ("virgo")
        elif ((int(mes)==9 and int(dia) >= 23)or(int(mes)==10 and int(dia)<= 22)):
                signo_zodiacal = ("libra")
        elif ((int(mes)==10 and int(dia) >= 23)or(int(mes)==11 and int(dia)<= 21)): 
                signo_zodiacal = ("escorpio")
        elif ((int(mes)==11 and int(dia) >= 22)or(int(mes)==12 and int(dia)<= 21)):
                signo_zodiacal = ("sagitario")

        print(signo_zodiacal)
        
signos()