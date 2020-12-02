'''
    File Name: test_reservations.py
    Project Name: SimplePark
    Author: Colin Robbins
    Student Number: 400353539
    Date: 12/02/2020
    Class: SFWRTECH 3RQ3
    Professor: Sean Watson
    Purpose: used to run tests on the reservations.py class
'''

from simplepark.reservations import Reservations

'''
Requirement 3.2: Viewing Account / Reservations
Testing: Will check the system to see if the ID is valid and
         follows the correct format for recalling from storage
         and for saving future data. 
---------------------------------------------------------------
'''
#--------------------------------------------------------------
def test_reservation_id():
    valid_id = [
        "000000",
        "010203",
        "999999"
    ]
    
    reservation = Reservations()
    for identity in valid_id:
        assert reservation.verify_reserve_id(identity) == True, "the reserve ID is correct."

def test_reservation_id_failed():
    invalid_id = [
        "AS0000",
        "ASVD010203",
        "999",
        None
    ]
    
    reservation = Reservations()
    for identity in invalid_id:
        assert reservation.verify_reserve_id(identity) == False, "the reserve ID is required to be 6 numerical digits."

#--------------------------------------------------------------
'''
Requirement 3.3.1: Setting time and reservation date.
Testing: Makes sure that the date that is given follows the correct format
         of MM/DD/YYYY and that it is dated to post creation of the app/company
         (conceptually created on 10/01/2020)
'''
#--------------------------------------------------------------
def test_reservation_date():
    valid_date = [
        "10/11/2020",
        "01/30/2022",
        "02/16/2021"
    ]

    reservation = Reservations()
    for date in valid_date:
        assert reservation.verify_date_reserved(date) == True, "the dates are valid and functioning"

def test_reservation_date_failed():
    invalid_date = [
        "10-11-2020",
        "13/32/1997",
        "02.16.2021",
        None
    ]

    reservation = Reservations()
    for date in invalid_date:
        assert reservation.verify_date_reserved(date) == False, "dates are well out of range before the companies existance or invalid format"
#--------------------------------------------------------------
'''
Requirement 3.3.2: Determining How long the Stay
Testing: If the stay is within the range of 0.5 hours to 24 hours.
         Where it is a negative number or it is outside of the given
         reservation range, it is no good.
'''
#--------------------------------------------------------------
def test_reservation_time():
    valid_times = [
        6,
        0.5,
        2,
        12,
        24
    ]
    
    reservation = Reservations()
    for time in valid_times:
        assert reservation.verify_time_allocated(time) == True, "The time can be anywhere from 0.5 to 24 hours"

def test_reservation_time_failed():
    invalid_times = [
        0.25,
        25,
        300,
        -1,
        None
    ]
    
    reservation = Reservations()
    for time in invalid_times:
        assert reservation.verify_time_allocated(time) == False, "The time cannot be a negative, over 24 hours or less then 30 minutes."
#--------------------------------------------------------------
'''
Requirement 3.3.3: Cancelling a Reservation
Testing: Used to determine whether a reservation is correctly cancelled
         and if someone is properly requesting it.
'''
#--------------------------------------------------------------
def test_reservation_cancellation():
    valid_cancel = True
    
    reservation = Reservations()
    if valid_cancel == True:
        assert reservation.verify_reservation_cancellation(valid_cancel) == True, "this will correctly cancel the reservation"

def test_reservation_cancellation_failed():
    invalid_cancel = False
    
    reservation = Reservations()
    if invalid_cancel == False:
        assert reservation.verify_reservation_cancellation(invalid_cancel) == False, "this will not cancel the reservation"
#--------------------------------------------------------------