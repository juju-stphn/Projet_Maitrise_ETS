# Permet le deplacement de la canera selon axe x pour intervalle donnee
class Range:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        if self.step>0:
            while self.current < self.stop:
                yield self.current
                self.current += self.step    
        if self.step<0:
            while self.current >= self.stop:
                yield self.current
                self.current += self.step    
            
