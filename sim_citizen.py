
from random import randrange,choice

class Citizen():
    def __init__(self,id_number,
                      community,
                      age,
                      disease):
        
        # Variables por definición
        self.id_number = id_number
        self.community = community
        self.age = age
        self.disease = disease
        self.status = False
        self.inmune = False
        self.infection_date = "Nunca fué infectado"
        self.isAlive = True

        # Variables por Asignación
        self.family = []
        self.affection = "Ninguna"
        self.base_disease = "Ninguna"

    # Infección
    def infect(self,step):
        self.inmune = True
        self.status = True
        self.disease.add_case()
        self.infection_date = "Fue infectado en el paso <span foreground='Firebrick 2'>"+str(step)+"</span>"

    # Setters & Getters
    def is_inmune(self):
        return self.inmune

    def set_affection(self):
        self.affection = choice(["Asma","Enfermedad cerebrovascular","Fibrosis Quistica","Hipertension"])
    
    def set_base_disease(self):
        self.affection = choice(["Obesidad","Desnutrición"])

    def get_id_number(self):
        return self.id_number