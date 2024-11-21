def km_m(kmh):
    m_mk = 1000
    s_h = 3600
    m_s = (kmh*m_mk)/s_h
    return m_s
v = float(input("Por favor ingrese la velocidad en kilómetros por segundo km/s: "))
print("La velocidad en metros por segundo m/s es de: ", km_m(v))