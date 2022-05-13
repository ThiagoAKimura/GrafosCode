# Grupo M
# Nome: Gustavo das Flores Lima      RA: 22.221.041-1
# Nome: Thiago Ayres Kimura			 RA: 22.221.045-2
# Nome: Victor Garcia Zornek		 RA: 22.221.048-6
# Disciplina: Teoria dos Grafos


def main():
	arquivo = open("A.txt", "r")
	dados = arquivo.readlines()
	arquivo.close()
	for x in range(len(dados)):
		dados[x] = dados[x].split()
	
	dados = list(filter(None, dados)) # Remove os espaços em branco

	# Estrutura da exibição das perguntas e respostas no terminal chamando as funções criadas

	simples = grafo_simples(dados)

	existeGrafo, graus, soma_graus = sequen_graus(dados)
	if existeGrafo == 1:
		exit()

	numero_arestas(soma_graus)
	grafo_completo(dados, simples)
	grafo_regular(graus)

	bipartido, x, y = grafo_bipartido(dados)
	grafo_bipartido_completo(simples, bipartido, x, y)

def grafo_simples(matriz): # Função que verifica se o grafo é simples
	lacos, arestas_multiplas = verifica_lacos(matriz)

	print("="*60 + "\n")
	print("1) O grafo é simples? Indique se há arestas múltiplas  ou laços. Indique, também, entre que vértices as arestas múltipas ocorrem; em que vértices ocorrem laços\n")

	if lacos and arestas_multiplas:
		print("-> Este grafo não é simples pois possui arestas múltiplas e laços\n")
		imprime_lacos(lacos, arestas_multiplas)
		print("\n"+"="*60 + "\n")
		return 0

	elif lacos or arestas_multiplas:
		if lacos:
			print("-> Este grafo não é simples pois possui laços\n")

		if arestas_multiplas:
			print("-> Este grafo não é simples pois possui arestas múltiplas\n")

		imprime_lacos(lacos, arestas_multiplas)
		print("="*60 + "\n")
		return 0
	else:
		print("-> Este grafo é simples pois não possui arestas múltiplas nem laços\n")
		return 1

def sequen_graus(matriz): # Função que verifica a sequência de graus
	graus = []

	for linha in range(len(matriz)):
		graus.append(0)

		for coluna in range(len(matriz)):
			if linha == coluna:
				graus[linha] += (int(matriz[linha][coluna])*2)
			else:
				graus[linha] += int(matriz[linha][coluna])

	soma_graus = 0
	for valor in range(len(graus)):
		soma_graus += graus[valor]

	if soma_graus % 2 != 1:
		graus = ordem_decrescente(graus)
		print("2) Qual a sequência dos graus do grafo? Obs. Os graus devem estar em ordem não crescente \n")
		print("A sequência dos graus do grafo é:", end=" ")
		print(*graus, sep=", ")
		print()
		print("="*60 + "\n")
		return 0, graus, soma_graus
	else:
		print("Não é possível existir grafo")
		return 1, graus, soma_graus
	
def ordem_decrescente(graus): # Função que coloca os graus em ordem decrescente	
	graus = sorted(graus)  
	graus = graus[::-1]  
	return graus

def imprime_lacos(lacos, arestas_multiplas): # Função que imprime os laços e arestas múltiplas
	if lacos:
		print("-> Vértices que possuem laços:", end=" ")
		print(*lacos, sep=", ")
	else:
		print("\n-> O grafo não tem laços")

	if arestas_multiplas:
		print("\n-> Vértices que possuem arestas múltiplas:", end=" ")
		print(*arestas_multiplas, sep=", ")
	else:
		print("\n-> O grafo não tem arestas múltiplas")

def numero_arestas(soma_graus): # Função que verifica o número total de arestas do grafo
	arestas = soma_graus/2
	print("3) Qual o número de arestas do grafo? \n")
	print("Número total de arestas do grafo é:", int(arestas))
	print()
	print("="*60 + "\n")

def verifica_lacos(matriz):  # Função para verificar a existência de laços e arestas múltiplas no grafp
	lacos = []
	arestas_multiplas = []

	for linha in range(len(matriz)):
		for coluna in range(linha, len(matriz)):
			if linha == coluna and int(matriz[linha][coluna]) > 0:
				lacos.append("V{0}".format(linha+1)) # Adiciona o vértice na lista de laços
			elif int(matriz[linha][coluna]) > 1:
				arestas_multiplas.append("V{0} e V{1}".format(linha+1, coluna+1)) # Adiciona o vértice na lista de arestas múltiplas

	return lacos, arestas_multiplas

def grafo_completo(matriz, grafo_simples): # Função que verifica se o grafo é completo
	if grafo_simples == 1:
		completo = False
	else:
		completo = True

		for linha in range(len(matriz)):
			for coluna in range(len(matriz)):
				if linha == coluna and int(matriz[linha][coluna]) != 0:
					completo = False
					break
				elif linha != coluna and int(matriz[linha][coluna]) != 1:
					completo = False
					break
	print("4) O grafo é completo?\n")
	if completo:
		print("Sim, pois um grafo é completo quando todos os seus vértices possuem seu número máximo de arestas, ou seja, todos os vértices estão conectados entre si\n")
		print("="*60 + "\n")
	else:
		print("Não, pois um grafo só é completo se todos os seus vértices possuirem o número máximo possível de graus, o que não se aplica nesse caso\n")
		print("="*60 + "\n")

def grafo_regular(graus): # Função que verifica se o grafo é regular
	regular = 1
	for valor in graus:
		if graus[0] == valor:
			pass
		else:
			regular = 0
			break

	print("5) O grafo é regular?\n")
	if regular == 1:
		print("Sim, pois por definição, um grafo é regular se todos os seus vértices possuem o mesmo valor de graus\n")
		print("="*60 + "\n")
	else:
		print("Não, pois por definição, um grafo não é regular se os seus vértices possuem graus diferentes, como nesse caso\n")
		print("="*60 + "\n")

def imprime_biparticao(x, y): # Função que imprime a bipartição do grafo
	print("Bipartição:")
	print("X = {", end="")
	for i in x:
		if i == x[-1]:
			print("V{0}".format(i+1), end="}\n")
		else:
			print("V{0}".format(i+1), end=", ")

	print("Y = {", end="")
	for i in y:
		if i == y[-1]:
			print("V{0}".format(i+1), end="}\n")
		else:
			print("V{0}".format(i+1), end=", ")

def grafo_bipartido(matriz): # Função que verifica se o grafo é bipartido
	x = [0]
	y = []
	bipartido = 1

	for linha in range(len(matriz)):
		for coluna in range(len(matriz)):
			if linha in x and int(matriz[linha][coluna]) != 0 and coluna not in y:
				if coluna in x:
					bipartido = 0
				else:
					y.append(coluna)
			elif linha in y and int(matriz[linha][coluna]) != 0 and coluna not in x:
				if coluna in y:
					bipartido = 0
				else:
					x.append(coluna)

	print("6) O grafo é bipartido? Em caso afirmativo dê uma bipartição dos vértices do grafo\n")
	if bipartido == 1:
		print("Sim, é bipartido pois os vértices podem ser divididos em dois conjuntos distintos, tal que toda aresta conecta um vértice em U a um vértice em V, ou seja, U e V são conjuntos independentes")
		imprime_biparticao(x, y)
		print("\n"+"="*60 + "\n")
		return 1, x, y
	else:
		print("Não é bipartido pois os vértices não podem ser divididos em dois conjuntos distintos, tal que toda aresta conecta um vértice em U a um vértice em V, ou seja, U e V são conjuntos independentes")
		print("\n"+"="*60 + "\n")
		return 0, 0, 0

def grafo_bipartido_completo(grafo_simples, bipartido, x, y): # Função que verifica se o grafo é bipartido completo
	print("7) O grafo é bipartido completo? Em caso afirmativo dê uma bipartição dos vértices do grafo\n")
	
	if grafo_simples == 1 and bipartido == 1:
		print("Sim, pois para ser um grafo bipartido completo, cada um dos vértices em um conjunto deve se conectar com todos os outros vértices do outro conjunto")
		imprime_biparticao(x, y)
		print("\n"+"="*60 + "\n")
	else:
		print("Não, pois para ser um grafo bipartido completo, cada um dos vértices em um conjunto deve se conectar com todos os outros vértices do outro conjunto, o que não se aplica nesse caso")
		print("\n"+"="*60 + "\n")

main()