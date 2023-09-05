from urllib.request import urlopen
import json

api_url = 'http://185.68.22.253/json-test'
response = urlopen(api_url)
data_json = json.loads(response.read())

with open('telephones.txt', 'w') as file:
    for branch in data_json['branches']:
        for division in branch['divisions']:
            for warehouse in division['warehouses']:
                if 'telephone' in warehouse:
                    telephone_data = "Telephone found:", warehouse['telephone'], branch['title']
                    for line in telephone_data:
                        file.write(str(line))  
                        file.write('\n')
                else:
                    print("Telephone not found in warehouse.")
