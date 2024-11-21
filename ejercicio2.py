for i in range(1,5,1):
    import time
    import random
    destinos = ["Bogotá","Barranquilla", "Cali", "Santa Marta","Ibagué"]
    a = random.choice(destinos)
    vuelo = "Su vuelo con destino a {} se encuentra a tiempo."
    vuelo = vuelo.format(a)
    print(vuelo)
    time.sleep(0.5)
    print(vuelo.replace("A tiempo","Retrasado"))
 