import requests

# AIzaSyDe1aRDqNcM6GDFD-ownLRFkPYWybCRXXQ

result = requests.get('https://www.googleapis.com/voterinfo/v2/elections?key=AIzaSyDe1aRDqNcM6GDFD-ownLRFkPYWybCRXXQ')
#start = 'https://www.googleapis.com/civicinfo/v2/voterinfo?key=AIzaSyDe1aRDqNcM6GDFD-ownLRFkPYWybCRXXQ&address='
#address = '22%20Post%20Lane%South.%20Suffern%20NY'
start ='https://www.googleapis.com/civicinfo/v2/representatives?key=AIzaSyDe1aRDqNcM6GDFD-ownLRFkPYWybCRXXQ&address='
# address ='22%20Post%20Lane%20South.%20Suffern%20NY'
# address = '22 Post Lane South, Suffern NY'
# address = '270 East 27th Street, Brooklyn NY'
def space(address):
        address = address.replace(' ','%20',address.count(' '))
        address = address.replace(',','.', address.count(','))
        return (address)
# print (space(address))        
# url = start + address
# print(url)
# result = requests.get(url)

# result_dict = result.json()
# print(result_dict)
# for item in result_dict['offices'][10]['name']:
#     print (item)
# # for item in result_dict['Time Series (Daily)']:
# #     print(item, result_dict['Time Series (Daily)'][item]['4. close'])
    
# print ('now im doing the api part!')
# print ('Your '+result_dict['offices'][10]['name']+' is')
#j = range(11)
# for n in j:
#     print (n)
# j=range(11)
# j = range(len(result_dict['offices']))
# print (j)
# for x in j:
#   # j = range(11)
#   # result_dict['offices'][j]['name']
#     print('Your '+ result_dict['offices'][x]['name']+ ' is '+ result_dict['officials'][x]['name'])

# result_dict['officials'][x]['name']

# print( "hi "+"        "   + " you")
# print( "hi "+"                                           "   + " you")


def api_function(address):
    address = space(address)
    url = start + address
    result = requests.get(url)
    result_dict = result.json()
    j = range(len(result_dict['offices']))
    candidates = []
    for x in j:
        candidates.append((result_dict['offices'][x]['name'], result_dict['officials'][x]['name']))
        # print('Your '+ result_dict['offices'][x]['name']+ ' is '+ result_dict['officials'][x]['name'])
    return candidates



