import os
import networkx as nx
import matplotlib.pyplot as plt

class GrafoColoracao:
    def __init__(self):
        self.n = 0  # Número de vértices
        self.arestas = []  # Lista de arestas (v1, v2, peso)
        self.grafo = nx.Graph()  # Grafo do NetworkX
        self.instancia_carregada = None  # Nome do arquivo carregado
        self.pos = None  # Armazena posições dos vértices

    def listar_instancias(self):
        arquivos = [f for f in os.listdir() if f.startswith("coloracao-inst")]
        print("\nInstâncias disponíveis:")
        print("\n".join(f"- {arq}" for arq in arquivos) if arquivos else "Nenhuma instância encontrada.")

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
                
                self.pos = nx.spring_layout(self.grafo)  # Inicializa a posição dos vértices
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def algoritmo_genetico_coloracao(self):
        if not self.grafo or self.grafo.number_of_nodes() == 0:
            print("\nNenhum grafo carregado! Use 'read <arquivo>' primeiro.")
            return None
        
        cores = {}
        cores_disponiveis = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "gray", "cyan", "brown"]
        
        for vertice in sorted(self.grafo.nodes):  # Garante que percorremos os vértices corretamente
            vizinhos = list(self.grafo.neighbors(vertice))
            vizinhos_cores = {cores.get(v, None) for v in vizinhos if v in cores}
            
            for cor in cores_disponiveis:
                if cor not in vizinhos_cores:
                    cores[vertice] = cor
                    break
            else:
                cores[vertice] = "black"  # Caso especial se não houver cores suficientes
        
        return cores

    def mostrar_grafo_colorido(self):
        if not self.grafo or self.grafo.number_of_nodes() == 0:
            print("\nNenhum grafo carregado! Use 'read <arquivo>' primeiro.")
            return
        
        cores = self.algoritmo_genetico_coloracao()
        if not cores:
            print("\nErro ao colorir o grafo.")
            return
        
        if self.pos is None:
            self.pos = nx.spring_layout(self.grafo)  # Garante que sempre há uma posição válida
        
        fig, ax = plt.subplots()
        
        def atualizar(event):
            nonlocal self
            self.pos = nx.spring_layout(self.grafo, pos=self.pos)  # Atualiza posição sem erro
            ax.clear()
            nx.draw(self.grafo, self.pos, with_labels=True, node_color=[cores[n] for n in self.grafo.nodes],
                    node_size=700, edge_color="black", linewidths=1, font_size=10, ax=ax)
            labels = nx.get_edge_attributes(self.grafo, 'weight')
            nx.draw_networkx_edge_labels(self.grafo, self.pos, edge_labels=labels, ax=ax)
            plt.draw()
        
        fig.canvas.mpl_connect('button_press_event', atualizar)
        atualizar(None)
        plt.show()

if __name__ == "__main__":
    grafo = GrafoColoracao()
    
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