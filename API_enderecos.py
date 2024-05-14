import requests

lista_ceps = ['58028520', '20050000', '58028500']
lista_enderecos = []

for cep in lista_ceps:
    url = 'http://viacep.com.br/ws/{}/json/'.format(cep)
    try:
        req = requests.get(url, timeout=5)
        endereco = req.json()
        if 'cep' in endereco:
            lista_enderecos.append([endereco["cep"], endereco.get("logradouro", ""), endereco.get("uf", "")])
        else:
            print("CEP não encontrado para:", cep)
    except Exception as e:
        print("Erro ao obter informações para o CEP:", cep)
        print("Erro:", e)

for item in lista_enderecos:
    print(item)
