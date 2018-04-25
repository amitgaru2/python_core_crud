import re

class Validation():
    def __init__(self):
        pass
    
    def validate_name(self, value):
        if re.match(r'^[a-zA-Z]+(\s?[a-zA-Z]*)*$', value): return value
        else: raise ValueError('Invalid Name')
    
    def validate_email(self, value):
        if re.match(r'^[a-zA-Z]+\d*(\.|_)?[a-zA-Z]+\d*@[a-zA-Z]+\.[a-zA-Z]+$', value): return value
        else: raise ValueError('Invalid Email')
    
    def validate_phone(self, value):
        if re.match(r'^\d{5,13}$', value): return value
        else: raise ValueError('Invalid Phone no')
    
    def validate_longitude(self, value):
        if value == '': return value        # can be null
            
        _value = float(value)
        if _value>-180 and _value<180: return value
        else: raise ValueError('Invalid Longitude')
        
    def validate_latitude(self, value):
        if value == '': return value        # can be null

        _value = float(value)
        if _value>-90 and _value<90: return value
        else: raise ValueError('Invalid Latitude')
    
    def validate_gender(self, value):
        if value=="0" or value=="1": return value
        else: raise ValueError("Invalid Gender")
    
    def validate_dob(self, value):
        if value == '': return value        # can be null

        _value = value.split('/')
        month = int(_value[0])
        day = int(_value[1])
        year = int(_value[2])

        if day>0 and day<33 and month>0 and month<13 and year>1960 and year<2018:
            return value
        else:
            raise ValueError("Invalid DOB")

    
    def validate_social(self, value):
        if value == '': return value        # can be null

        if re.match(r'^http://', value): return value
        else: raise ValueError("Invalid Social Media Link")

# vald = Validation()
# print(vald.validate_social("http:/ami_mi@gmail.com"))             