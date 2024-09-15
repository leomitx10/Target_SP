def calcula_mensal():
    data = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "OUTROS": 19849.53
    }
    
    total = sum(data.values())
    
    porcentagem = {state: round((value / total) * 100, 2) for state, value in data.items()}
    
    for state, porcenta in porcentagem.items():
        print(f"{state}: {porcenta}%")
        
calcula_mensal()
