import phonenumbers
from test import number  #import from test file 

from phonenumbers import geocoder #geocoder is a build in function in phonenumbers

country = phonenumbers.parse(number, "CH") #C FOR COUNTRY AND H FOR HISTORY
print(geocoder.description_for_number(country, "en"))


from phonenumbers import carrier  #for service provider

service = phonenumbers.parse(number, "RO")
print(carrier.name_for)