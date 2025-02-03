import os
import random
import networkx as nx
import matplotlib.pyplot as plt

class GrafoColoracaoGenetico:
    def __init__(self):
        self.n = 0  # Número de vértices
        self.arestas = []  # Lista de arestas (v1, v2, peso)
        self.grafo = nx.Graph()
        self.instancia_carregada = None
        self.cores_disponiveis = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "gray", "cyan"]

    def listar_instancias(self):
        arquivos = [f for f in os.listdir() if f.startswith("coloracao-inst")]
        print("\nInstâncias disponíveis:")
        for arq in arquivos:
            print(f"- {arq}")

    def ler_arquivo(self, arquivo):
        if not os.path.exists(arquivo):
            print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
            return
        
        try:
            with open(arquivo, "r") as file:
                linhas = file.readlines()
                self.n = int(linhas[0].strip())
                self.arestas = []
                for linha in linhas[1:]:
                    dados = list(map(int, linha.strip().split()))
                    if len(dados) == 3:
                        self.arestas.append((dados[0], dados[1], dados[2]))
                
                self.instancia_carregada = arquivo
                print(f"\nArquivo '{arquivo}' carregado com sucesso!")
                
                self.grafo.clear()
                self.grafo.add_nodes_from(range(1, self.n + 1))
                for v1, v2, peso in self.arestas:
                    self.grafo.add_edge(v1, v2, weight=peso)
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def gerar_populacao_inicial(self, tamanho):
        populacao = []
        for _ in range(tamanho):
            individuo = {v: random.choice(self.cores_disponiveis) for v in self.grafo.nodes}
            populacao.append(individuo)
        return populacao

    def avaliar_aptidao(self, individuo):
        conflitos = sum(1 for v1, v2 in self.grafo.edges if individuo[v1] == individuo[v2])
        return conflitos

    def selecao_torneio(self, populacao, k=3):
        torneio = random.sample(populacao, k)
        torneio.sort(key=lambda ind: self.avaliar_aptidao(ind))
        return torneio[0]

    def crossover(self, pai1, pai2):
        ponto_corte = random.randint(1, self.n - 1)
        filho = {}
        for i, v in enumerate(self.grafo.nodes):
            filho[v] = pai1[v] if i < ponto_corte else pai2[v]
        return filho

    def mutacao(self, individuo, taxa_mutacao=0.1):
        for v in self.grafo.nodes:
            if random.random() < taxa_mutacao:
                individuo[v] = random.choice(self.cores_disponiveis)

    def algoritmo_genetico(self, tamanho_pop=100, geracoes=100, taxa_mutacao=0.1):
        populacao = self.gerar_populacao_inicial(tamanho_pop)
        melhor_solucao = None
        melhor_aptidao = float('inf')
        
        for _ in range(geracoes):
            nova_populacao = []
            for _ in range(tamanho_pop // 2):
                pai1 = self.selecao_torneio(populacao)
                pai2 = self.selecao_torneio(populacao)
                filho1 = self.crossover(pai1, pai2)
                filho2 = self.crossover(pai2, pai1)
                self.mutacao(filho1, taxa_mutacao)
                self.mutacao(filho2, taxa_mutacao)
                nova_populacao.extend([filho1, filho2])
            
            populacao = nova_populacao
            populacao.sort(key=lambda ind: self.avaliar_aptidao(ind))
            if self.avaliar_aptidao(populacao[0]) < melhor_aptidao:
                melhor_solucao = populacao[0]
                melhor_aptidao = self.avaliar_aptidao(populacao[0])
            if melhor_aptidao == 0:
                break
        return melhor_solucao

    def mostrar_grafo_colorido(self):
        if not self.grafo or self.grafo.number_of_nodes() == 0:
            print("\nNenhum grafo carregado! Use 'read <arquivo>' primeiro.")
            return
        
        cores = self.algoritmo_genetico()
        if not cores:
            print("\nErro ao colorir o grafo.")
            return
        
        pos = nx.spring_layout(self.grafo)
        nx.draw(self.grafo, pos, with_labels=True, node_color=[cores[n] for n in self.grafo.nodes], node_size=700, edge_color="black", linewidths=1, font_size=10)
        labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.show()

if __name__ == "__main__":
    grafo = GrafoColoracaoGenetico()
    while True:
        print("\nDigite um comando: (list, read <arquivo>, colorir, exit)")
        comando = input("> ").strip().split()
        if not comando:
            continue
        if comando[0] == "list":
            grafo.listar_instancias()
        elif comando[0] == "read" and len(comando) == 2:
            grafo.ler_arquivo(comando[1])
        elif comando[0] == "colorir":
            grafo.mostrar_grafo_colorido()
        elif comando[0] == "exit":
            print("Saindo...")
            break
        else:
            print("Comando inválido! Use: list, read <arquivo>, colorir ou exit.")
