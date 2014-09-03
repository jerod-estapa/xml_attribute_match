#!/usr/bin/python
#XML Attribute Match
#Parses an XML doc, matches unique attributes from a list to associated attributes in child elements,
#and prints matching results
#Python 2.7.4

import xml.etree.ElementTree as ET

#Puts inspection report numbers in a list
codes = ['TX3YZ8HQE1X1', 'TX3YAEHQE15W', 'KS00YQ008857', 'TX43D99DAN33', 'NM3267100378',
         'COPF31000853', 'TX3ZYF0MUQ6F', 'TX3ZFC0MHXLU', 'TX3Z760MGU0H', 'TX3YGG0MUQ1R',
         'TX3YBD0MUI0A', 'TX3XPF0MKQYG', 'TX3X8F0MHXA7', 'AZ0160001581', 'TX3WC40ADYGZ',
         'ID6300005350', 'TX3VV50ADUOI', 'TX137S0ELO02', 'UTCE03208119', 'UTCE03208119',
         'TX3UTG0MJKDL', 'TX3UD60MIJU5', 'TX13690EBI05', 'TX3U4E0AFA94', 'TX3U4E0AFA94',
         'TX3T5F0MIJMH', 'TX13550BKL02', 'TX3SLE0MIJGZ', 'TX3SLE0MIJGZ', 'TX3S8D0AFH3D',
         'UTCE03207947', 'TX133Q0ENG01', 'TX133Q0ENG01', 'TX133Q0ENG01', 'TX3REM0MHEK3',
         'ID0000169042', 'COPF05000200', 'TX13280EPV0B', 'TX131S9DAB02', 'CO1E19000017',
         'TX3PD60WAA4L', 'TX1317W1NW07', 'CO2D02000044', 'LALAEQ001266', 'TX130H0EBT06',
         'TX3NW10ABLMK', 'NV7233010192', 'NV4045000998', 'CO3301000406', 'CO5C01000218',
         'TX12949DBU03', 'FL1619000314', 'TX12929DIE02', 'TX128X0AAP01', 'TX128A9DHA07',
         'CO2B01000061', 'TX1274W1DV01', 'TX126Z9DCM01', 'TX127U9DBV01', 'TX127U9DBV01',
         'TX127R9DIZ02', 'TX127K9DCQ06', 'AZ0YDG000141', 'NV7196001031', 'TX126B0FJZ01',
         'TX126I9DAN01', 'LALACV003777', 'CO2B12000014', 'TX12650HTB01', 'ID0000220955']

#Parses the XML file and gets the root element
tree = ET.parse("C:\Users\Jest2733\Desktop\Complio\USDOT_156275_All_BASICs_07-25-2014.xml")
root = tree.getroot()

#Iterates through the list and the XML doc once, and uses set() to separate out only the necessary report numbers
codes = set(codes)
for x in codes:
    for node in tree.iter('inspection'):
        if node.attrib['report_number'] == x:
            primary_driver = [d for d in node.iter('driver') if d.attrib['driver_type'] == "Primary Driver"]
            primary_driver = primary_driver[0]
            first_name = primary_driver.attrib['first_name']
            last_name = primary_driver.attrib['last_name']
            print x
            print first_name, last_name

            

