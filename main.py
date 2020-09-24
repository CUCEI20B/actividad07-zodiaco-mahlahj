def signos():
        mes = int(input("mes de nacimiento: " ))
        dia = int(input("dia de nacimiento: " ))

        if (dia >= 20 and mes == 1) or (dia <= 10 and mes == 2):
            signo_zodiacal = ("geminis")
        elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
            signo_zodiacal = ("piscis")
        elif (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
            signo_zodiacal = ("aries")
        elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
            signo_zodiacal = ("tauro")
        elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
            signo_zodiacal = ("acuario")
        elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
            signo_zodiacal = ("cancer")
        elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
            signo_zodiacal = ("leo")
        elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
            signo_zodiacal = ("sagitario")
        elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
            signo_zodiacal = ("libra")
        elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
            signo_zodiacal = ("escorpio")
        elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
            signo_zodiacal = ("virgo")
        elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
            signo_zodiacal = ("capricornio")
        
        print(signo_zodiacal)
        
signos()