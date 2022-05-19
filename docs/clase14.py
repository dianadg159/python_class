def hola_con_nombre(name):
    print('Hola ' + name)


nombre = 'Phil'
hola_con_nombre(nombre)


def multiplica(val1, val2):
    result = val1 * val2
    return result


resultado = multiplica(3, 5)
print(resultado)


def get_AT_content(dna, decimales=2):  # Con dos como defalut
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return str(round(at_content, decimales))


print(get_AT_content("ATGCGTAGCAGTGCAG"))
print(get_AT_content("ATGCGTAGCAGTGCAG", decimales=4))
