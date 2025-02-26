class Resturant:
    """information about resturant"""
    
    def __init__(self, resturant_name, cuisine_type):
        """returning resturent info"""
        self.resturent_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_resturent(self):
        print(f"Our resturent name is {self.resturent_name} ")
        print(f'We best in making {self.cuisine_type}')
    
    def open_resturent(self):
        print(f"our restrnt is open")

    def set_number_served(self, number):
        """Setting a new value to a number served"""
        update = self.number_served
        return update
resturant = Resturant("om bhole", 'java')
resturant.describe_resturent()
resturant.open_resturent()
print(resturant.number_served)

