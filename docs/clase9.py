# Abrir el archivo
names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",")
print(str(species))
for specie in species:
    print(specie + " es una especie")

file = open("data/dna_sequences.txt")
all_lines = file.readlines()
file.close()

sec = []
noAdaptadores = open("data/noAdaptadores", "w")

for line in all_lines:
    noAdaptadores.write(str(line[14:-1]))
    noAdaptadores.write("\n")