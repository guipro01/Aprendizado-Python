trib_produto = float(input("Digite o valor do item: "))
uf = input("Digite a UF (ex: SP, MG, RJ): ").upper()

# Tabela de ICMS por UF 
aliquotas_icms = {
    "AC": 0.17,
    "AL": 0.18,
    "AP": 0.18,
    "AM": 0.18,
    "BA": 0.18,
    "CE": 0.18,
    "DF": 0.18,
    "ES": 0.17,
    "GO": 0.17,
    "MA": 0.18,
    "MT": 0.17,
    "MS": 0.17,
    "MG": 0.18,
    "PA": 0.17,
    "PB": 0.18,
    "PR": 0.19,
    "PE": 0.18,
    "PI": 0.18,
    "RJ": 0.20,
    "RN": 0.18,
    "RS": 0.17,
    "RO": 0.17,
    "RR": 0.17,
    "SC": 0.17,
    "SP": 0.18,
    "SE": 0.18,
    "TO": 0.18
}

# Verifica se a UF existe
if uf in aliquotas_icms:
    aliquota = aliquotas_icms[uf]
    base_icms = trib_produto
    valor_icms = trib_produto * aliquota

    print("Base de ICMS =", base_icms)
    print("Alíquota =", aliquota)
    print("Valor ICMS =", valor_icms)
else:
    print("UF inválida! Verifique e tente novamente.")