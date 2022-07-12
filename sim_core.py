
from sim_community import Community
from sim_disease import Disease
from sim_simulation import Simulation

class SimulatorCore():
    def __init__(self,core,steps):
        
        # Actualizar el estado
        core.newStatus("<span foreground='yellow'>Iniciando simulación</span>")

        # Creación de la enfermedad
        disease = Disease(int(core.simulation_parameters[7]),
                          int(core.simulation_parameters[8]),
                          int(core.simulation_parameters[9]),
                          int(core.simulation_parameters[10]))

        # Creación de la comunidad
        community = Community(core.simulation_parameters[0],
                              int(core.simulation_parameters[1]),
                              int(core.simulation_parameters[2]),
                              int(core.simulation_parameters[3]),
                              int(core.simulation_parameters[4]),
                              int(core.simulation_parameters[5]),
                              int(core.simulation_parameters[6]),
                              disease,
                              core)

        # Creación de la simulación
        self.simulation = Simulation(community,
                                core)

        self.simulation.run(steps)

        core.newStatus("<span foreground='Chartreuse'>Mostrando Resultados</span>")

    # Recuperar datos de la simulación
    def get_log(self):
        self.simulation.get_log()
        