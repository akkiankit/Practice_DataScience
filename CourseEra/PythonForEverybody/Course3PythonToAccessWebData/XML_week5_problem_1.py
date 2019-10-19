#importing the xml libarary
#Et works as a alias
import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
    +176033 3234 0809
    </phone>
    <email hide="yes"/>
    </person>'''
#format string is used to take the string and format the string in tree architecture as internal memory architcture
tree = ET.fromstring(data)
#
print('Name:',tree.find('name').text)
print('attr: ', tree.find('email').get('hide'))    