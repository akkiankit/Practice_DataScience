import json
#this is the exapmple of json as a dictionary
data = '''{
    "name" : "chuck",
    "phone" : {
        "type" : "intl",
        "number" : " +989769"
    },
    "email" : {
        "hide" : "Yes"
    }
}'''
#json represents data as nested lists and dictionaries
info = json.loads(data)
print(type(info))
#here info is dictionalries
print('name : ', info["name"])
print('hide : ', info["email"]["hide"])

# Another example of JSON as a list
#since here json is starting with [ ] so it is list however previous example having {} so it is dictionary
input1 = '''[
    { "id" : "001",
        "x" : "3",
        "name" : "ankit"
        },
        {
            "id" : "008",
            "x" : "87",
            "name" : "kumar"
        }
]'''

info1 = json.loads(input1)
print("user count ; ",len(info1))
print(type(info))
for item in info1:
    print('name: ', item['name'])
    print('id', item['id'])
    print('attribute', item['x'])