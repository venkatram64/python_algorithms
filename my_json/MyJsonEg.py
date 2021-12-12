import json


def processJons():
    global data
    people_string = '''
        {
        "people":[
            {
                "name":"Venkat Veerareddy",
                "phone": "123-123-1234",
                "emails":["abc@abc.com","xyz@xyz.com"],
                "has_license": false
            },
            {
                "name":"Srijan Veerareddy",
                "phone": "456-123-1234",
                "emails":null,
                "has_license": true
            }]
        }
    '''
    data = json.loads(people_string)
    print(data)
    print(type(data))
    print(type(data['people']))
    print("************")
    for people in data['people']:
        print(people)
        print(people['name'])
    # deleting phone number from json object
    for people in data['people']:
        del people['phone']
        print(people)
    # after modifying json, dumps
    # converting python object into json
    print("***********")
    new_string = json.dumps(data)
    print(new_string)
    new_string = json.dumps(data, indent=4)
    print(new_string)
    new_string = json.dumps(data, indent=2, sort_keys=True)
    print(new_string)


#https://docs.python.org/3/library/json.html
processJons()