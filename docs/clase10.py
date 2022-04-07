expressionLevel = 2
if expressionLevel > 100:
    print("gene is highly expressed.")
else:
    print("gene is lowly expressed")

# Operador if dentro de un loop
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        print(accession)

# operador is
list1 = []
list2 = []
list3 = list1
if (list1 == list2):
    print("True")
else:
    print("False")
if (list1 is list2):
    print("True")
else:
    print("False")
if (list1 is list3):
    print("True")
else:
    print("False")

print(id(list1))
print(id(list2))
print(id(list3))

# Estructura if, elif, else
