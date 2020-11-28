from simplepark.creditcard import CreditCards

def test_credit_card_holder_name():
    firstName = "Billy"
    lastName = "Bob"
    
    valid_name = [firstName, 
                   lastName]
    
    creditNameCheck = CreditCards()
    for names in valid_name:
        assert creditNameCheck.verify_name_on_card(names) == True, "names contains first and last, and valid characters"
        
def test_credit_card_holder_name_failed():
    firstName = "$illy"
    lastName = None
    
    invalid_name = [firstName,
                    lastName]
    
    creditNameCheck = CreditCards()
    for names in invalid_name:
        assert creditNameCheck.verify_name_on_card(names) == False, "name has invalid characters or missing either first or last name"

def test_credit_card_number():
    valid_card_numbers = [
        "5191789023457890",
        "4111111111111111",
        "340000000000009",
        "1234567891234567"    
    ]   
    
    creditNumberCheck = CreditCards()
    for number in valid_card_numbers:
        assert creditNumberCheck.verify_card_number(number) == True, "the number follows a correct format and has correct spacing"
        
def test_credit_card_number_failed():
    invalid_card_numbers = [
        "5191789ggh890",
        "411111",
        "banana000000009",
        "#@$@3214323$%34345234527",
        None  
    ]
        
    creditNumberCheck = CreditCards()
    for number in invalid_card_numbers:
        assert creditNumberCheck.verify_card_number(number) == False, "the number may contain letters or other formats that are incorrect."    
        
def test_credit_card_expiry_date():
    valid_dates = [
        "10/22",
        "06/23",
        "03/26",
        "07/25"
    ]

    creditExpiryCheck = CreditCards()
    for date in valid_dates:
        assert creditExpiryCheck.verify_card_expiry(date) == True, "the date has to be future and has format MM/YY"
        
def test_credit_card_expiry_date_failed():
    invalid_dates = [
        "200/Banana",
        "14,16",
        "14/19",
        None
    ]
    
    creditExpiryCheck = CreditCards()
    for date in invalid_dates:
        assert creditExpiryCheck.verify_card_expiry(date) == False, "the date is outdated, not numerical, or does not follow format"
        
def test_credit_card_ccv():
    valid_ccv = [
        "001",
        "849",
        "738",
        "189"
    ]
    
    creditCCVCheck = CreditCards()
    for ccv in valid_ccv:
        assert creditCCVCheck.verify_ccv(ccv) == True, "the CCV follows correct format and is not missing"

def test_credit_card_ccv_failed():
    invalid_ccv = [
        "0000",
        "Banana",
        "91",
        "1",
        None
    ]
        
    creditCCVCheck = CreditCards()
    for ccv in invalid_ccv:
        assert creditCCVCheck.verify_ccv(ccv) == False, "the CCV does not follow correct format (###)"
