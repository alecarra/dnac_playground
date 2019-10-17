#!/usr/bin/python

import json

#open the json file and print the data

file_name = input("What's the file you want to read? ")
print("Reading ",file_name)


print("\n")
print("This is the entire file:")
print("\n")
with open("/Users/alecarra/Documents/DNA/brkdev-1105/"+file_name) as f:
    data = json.loads(f.read())
    # print(data) --> commented because this is the raw file
    print(json.dumps(data, indent=4, sort_keys=True)) #this is the pretty print of json
    
#get only the second level keys, the first level is response
    print("\n")
    print("These are the keys only")
    print("\n")

    the_keys=data["response"][0].keys()
    print(the_keys)
    print("\n")

#other way to get the keys
    print("\n")
    print("These is the other way to get the keys only")
    print("\n")
    print(list(data)[1])

#after opening the file show all the hostnames, family and mgmt ip of the devices in the file
    print("\n")
    print("This is the data I'm intersted in:")
    print("\n")
    for p in data['response']:
        print('hostname: ' + p['hostname'])
        print('family: ' +p['family'])
        print('managementIpAddress: ' +p['managementIpAddress'])
        print("\n")

    for (k, v) in data.items():
       print("Keys: " + k)
       print("Value: " + str(v))
       
       
	