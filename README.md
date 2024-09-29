**Simulador de Incisões**

Participantes

**Introdução**
Este projeto tem como objetivo simular e avaliar a precisão de incisões realizadas em procedimentos cirúrgicos fictícios. A simulação é feita com base em coordenadas fornecidas pelo usuário, comparando-as com posições previamente estabelecidas para determinar o quão precisa foi a incisão. O projeto visa fornecer uma ferramenta simples para realizar simulações e armazenar os resultados em um arquivo JSON, permitindo ainda o cálculo da média de precisão das simulações realizadas.

Essa ferramenta foi criado com o intuíto de ajudar estudantes de medicina a melhorarem o seu desempenho nesse tipo de cirgurgia.

**Metodologias**
O projeto utiliza uma abordagem orientada a dados e lógica condicional para calcular a precisão das incisões. A seguir, estão descritas as principais metodologias aplicadas:

**Simulação de Incisão:**
O usuário fornece as coordenadas (x, y) da incisão real.
O sistema compara essas coordenadas com as coordenadas esperadas (definidas no código).
A diferença entre as coordenadas reais e as esperadas é usada para calcular a precisão da incisão, onde quanto menor a diferença, maior a precisão.

**Armazenamento de Dados:**
Após a simulação, os resultados são salvos em um arquivo JSON. Cada entrada de simulação contém as coordenadas inseridas, as coordenadas esperadas e a porcentagem de precisão calculada.
Se o arquivo já existir, os novos resultados são adicionados sem sobrescrever os dados anteriores.
Cálculo da Média de Precisão:

O sistema permite calcular a média das porcentagens de precisão de todas as simulações armazenadas.
O cálculo é realizado lendo todas as entradas do arquivo JSON e extraindo os valores de precisão para calcular a média.
Entrada de Dados:

O projeto é interativo, solicitando ao usuário que insira manualmente as coordenadas da incisão e depois decidindo entre realizar uma simulação ou calcular a média das simulações passadas.
Funcionalidades

**Simulação de Incisão:**
 Simula uma incisão com base nas coordenadas fornecidas e calcula a precisão em comparação às coordenadas esperadas.

**Armazenamento de Dados:** 
Todos os dados das simulações são armazenados em um arquivo "Resultado.json".
Cálculo da Média de Precisão: Calcula e exibe a média das porcentagens de precisão de todas as simulações já realizadas.
Instruções de Uso
Ao rodar o programa, você será questionado sobre qual operação deseja realizar:

**Simular:** 
Insira as coordenadas da incisão real (valores entre 1-9). O sistema calculará a precisão e salvará os resultados no arquivo Resultado.json.

**Média:** 
O sistema calculará e exibirá a média de acerto das simulações salvas no arquivo.

Os dados de cada simulação incluem a data e hora da realização, as coordenadas fornecidas e a precisão calculada.


**Bibliotecas:** json, datetime, os.

**json**
{
        "nome": "Tumor",
        "data": "28/09/2024 23:56:04",
        "posicao_colocada": {
            "x": 6,
            "y": 9
        },
        "posicao_certa": {
            "x": 6,
            "y": 9
        },
        "precisao": 100.0
    }

**Conclusão**
Este projeto apresenta uma solução simples e funcional para a simulação de incisões e cálculo de precisão, permitindo que os usuários avaliem a exatidão de suas incisões em relação às coordenadas esperadas. O sistema armazena os dados de maneira eficiente em um arquivo JSON e permite o cálculo da média de acertos, o que pode ser útil para monitorar o desempenho ao longo do tempo.

A solução pode ser expandida no futuro com funcionalidades adicionais, como uma interface gráfica ou a possibilidade de simular múltiplas incisões em uma única execução. No entanto, a simplicidade e eficácia do sistema atual fazem dele uma boa ferramenta para fins educativos e experimentais.