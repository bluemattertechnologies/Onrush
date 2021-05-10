from firebase import firebase

# firebase=firebase.FirebaseApplication("https://onrush-delivery-5e1e8-default-rtdb.firebaseio.com/",None)
# data={
#     'Names':'Tester2',
#     'Email':'par2@gmail.com',
#     'Phone':8139891838,
#     'XXXX':'1234567u'
# }

# result=firebase.post('onrush-delivery-5e1e8-default-rtdb/Customer',data)
# result=firebase.get('onrush-delivery-5e1e8-default-rtdb/Customer','')
# print(result)

################################################################################################
import re


def fizz_count():
    string="banana banana banana"
    s=string.split(" ")
    for x in s:
        if x.lower().startswith(str("BA").lower()):
            return True

print(fizz_count())