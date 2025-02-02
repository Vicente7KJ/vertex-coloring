# Algoritmo Genético para Coloração de Grafos

## Visão Geral
Este projeto implementa um algoritmo genético para resolver o problema da coloração de grafos, garantindo que vértices adjacentes possuam cores diferentes. Ele utiliza a biblioteca `networkx` para manipulação de grafos e `matplotlib` para visualização.

## Funcionalidades
- **Carregamento de instâncias**: Leitura de arquivos de texto contendo grafos.
- **Listagem de instâncias**: Exibe todos os arquivos de instância disponíveis.
- **Coloração por algoritmo genético**: Aplica um método heurístico para atribuir cores aos vértices.
- **Visualização interativa**: Permite ajustar a disposição dos vértices.

## Requisitos
Para executar o projeto, é necessário ter Python instalado e as seguintes bibliotecas:
```sh
pip install networkx matplotlib
```

## Como Usar
1. **Listar instâncias disponíveis:**
```sh
python gen.py
> list
```

2. **Carregar um arquivo de instância:**
```sh
> read coloracao-inst7
```

3. **Colorir o grafo e exibir a visualização:**
```sh
> colorir
```

4. **Sair do programa:**
```sh
> exit
```

## Estrutura do Projeto
- `gen.py`: Script principal contendo a implementação do algoritmo genético e a interface do programa.
- `coloracao-instX`: Arquivos contendo diferentes instâncias de grafos para testes.

## Formato dos Arquivos de Instância
Cada arquivo segue o seguinte formato:
```
N  # Número de vértices
v1 v2 peso  # Arestas com pesos
v3 v4 peso
...
```

Exemplo:
```
5
1 2 3
2 3 2
3 4 4
4 5 1
1 5 2
```

## Documentação do Algoritmo
O algoritmo genético segue uma abordagem gulosa, onde:
1. Percorre os vértices ordenadamente.
2. Para cada vértice, verifica as cores usadas por seus vizinhos.
3. Atribui a menor cor disponível que não conflita.

## Contribuição
Contribuições são bem-vindas! Fique à vontade para abrir issues e enviar pull requests.

## Licença
Este projeto está licenciado sob a MIT License.

