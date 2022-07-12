
from random import randrange,choice
from sim_citizen import Citizen

class Community():
    def __init__(self,
                 name,
                 population,
                 contactProm,
                 contactProb,
                 minFam,
                 maxFam,
                 initialInfected,
                 disease,
                 core):

        # Variables por definición
        self.name = name
        self.population = population
        self.contactProm = contactProm
        self.contactProb = contactProb
        self.minFam = minFam
        self.maxFam = maxFam
        self.initialInfected = initialInfected

        self.disease = disease

        self.core = core

        # Variables por asignación
        self.citizens = []
        self.citizens_disease = []
        self.citizens_affection = []
        self.log = []
        self.step = 0

        # Generar población
        self.core.newStatus("<span foreground='Chartreuse'>Generando Población</span>")
            
        for id_number in range(self.population):

            age = choice(["Niño","Adolecente","Adulto","Adulto Mayor"])
            self.citizens.append(Citizen(id_number,
                                         self,
                                         age,
                                         self.disease))

        # Asignar enfermedades base
        self.core.newStatus("<span foreground='Chartreuse'>Generando Población con enfermerdad base</span>")
        
        while len(self.citizens_disease) != int(self.population/4):
            target_citizen = choice(self.citizens)
            if not target_citizen in self.citizens_disease:
                target_citizen.set_base_disease()
                self.citizens_disease.append(target_citizen)
        
        # Asignar afeccion
        self.core.newStatus("<span foreground='Chartreuse'>Generando Población con afección</span>")

        while len(self.citizens_affection) != int(self.population*0.65):
            target_citizen = choice(self.citizens)
            if not target_citizen in self.citizens_affection:
                target_citizen.set_affection()
                self.citizens_affection.append(target_citizen)

        # Asignar pacientes 0
        self.core.newStatus("<span foreground='Firebrick 2'>Infectando Población</span>")
        
        while self.disease.get_cases() != self.initialInfected:
            target_citizen = choice(self.citizens)
            if not target_citizen.is_inmune():
                target_citizen.infect(step=0)

        self.core.newStatus("<span foreground='Chartreuse'>Población Correctamente Generada</span>")

    def show_population(self):
        self.core.load_citizen_data(self.citizens)

    def take_step(self):
        pass
    
    def get_log(self):
        return self.log
