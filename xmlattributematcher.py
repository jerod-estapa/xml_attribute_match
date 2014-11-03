#!/usr/bin/python
#XML Attribute Match
#Parses an XML doc, matches unique attributes from a list to associated attributes in child elements,
#and prints matching results
#Python 2.7.4

import xml.etree.ElementTree as ET

#Puts inspection report numbers in a list
codes = ["LALAGL000755",
"MO1502005127",
"AZ0000781157",
"UT14SK000107",
"CO4B09000281",
"COPM40000748",
"NM3583103843",
"COHM34001388",
"NM3287102091",
"LALAGJ001256",
"TX3YBD0MUI0A",
"AZ00YP000747",
"ID6300005350",
"CO2C31000566",
"TX135U9DAK01",
"TX3S8D0AFH3D",
"AZ0YAR001127",
"FL1619000314",
"NM3529101793"]




#Parses the XML file and gets the root element
tree = ET.parse("C:\Users\Jest2733\Desktop\Complio\Exceptions\USDOT_156275_All_BASICs_09-26-2014.xml")

#Iterates through the list and the XML doc once, and uses set() to separate out only the necessary report numbers
codes = set(codes)
for x in codes:
    for node in tree.iter('inspection'):
        if node.attrib['report_number'] == x:
            primary_driver = [d for d in node.iter('driver') if d.attrib['driver_type'] == "Primary Driver"]
            primary_driver = primary_driver[0]
            first_name = primary_driver.attrib['first_name']
            last_name = primary_driver.attrib['last_name']
            cdl_number = primary_driver.attrib['License_number']
            print first_name, last_name, cdl_number

    for node in tree.iter('crash'):
        if node.attrib['report_number'] == x:
            driver = [d for d in node.iter('driver')]
            driver = driver[0]
            first_name = driver.attrib['first_name']
            last_name = driver.attrib['last_name']
            cdl_number = driver.attrib['license_number']
            print first_name, last_name, cdl_number



