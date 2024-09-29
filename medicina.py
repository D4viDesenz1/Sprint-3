import json
from datetime import datetime
import os

# Função que simula uma incisão e calcula a precisão com base nas coordenadas fornecidas
def simular_incisao(x_real, y_real, x_esperado, y_esperado, tamanho_padrao=5):
    diferenca_x = abs(x_real - x_esperado)  # Diferença em X
    diferenca_y = abs(y_real - y_esperado)  # Diferença em Y

    # Calcula a porcentagem de precisão baseada nas diferenças
    precisao_x = max(0, 100 - (diferenca_x * 10))  # Cada unidade de erro reduz 10% da precisão
    precisao_y = max(0, 100 - (diferenca_y * 10))  # Idem para o eixo Y

    # A precisão final é a média das duas precisões
    precisao_final = (precisao_x + precisao_y) / 2

    # Retorna uma mensagem com o resultado e a precisão calculada
    resultado_incisao = f"Incisão realizada na posição ({x_real}, {y_real}) com tamanho padrão ({tamanho_padrao}, {tamanho_padrao})."
    return resultado_incisao, precisao_final

# Função que salva os resultados da simulação em um arquivo JSON
def salvar_dados(procedimento, nome_arquivo):
    # Verifica se o arquivo já existe
    if os.path.exists(nome_arquivo):
        # Carrega dados existentes
        with open(nome_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
    else:
        dados = []

    # Adiciona o novo procedimento aos dados
    dados.append(procedimento)

    # Salva os dados atualizados no arquivo JSON
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
    print(f"Dados salvos em {nome_arquivo}")

# Função que calcula a média das precisões armazenadas
def calcular_media(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print("Nenhum dado encontrado.")
        return
    
    # Carrega os dados existentes
    with open(nome_arquivo, 'r') as arquivo_json:
        dados = json.load(arquivo_json)

    # Filtra as porcentagens de precisão e calcula a média
    porcentagens = [proc['precisao'] for proc in dados if 'precisao' in proc]

    if porcentagens:
        media = sum(porcentagens) / len(porcentagens)
        print(f"Média de acerto: {media:.2f}%")
    else:
        print("Nenhuma porcentagem de acerto encontrada.")

# Função para obter as coordenadas da incisão fornecidas pelo usuário
def obter_dados():
    nome_cirurgia = "Tumor"  # Nome fixo da cirurgia

    # Coleta a data e hora atual
    data_cirurgia = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Obtém as coordenadas da incisão real
    x_real = int(input("Posição X real da incisão (1-9): "))
    y_real = int(input("Posição Y real da incisão (1-9): "))

    # Define as coordenadas esperadas da incisão
    x_esperado = 6
    y_esperado = 9

    # Retorna um dicionário com as informações da cirurgia
    procedimento = {
        "nome": nome_cirurgia,
        "data": data_cirurgia,
        "posicao_colocada": {"x": x_real, "y": y_real},
        "posicao_certa": {"x": x_esperado, "y": y_esperado}
    }

    return procedimento

# Função principal que executa o fluxo do programa
def executar_simulacao():
    # Solicita a ação desejada pelo usuário
    opcao = input("Seja bem-vindo ao nosso sistema! O que você deseja? (Simular ou Media): ").lower()

    if opcao == 'simular':
        procedimento = obter_dados()

        # Simula a incisão e obtém o resultado e a precisão
        resultado_incisao, precisao = simular_incisao(
            procedimento["posicao_colocada"]["x"],
            procedimento["posicao_colocada"]["y"],
            procedimento["posicao_certa"]["x"],
            procedimento["posicao_certa"]["y"]
        )

        print(resultado_incisao)
        print(f"Porcentagem de acerto: {precisao:.2f}%")

        # Adiciona a precisão aos dados do procedimento e salva
        procedimento['precisao'] = precisao
        salvar_dados(procedimento, 'Resultado.json')

    elif opcao == 'media':
        # Calcula e exibe a média das porcentagens de precisão
        calcular_media('Resultado.json')

    else:
        print("Opção inválida. Tente novamente.")

# Executa a simulação
executar_simulacao()
