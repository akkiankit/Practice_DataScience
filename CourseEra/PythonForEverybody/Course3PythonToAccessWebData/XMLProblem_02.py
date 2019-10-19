import xml.etree.ElementTree as ET

input = ''' <stuff>
        <users>
            <user x="2">
                <id> 009</id>
                <name>Chuck</name>
            </user>
            <user x= "7">
                <id> 008 </id>
                <name>Bent</name>
            </user>
        </users>
    </stuff>'''

stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
lst = stuff.findall('users/user')
print("user count", len(lst))

for item in lst:
    print("name", item.find('name').text)
    print('id:',item.find('id').text)
    print('Attribute:',item.get("x"))
