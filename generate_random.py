import random

def aleatoriu(lista):
    adresa = random.choices(lista, k=64)
    adresa_str = "".join(str(e) for e in adresa)
    return adresa_str
