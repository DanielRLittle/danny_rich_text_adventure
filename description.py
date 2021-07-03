class Description:
    def __init__(self, description, alive_description = None):
        self.description = description
        self.alive_description = alive_description
    
    def get_description(self, is_alive = False):
        if is_alive and self.alive_description != None:
            return self.alive_description
        return self.description
