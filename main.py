import re
expressao_regular = r'^[1-9][\d+]{5}$'

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

def main():
    cep_a_validar = input('Digite o número do cep: ')
    if verifica_cep_valido(cep_a_validar):
        return print('Cep válido')
    return print('Cep inválido')

if __name__ == '__main__':
    main()