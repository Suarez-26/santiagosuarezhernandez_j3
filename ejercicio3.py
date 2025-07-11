# Programa para calcular las emisiones de CO2 de una oficina

# Datos de consumo de equipos (en Watts)
computadoras = {
    "cantidad": 5,
    "consumo_W": 100,
    "horas_dia": 8
}

impresoras = {
    "cantidad": 2,
    "consumo_W": 250,
    "horas_dia": 2
}

aire_acondicionado = {
    "cantidad": 1,
    "consumo_W": 1500,
    "horas_dia": 6
}

lamparas = {
    "cantidad": 10,
    "consumo_W": 40,
    "horas_dia": 10}

# Factor de emisión y días de funcionamiento
factor_emision = 0.5  # kg CO2e/kWh
dias_anio = 250

# Función para calcular consumo anual (kWh) y emisiones
def calcular_consumo_emision(equipo):
    consumo_kWh = (equipo["cantidad"] * equipo["consumo_W"] * equipo["horas_dia"] * dias_anio) / 1000
    emisiones = consumo_kWh * factor_emision
    return consumo_kWh, emisiones

# Cálculos por equipo
consumo_comp, emision_comp = calcular_consumo_emision(computadoras)
consumo_imp, emision_imp = calcular_consumo_emision(impresoras)
consumo_aire, emision_aire = calcular_consumo_emision(aire_acondicionado)
consumo_lamparas, emision_lamparas = calcular_consumo_emision(lamparas)

# Sumar emisiones totales
emision_total = emision_comp + emision_imp + emision_aire + emision_lamparas

# Mostrar resultados
print(f"Computadoras: {consumo_comp:.2f} kWh/año -> {emision_comp:.2f} kg CO2e/año")
print(f"Impresoras: {consumo_imp:.2f} kWh/año -> {emision_imp:.2f} kg CO2e/año")
print(f"Aire acondicionado: {consumo_aire:.2f} kWh/año -> {emision_aire:.2f} kg CO2e/año")
print(f"Lámparas: {consumo_lamparas:.2f} kWh/año -> {emision_lamparas:.2f} kg CO2e/año")
print(f"\nEmisiones totales: {emision_total:.2f} kg CO2e/año")
