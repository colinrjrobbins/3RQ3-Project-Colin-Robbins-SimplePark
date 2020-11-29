from simplepark.reservations import Reservations

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
