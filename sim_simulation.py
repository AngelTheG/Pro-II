

class Simulation():
    def __init__(self,community,core):
        self.community = community
        self.core = core
    
    def run(self,steps):
        for i in range(int(steps)):
            self.core.newStatus(("Simulando paso <span foreground='yellow'>"+str(i+1)+"</span>"))
            self.community.take_step()
        
        self.community.show_population()

    def get_log(self):
        return self.community.get_log()