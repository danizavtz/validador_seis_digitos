import re
expressao_regular = '^[1-9][\d+]{5}$'

def verifica_alternado_em_par(valor_a_verificar):
    for num, f in enumerate(valor_a_verificar):
        j = num + 2
        if j < len(valor_a_verificar) and f == valor_a_verificar[j]:
            return True
    return False

def verifica_cep_valido(cep):
    cep = str(cep)
    resultado = re.match(expressao_regular, cep)
    if resultado and not verifica_alternado_em_par(cep):
        return True
    return False