from simplepark.licenseplate import LicensePlate

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
    