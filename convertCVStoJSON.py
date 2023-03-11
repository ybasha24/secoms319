# From https://www.geeksforgeeks.org/convert-text-file-to-json-in-python/

# Adjusted by: Abraham Aldaco
# Nov 22, 2022

# Python program to convert text
# file to JSON


import json

def removeLeadingSpaces(product):
    newListproduct = []
    for element in product:
        element=element.strip()
        element=element.strip('\n')
        newListproduct.append(element)
    return newListproduct

def createDictionary(product,productName):
    # productName = 'Ceiling Fan' 'Wall Light' or 'Jacket'
    dicTemp = {}
    i = 0
    while i<len(product):
        # creating dictionary for each employee
        if productName == 'Basketball':
            dicTemp[fieldsBasketball[i]]= product[i]
        elif productName == 'Football':
            dicTemp[fieldsFootball[i]]= product[i]
        i = i + 1
    return dicTemp


# the file to be converted
filename = 'data.csv'

# resultant dictionary
dictBasketball = {}
dictFootball = {}
dictGeneral = {}


listBasketball = []
listFootball = []


# fields in the sample file
productType = ['Basketball','Football']
fieldsBasketball =['productId', 'productName', 'location', 'description','prize']
fieldsFootball = ['productId', 'productName', 'location', 'description','prize']


with open(filename) as catalog:
    # Read line by line
    for line in catalog:
        
        # reading line by line from the text file
        product = line.split(',')
        product = removeLeadingSpaces(product)

		# for output see below
        print(product)

        if (product[1] == 'Basketball'):
            listBasketball.append(createDictionary(product, 'Basketball'))
            

        elif (product[1] == 'Football'):
            listFootball.append(createDictionary(product,'Football'))
        else:
            continue


# close catalog file
catalog.close()

# create general dictionary
dictGeneral['Basketball']=listBasketball
dictGeneral['Football']=listFootball


# creating json file	
out_file = open("data.json", "w")
json.dump(dictGeneral, out_file, indent = 4)
out_file.close()

