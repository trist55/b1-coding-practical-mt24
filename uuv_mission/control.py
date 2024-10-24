class Controller:
    def __init__(self):

        self.K_p = 0.15
        self.K_d = 0.6
        
    def calculate_error(self, reference, depth):
        
        error = reference - depth
        return error
    
    def PD_controller(self, reference, depth, error_previous):
        error_current = Controller.calculate_error(self, reference, depth)
        action = self.K_p * error_current + self.K_d * (error_current - error_previous)
        return action
