class Disease():
    def __init__(self, probInfection,
                       duration,
                       infectionType,
                       vulnerable):
        
        self.probInfection = probInfection
        self.duration = duration
        self.infectionType = infectionType
        self.vulnerable = vulnerable

        self.cases = 0
        
    # Fun - Añadir caso
    def add_case(self):
        self.cases += 1

    def isVulnerable(self,citizen):
        pass

    """ GETTERS """
    def get_prob(self):
        return self.probInfection
    
    def get_stepsEvolution(self):
        return self.duration

    def get_cases(self):
        return self.cases