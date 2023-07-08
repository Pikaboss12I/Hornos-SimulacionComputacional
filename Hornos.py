from random import randint

#Tiempos dados
simulacion=300 #5 horas 300 minutos
tiempoensamble=30


#Se generá unos tiempos de llegada iniciales aleatorios para empezar la simulación
def tiempoLlegada(tam):
    tllegada=[]
    #Se tendrá en un inicio 10 tiempos de maquinas ensambladoras, simulando que ya estaban ensamblando componentes antes
    for _ in range (tam):
        tllegada.append(randint(1,35))
    tllegada.sort()
    return tllegada

def simulacion (enfriar,tam):
    #Se maneja una lista para los tiempos en que cada ensambladora llegará con piezas listas para el horno
    
    servicioH=0;cola=0;t=1;tf=2;horneados=0;colamax=0;ensamblados=tam;tiempoTH=0
    tllegada=tiempoLlegada(tam)

    #manejar caso base y primera variante
    if enfriar == False and t==1:
        tiempohorno=8
    elif enfriar == True and t==1:
        tiempohorno=13
    #Tiempo que se simulará: 300 minutos
    while(t<=300):
        #print("---------------Tiempo llegada evaluado: "+str(t)+"---------------")
        #Se verifica si el horno estaba horneando y si hay algo esperando por ser horneado
        if servicioH==0 and cola>0:
            
            servicioH=randint(tiempohorno-2,tiempohorno+2)
            if t+servicioH<=300:
                horneados+=1
                tiempoTH+=servicioH
                #print("Tiempo que tomará siguiente horneado:"+str(servicioH))
                cola-=1
        #Verificación si una pieza llegará en ese tiempo
        if t==tllegada[0]:

            #Si el horno se encuentra ocupado
            if servicioH != 0:
                
                #Se generará un nuevo tiempo de ensamblado
                ensamblados+=1
                ensamble=randint(tiempoensamble-5,tiempoensamble+5)
                #print("El ensamblado se demora:"+str(ensamble))
                tllegada.append(t+ensamble)
                tllegada.sort()
                cola+=1
                #Se valida si dos maquinas llegarán en el mismo tiempo
                if t==tllegada[0]==tllegada[1]:
                    t-=1
                tllegada.pop(0)
                #Se lleva un control de la cola maxima para el analisis de resultados    
                if(colamax<cola):
                    colamax=cola
  
            #Si el horno se encuentra desocupado
            else:
                ensamblados+=1
                ensamble=randint(tiempoensamble-5,tiempoensamble+5)
                #print("El ensamblado se demora:"+str(ensamble))
                tllegada.append(t+ensamble)
                tllegada.sort()
                #Se valida si dos maquinas llegarán en el mismo tiempo
                if t==tllegada[0]==tllegada[1]:
                    t-=1
                tllegada.pop(0)
                servicioH=randint(tiempohorno-2,tiempohorno+2)
                if t+servicioH<=300:
                    horneados+=1
                    tiempoTH+=servicioH
                    #print("Tiempo que tomará siguiente horneado:"+str(servicioH))
                    if cola>0:
                        cola-=1
        #Se va disminuyendo el tiempo de horneado al pasar un minuto
        if t==tf-1:
            tf+=1
            if servicioH>0:
                servicioH-=1
        t+=1
        
    

#Se da el formato para que el porcentaje quede unicamente con un numero decimal
    porcentaje= "{:.1f}".format(((tiempoTH/300)*100))
    print("El numero de piezas que se pudieron hornear fueron: "+str(horneados))
    print("La cola maxima fue: "+str(colamax))
    print("Se ensamblaron: "+str(ensamblados)+ " piezas")
    print("Tiempo ocupación horno: "+str(tiempoTH)+ " minutos")
    print("Porcentaje: "+str(porcentaje)+"%")

#Se tienen 2 hornos
def simulacionv2 (tam):
    #Se maneja una lista para los tiempos en que cada ensambladora llegará con piezas listas para el horno
    tiempohorno=13
    servicioH=0;servicioH2=0;cola=0;t=1;tf=2;horneados=0;colamax=0;ensamblados=tam;tiempoTH=0;tiempoTH2=0
    tllegada=tiempoLlegada(tam)

    #Tiempo que se simulará: 300 minutos
    while(t<=300):
        #print("---------------Tiempo llegada evaluado: "+str(t)+"---------------")

        #Se verifica si los hornos estaban horneando y si hay algo esperando por ser horneado
        if servicioH==0 and cola>0:
            #print("Quedan piezas por hornear, seguire trabajando")
            servicioH=randint(tiempohorno-2,tiempohorno+2)
            if t+servicioH<=300:
                horneados+=1
                tiempoTH+=servicioH
                #print("Tiempo que tomará siguiente horneado en el horno 1:"+str(servicioH))
                cola-=1

        if servicioH2==0 and cola>0:
            #print("Quedan piezas por hornear, seguire trabajando")
            servicioH2=randint(tiempohorno-2,tiempohorno+2)
            if t+servicioH2<=300:
                horneados+=1
                tiempoTH2+=servicioH2
                #print("Tiempo que tomará siguiente horneado en el horno 2:"+str(servicioH2))
                cola-=1

        
        #Verificación si una pieza llegará en ese tiempo
        if t==tllegada[0]:
            
            #Si ambos hornos se encuentran ocupado
            if servicioH != 0 and servicioH2!=0:
                
                #Se generará un nuevo tiempo de ensamblado
                ensamblados+=1
                ensamble=randint(tiempoensamble-5,tiempoensamble+5)
                #print("El ensamblado se demora:"+str(ensamble))
                tllegada.append(t+ensamble)
                tllegada.sort()
                cola+=1
                #Se valida si dos maquinas llegarán en el mismo tiempo
                if t==tllegada[0]==tllegada[1]:
                    t-=1
                tllegada.pop(0)
                #Se lleva un control de la cola maxima para el analisis de resultados    
                if(colamax<cola):
                    colamax=cola

            #Si alguno de los hornos se encuentra desocupado
            elif servicioH ==0 or servicioH2==0:
                ensamblados+=1
                ensamble=randint(tiempoensamble-5,tiempoensamble+5)
                #print("El ensamblado se demora:"+str(ensamble))
                tllegada.append(t+ensamble)
                tllegada.sort()
                #Se valida si dos maquinas llegarán en el mismo tiempo
                if t==tllegada[0]==tllegada[1]:
                    t-=1
                tllegada.pop(0)
                if servicioH == 0:
                    servicioH=randint(tiempohorno-2,tiempohorno+2)
                    if t+servicioH<=300:
                        horneados+=1
                        tiempoTH+=servicioH
                        #print("Tiempo que tomará siguiente horneado en el horno 1:"+str(servicioH))
                        if cola>0:
                            cola-=1
                else: 
                    servicioH2=randint(tiempohorno-2,tiempohorno+2)
                    if t+servicioH2<=300:
                        horneados+=1
                        tiempoTH2+=servicioH2
                        #print("Tiempo que tomará siguiente horneado en el horno 2:"+str(servicioH2))
                        if cola>0:
                            cola-=1
        #Se va disminuyendo el tiempo de horneado al pasar un minuto
        if t==tf-1:
            tf+=1
            if servicioH>0:
                servicioH-=1
            if servicioH2>0:
                servicioH2-=1      
        t+=1
    

    #Se da el formato para que el porcentaje quede unicamente con un numero decimal
    porcentajeh1= "{:.1f}".format(((tiempoTH/300)*100))
    porcentajeh2= "{:.1f}".format(((tiempoTH2/300)*100))
    print("El numero de piezas que se pudieron hornear fueron: "+str(horneados))
    print("La cola maxima fue: "+str(colamax))
    print("Se ensamblaron: "+str(ensamblados)+ " piezas")
    print("Tiempo ocupación del horno 1: "+str(tiempoTH)+ " minutos")
    print("Tiempo ocupación del horno 2: "+str(tiempoTH)+ " minutos")
    print("Porcentaje horno 1: "+str(porcentajeh1)+"%")
    print("Porcentaje horno 2: "+str(porcentajeh2)+"%")

#Caben 10 piezas
def simulacionv3 (tam):
    #Se maneja una lista para los tiempos en que cada ensambladora llegará con piezas listas para el horno
    tiempohorno=8
    servicioH=[0,0,0,0,0,0,0,0,0,0];cola=0;t=1;tf=2;horneados=0;colamax=0;ensamblados=tam;tiempoTH=0;flag=0
    tllegada=tiempoLlegada(tam)
 
    #Tiempo que se simulará: 300 minutos
    while(t<=300):
        #print("---------------Tiempo llegada evaluado: "+str(t)+"---------------")
        #Se verifica si el horno estaba horneando y si hay algo esperando por ser horneado
        for i in range (10):
            if servicioH[i]==0 and cola>0:
                servicioH[i]=randint(tiempohorno-2,tiempohorno+2)
                if t+servicioH[i]<=300:
                    horneados+=1
                    tiempoTH+=servicioH[i]
                    #print("Tiempo que tomará siguiente horneado:"+str(servicioH[i]))
                    cola-=1
  
        #Verificación si una pieza llegará en ese tiempo
        if t==tllegada[0]:

            for i in range (10):
                if servicioH[i]==0:
                    flag=0
                    break
            #Si el horno se encuentra ocupado (esta horneando 10 piezas)
            if flag ==1:
                
                #Se generará un nuevo tiempo de ensamblado
                ensamblados+=1
                ensamble=randint(tiempoensamble-5,tiempoensamble+5)
                #print("El ensamblado se demora:"+str(ensamble))
                tllegada.append(t+ensamble)
                tllegada.sort()
                cola+=1
                #Se valida si dos maquinas llegarán en el mismo tiempo
                if t==tllegada[0]==tllegada[1]:
                    t-=1
                tllegada.pop(0)
                #Se lleva un control de la cola maxima para el analisis de resultados    
                if(colamax<cola):
                    colamax=cola
  
            #Si el horno se encuentra desocupado
            else:
                #Se verifica que slot esta disponible
                for i in range (10):
                    if servicioH[i]==0:
                        ensamblados+=1
                        ensamble=randint(tiempoensamble-5,tiempoensamble+5)
                        #print("El ensamblado se demora:"+str(ensamble))
                        tllegada.append(t+ensamble)
                        tllegada.sort()
                        #Se valida si dos maquinas llegarán en el mismo tiempo
                        if t==tllegada[0]==tllegada[1]:
                            t-=1
                        tllegada.pop(0)
                        #Se comieza a contabilizar el tiempo de esa pieza en el slot
                        servicioH[i]=randint(tiempohorno-2,tiempohorno+2)
                        if t+servicioH[i]<=300:
                            horneados+=1
                            tiempoTH+=servicioH[i]
                            #print("Tiempo que tomará siguiente horneado:"+str(servicioH))
                            flag=1
                            if cola>0:
                                cola-=1
                            break
        #Se va disminuyendo el tiempo de horneado al pasar un minuto
        if t==tf-1:
            tf+=1
            for i in range (10):
                if servicioH[i]>0:
                    servicioH[i]-=1
        t+=1
    

#Se da el formato para que el porcentaje quede unicamente con un numero decimal
    tiempoTH=tiempoTH/10
    porcentaje= "{:.1f}".format(((tiempoTH/300)*100))
    print("El numero de piezas que se pudieron hornear fueron: "+str(horneados))
    print("La cola maxima fue: "+str(colamax))
    print("Se ensamblaron: "+str(ensamblados)+ " piezas")
    print("Tiempo ocupación horno: "+str(tiempoTH)+ " minutos")
    print("Porcentaje promedio de los 10 hornos: "+str(porcentaje)+"%")

#Bloqueo de maquinas, colamax 4
def simulacionv4 (tam):
    #Se maneja una lista para los tiempos en que cada ensambladora llegará con piezas listas para el horno
    tiempohorno=8
    servicioH=0;cola=0;t=1;tf=2;horneados=0;colamax=0;ensamblados=tam;tiempoTH=0;flag=0
    tllegada=tiempoLlegada(tam)
    
    #Tiempo que se simulará: 300 minutos
    while(t<=300):
        #print("---------------Tiempo llegada evaluado: "+str(t)+"---------------")
        #Se verifica si el horno estaba horneando y si hay algo esperando por ser horneado
        if servicioH==0 and cola>0:
            
            servicioH=randint(tiempohorno-2,tiempohorno+2)
            if t+servicioH<=300:
                horneados+=1
                tiempoTH+=servicioH
                #print("Tiempo que tomará siguiente horneado:"+str(servicioH))
                cola-=1
        #Verificación si una pieza llegará en ese tiempo
        if t==tllegada[0]:

            #Si el horno se encuentra ocupado
            if servicioH != 0:
                if t==tllegada[0]==tllegada[1]:
                    t-=1
                    flag+=1
                if cola<4:
                    #Se generará un nuevo tiempo de ensamblado
                    ensamblados+=1
                    ensamble=randint(tiempoensamble-5,tiempoensamble+5)
                    #print("El ensamblado se demora:"+str(ensamble))
                    if flag >0:
                        tllegada.append(t+1+ensamble)
                        tllegada.sort()
                        flag=0
                    else:
                        tllegada.append(t+ensamble)
                        tllegada.sort()
                    cola+=1

                    #Se lleva un control de la cola maxima para el analisis de resultados    
                    if(colamax<cola):
                        colamax=cola
                    #Se valida si dos maquinas llegarán en el mismo tiempo
                    tllegada.pop(0)
                else:
                    #Si no se pudo agregar a la cola entonces la maquina queda bloqueada y debe esperar el horneado que le falte
                    tllegada[0]+=servicioH
                    tllegada.sort()
  
            #Si el horno se encuentra desocupado
            else:
                if cola<4:
                    ensamblados+=1
                    ensamble=randint(tiempoensamble-5,tiempoensamble+5)
                    #print("El ensamblado se demora:"+str(ensamble))
                    tllegada.append(t+ensamble)
                    tllegada.sort()
                    #Se valida si dos maquinas llegarán en el mismo tiempo
                    if t==tllegada[0]==tllegada[1]:
                        t-=1
                    tllegada.pop(0)
                    servicioH=randint(tiempohorno-2,tiempohorno+2)
                    if t+servicioH<=300:
                        horneados+=1
                        tiempoTH+=servicioH
                        #print("Tiempo que tomará siguiente horneado:"+str(servicioH))
                        if cola>0:
                            cola-=1
                else:
                    tllegada[0]+=servicioH
                    tllegada.sort()
        #Se va disminuyendo el tiempo de horneado al pasar un minuto
        if t==tf-1:
            tf+=1
            if servicioH>0:
                servicioH-=1
        t+=1
        

#Se da el formato para que el porcentaje quede unicamente con un numero decimal
    porcentaje= "{:.1f}".format(((tiempoTH/300)*100))
    print("El numero de piezas que se pudieron hornear fueron: "+str(horneados))
    print("La cola maxima fue: "+str(colamax))
    print("Se ensamblaron: "+str(ensamblados)+ " piezas")
    print("Tiempo ocupación horno: "+str(tiempoTH)+ " minutos")
    print("Porcentaje: "+str(porcentaje)+"%")



while True:
    print("\nBienvenido al menú de proceso de manufactura. Selecciona una opción:\n\n")
    print("1. Simulación inicial")
    print("2. Enfriar piezas 5 minutos")
    print("3. Se tienen 2 hornos")
    print("4. Caben 10 piezas en el horno")
    print("5. 4 piezas máximo en cola, bloqueo máquinas")
    print("6. Salir")

    seleccion = input("\nIngrese que metodo quiere realizar: \n")
    tamano = input("Ingrese cuantas maquinas ensambladoras quiere: \n")

    if seleccion == "1":
        simulacion(False,int(tamano))
    elif seleccion == "2":
        simulacion(True,int(tamano))
    elif seleccion == "3":
        simulacionv2(int(tamano))
    elif seleccion == "4":
        simulacionv3(int(tamano))
    elif seleccion == "5":
        simulacionv4(int(tamano))
    elif seleccion == "6":
        print("Un gusto, vuelve pronto")
        exit()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")