def calcular_tem(tea:int,cuotas):
    """
    Calcula el tem: `tasa efectiva mensual` a partir de tea: `tasa efectiva anual`
    """
    return round(((1+(tea/100))**(1/cuotas)-1),5)
