#!/usr/bin/python
#XML Attribute CSV Generator
#Parses an XML doc, matches unique attributes from a list to associated attributes in child elements,
#and prints matching results to a CSV file
#Python 2.7.4

import xml.etree.ElementTree as ET
import xlsxwriter

#prompts user to enter inspection codes
codes = [str(x) for x in raw_input('Enter inspection codes to search:').split()]


#prompts user to enter XML file path and parses to get the root element
tree = ET.parse(raw_input('Enter XML file path to parse:'))


#creates an empty list for the loops to populate
li = []

#iterates through the list and the XML doc once, and uses set() to separate out only the necessary report numbers
codes = set(codes)
for x in codes:
    for node in tree.iter('inspection'):
        if node.attrib['report_number'] == x:
            primary_driver = [d for d in node.iter('driver') if d.attrib['driver_type'] == "Primary Driver"]
            primary_driver = primary_driver[0]
            first_name = primary_driver.attrib['first_name']
            last_name = primary_driver.attrib['last_name']
            cdl_number = primary_driver.attrib['License_number']
            li.append((first_name, last_name, cdl_number))
            print first_name, last_name, cdl_number

    for node in tree.iter('crash'):
        if node.attrib['report_number'] == x:
            driver = [d for d in node.iter('driver')]
            driver = driver[0]
            first_name = driver.attrib['first_name']
            last_name = driver.attrib['last_name']
            cdl_number = driver.attrib['license_number']
            li.append((first_name, last_name, cdl_number))
            print first_name, last_name, cdl_number


#open a file for writing, truncates file and populates with li[]
with open('xmlmatch_report.csv', 'wb') as f:
    f.truncate()
    mywriter = csv.writer(f)
    mywriter.writerows(li)

#closes the file
f.close()
