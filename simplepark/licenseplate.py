class LicensePlate:
    def __init__(self):
        self.plate = "00"
        
    def __len__(self):
        return len(self.plate)
    
    def set_plate_number(self, plateToSetTo):
        self.plate = plateToSetTo
        return self.plate
        
    def verify_plate_number(self, licensePlateNumber):
        return None