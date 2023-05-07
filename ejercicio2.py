import random

def asignar_recursos(tipo, planeta_destino, general):
    vehiculos = {
        "contencion": ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"],
        "ataque": ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]
    }

    alta_prioridad = general in ["Palpatine", "Darth Vader"] 
    
    if alta_prioridad:
        return {"tipo": tipo, "planeta": planeta_destino, "general": general, "prioridad": "alta", "recursos": "manual"}
    else:
        recursos = {}
        if tipo == "exploracion":
            recursos = {"Scout Troopers": 15, "speeder bike": 2}
        elif tipo == "contencion":
            recursos = {"Stormtroopers": 30, "vehiculos": [random.choice(vehiculos["contencion"]) for _ in range(3)]}
        elif tipo == "ataque":
            recursos = {"Stormtroopers": 50, "vehiculos": [random.choice(vehiculos["ataque"]) for _ in range(7)]}
        
        return {"tipo": tipo, "planeta": planeta_destino, "general": general, "prioridad": "baja", "recursos": recursos}

def mostrar_recursos(misiones):
    for mision in misiones:
        print(f"Misión de {mision['tipo']} en el planeta {mision['planeta']} solicitada por el general {mision['general']}:")
        print(f"Prioridad: {mision['prioridad']}")
        print(f"Recursos asignados: {mision['recursos']}")
        print()

def main():
    misiones = [] #Lista de misiones
    misiones.append(asignar_recursos("exploracion", "Hoth", "Darth Vader")) #Agregamos las misiones a la lista
    misiones.append(asignar_recursos("contencion", "Endor", "Palpatine")) 
    misiones.append(asignar_recursos("ataque", "Yavin IV", "Darth Vader"))
    misiones.append(asignar_recursos("contencion", "Dagobah", "Tarkin"))
    misiones.append(asignar_recursos("ataque", "Kashyyyk", "Tarkin"))
    misiones.append(asignar_recursos("exploracion", "Mustafar", "Tarkin"))
    misiones.append(asignar_recursos("exploracion", "Dantooine", "Palpatine"))
    misiones.append(asignar_recursos("contencion", "Geonosis", "Tarkin"))
    misiones.append(asignar_recursos("ataque", "Naboo", "Darth Vader"))
    misiones.append(asignar_recursos("contencion", "Kamino", "Tarkin"))
    misiones.append(asignar_recursos("ataque", "Coruscant", "Palpatine"))
    misiones.append(asignar_recursos("exploracion", "Tatooine", "Darth Vader"))
    misiones.append(asignar_recursos("exploracion", "Lothal", "Tarkin"))
    misiones.append(asignar_recursos("contencion", "Jakku", "Palpatine"))
    misiones.append(asignar_recursos("ataque", "Scarif", "Tarkin"))
    misiones.append(asignar_recursos("contencion", "Bespin", "Darth Vader"))
    misiones.append(asignar_recursos("ataque", "Alderaan", "Palpatine"))
    misiones.append(asignar_recursos("exploracion", "Kessel", "Tarkin"))
    misiones.append(asignar_recursos("exploracion", "Mandalore", "Darth Vader"))
    misiones.append(asignar_recursos("contencion", "Starkiller", "Palpatine"))
    
    mostrar_recursos(misiones)

if __name__ == "__main__":
    main()
