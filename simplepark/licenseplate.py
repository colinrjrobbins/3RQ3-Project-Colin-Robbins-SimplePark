'''
    File Name: licensplate.py
    Project Name: SimplePark
    Author: Colin Robbins
    Student Number: 400353539
    Date: 12/02/2020
    Class: SFWRTECH 3RQ3
    Professor: Sean Watson
    Purpose: To give Pytest a simple LicensePlate class to test with
'''

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