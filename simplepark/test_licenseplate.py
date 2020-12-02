'''
    File Name: test_licenseplate.py
    Project Name: SimplePark
    Author: Colin Robbins
    Student Number: 400353539
    Date: 12/02/2020
    Class: SFWRTECH 3RQ3
    Professor: Sean Watson
    Purpose: used to run tests on the licenseplate.py class
'''

from simplepark.licenseplate import LicensePlate

'''
Requirement 3.1.2: Keep Track and Verify License Plate
Testing: Making sure that the license plate is correct and
         within the proper range for Ontarios legal limit
'''
#-----------------------------------------------------------
def test_license_plate_length():
    license_plate = LicensePlate()
    assert len(license_plate) >= 2, "the plate has a minimum of 2 characters"
    
    plateCheck = license_plate.set_plate_number("000000")
    
    assert len(plateCheck) >= 2 and len(plateCheck) <= 8, "the license plate is within a legal range of 2 and 8"
    
def test_license_plate_length_failed():
    license_plate = LicensePlate()
    plateCheck = license_plate.set_plate_number("0")
    assert len(plateCheck) >= 2, "the license plate is less then 2 characters"
    
    plateCheck = license_plate.set_plate_number("0000000000")
    
    assert len(plateCheck) < 2 and len(plateCheck) > 8, "the license plate should not be less then 2 or greater then 8"
#-----------------------------------------------------------