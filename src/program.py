def horas_para_minutos(horas):
    if horas < 0:
        raise ValueError("Valor não pode ser negativo")
    return horas * 60

def minutos_para_segundos(minutos):
    if minutos < 0:
        raise ValueError("Valor não pode ser negativo")
    return minutos * 60

def segundos_para_horas(segundos):
    if segundos < 0:
        raise ValueError("Valor não pode ser negativo")
    return segundos / 3600

def dias_para_horas(dias):
    if dias < 0:
        raise ValueError("Valor não pode ser negativo")
    return dias * 24

def horas_para_dias(horas):
    if horas < 0:
        raise ValueError("Valor não pode ser negativo")
    return horas / 24