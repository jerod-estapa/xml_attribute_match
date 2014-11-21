#!/usr/bin/python
#XML Attribute XLSX Generator
#Parses an XML doc, matches unique attributes from a list to associated attributes in child elements,
#and prints matching results to a .xslx file
#Python 2.7.4

import xml.etree.ElementTree as ET
import xlsxwriter
import easygui as eg

#Prompts user to enter inspection codes
codes = [str(x) for x in eg.enterbox(msg='Enter inspection codes to search:', strip=False).split()]

#Prompts user to select XML file and parses to get the root element
tree = ET.parse(eg.fileopenbox(msg='Select an XML file to parse:', filetypes='*.xml'))

#Creates an empty list for the loops to populate
li = []

#Iterates through the list and the XML doc once, and uses set() to separate out only the necessary report numbers
codes = set(codes)

#Nested loops to traverse the tree, find matching inspection codes, print associated first name, last name, cdl
for x in codes:
    for node in tree.iter('inspection'):
        if node.attrib['report_number'] == x:
            primary_driver = [d for d in node.iter('driver') if d.attrib['driver_type'] == "Primary Driver"]
            primary_driver = primary_driver[0]
            try:
                first_name = primary_driver.attrib['first_name']
            except:
                first_name = 'NA'
            try:
                last_name = primary_driver.attrib['last_name']
            except:
                last_name = 'NA'
            try:
                cdl_number = primary_driver.attrib['License_number']
            except:
                cdl_number = 'NA'
            li.append((first_name, last_name, cdl_number))
            print first_name, last_name, cdl_number

    for node in tree.iter('crash'):
        if node.attrib['report_number'] == x:
            driver = [d for d in node.iter('driver')]
            driver = driver[0]
            try:
                first_name = driver.attrib['first_name']
            except:
                first_name = 'NA'
            try:
                last_name = driver.attrib['last_name']
            except:
                last_name = 'NA'
            try:
                cdl_number = driver.attrib['license_number']
            except:
                cdl_number = 'NA'
            li.append((first_name, last_name, cdl_number))
            print first_name, last_name, cdl_number

#Creates a new workbook and worksheet
workbook = xlsxwriter.Workbook('Exception_matches.xlsx')
worksheet = workbook.add_worksheet()

#Add formatting
bold = workbook.add_format({'bold': 1})
worksheet.write('A1', 'First Name', bold)
worksheet.write('B1', 'Last Name', bold)
worksheet.write('C1', 'CDL Number', bold)

#Convert li[] tuples to strings and write to worksheet
newlist = [str(a) for a in li]
worksheet.write_column(1, 0, newlist)

#Close workbook
workbook.close()
