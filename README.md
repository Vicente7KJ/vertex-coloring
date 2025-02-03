# Documentação do Algoritmo Genético para Coloração de Grafos

## Introdução
Este documento descreve a lógica e heurística utilizadas no algoritmo genético implementado para resolver o problema de coloração de grafos. A coloração é feita garantindo que vértices adjacentes tenham cores diferentes, minimizando o número total de cores utilizadas.

## Estrutura do Algoritmo
O algoritmo genético segue as seguintes etapas:

1. **Inicialização**: O grafo é lido a partir de um arquivo de entrada e armazenado em uma estrutura `networkx.Graph()`.
2. **Geração Inicial**: É gerada uma população inicial de soluções aleatórias, onde cada solução é uma atribuição de cores aos vértices.
3. **Avaliação da Aptidão**: Cada solução é avaliada com base no número de cores utilizadas e na presença de conflitos.
4. **Seleção**: As melhores soluções são selecionadas para gerar a próxima geração usando torneio ou roleta.
5. **Cruzamento**: Novas soluções são geradas a partir das soluções selecionadas, combinando atributos de duas soluções parentais.
6. **Mutação**: Pequenas alterações são feitas para evitar que o algoritmo convirja prematuramente para um ótimo local.
7. **Critério de Parada**: O processo se repete até atingir um critério de parada, como um limite de gerações ou uma solução sem conflitos.

## Implementação no Código
O código implementa um algoritmo genético completo:
- **População Inicial**: Cada indivíduo representa uma possível coloração do grafo.
- **Função de Aptidão**: Penaliza soluções com conflitos e favorece soluções com menos cores.
- **Seleção**: Utiliza um método de torneio para escolher os melhores indivíduos.
- **Cruzamento**: Combina cores de dois indivíduos para gerar novos.
- **Mutação**: Modifica aleatoriamente a cor de alguns vértices para aumentar a diversidade.
- **Critério de Parada**: O algoritmo para após um número fixo de gerações ou quando encontra uma solução ótima.

## Formato do Arquivo de Entrada
Os arquivos de entrada devem seguir o seguinte formato:
- A primeira linha contém um número inteiro `N`, representando o número de vértices do grafo.
- As linhas subsequentes contêm três inteiros `v1 v2 peso`, onde `v1` e `v2` são os vértices conectados por uma aresta e `peso` representa a ponderação dessa aresta.

### Exemplo de Entrada:
```
5
1 2 3
1 3 2
2 4 1
3 5 4
4 5 2
```

## Melhorias Possíveis
- Ajustar os parâmetros genéticos para um melhor desempenho.
- Implementar elitismo para preservar as melhores soluções entre gerações.
- Explorar técnicas de aprendizado de máquina para aprimorar a seleção de cores.
- Melhorar a visualização dos grafos com um layout ajustável pelo usuário.

## Conclusão
O algoritmo genético para coloração de grafos implementado é uma abordagem adaptativa que permite encontrar boas soluções para o problema. A introdução de operadores genéticos aprimora a eficiência e qualidade das colorações obtidas.

## Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as bibliotecas necessárias com o comando:
   ```sh
   pip install networkx matplotlib
   ```
3. Execute o script principal:
   ```sh
   python gen.py
   ```
4. Utilize os comandos disponíveis no menu:
   - `list` para listar instâncias disponíveis.
   - `read <arquivo>` para carregar um grafo.
   - `colorir` para executar o algoritmo genético e visualizar o grafo colorido.
   - `exit` para sair do programa.

## Licença
Este projeto é disponibilizado sob a licença MIT.

