path = "fluxo-de-veiculo.csv"
content = []
filtered = []
#Primeira parte, abrir o arquivo e organizar em um array de arrays, cada array contem [local, data, hora, qtds de varios veiculos]
with open(path, 'r') as excel:
	line = excel.readline()
	content.append(line)
	cnt = 1
	while line:
		line = excel.readline()
		content.append(line)
		filtered.append(content[cnt].split(';'))
		cnt+=1


#Arrays de suporte 
a_logra = []
a_inter = []
a_nomes = []
a_nomes.append(filtered[0][0])

#Segunda parte, preencher os arrays de suporte com informações mais organizadas separar um array para cada local
for i in range(len(content)-2):
	fluxo = 0
	nome = filtered[i][0]

	if i>0:
		if(filtered[i][0] != filtered[i-1][0]):
			a_nomes.append(filtered[i][0])
			a_logra.append(a_inter)
			a_inter = []
	for k in range(3,12):
		fluxo+= int(filtered[i][k])
	a_inter.append([filtered[i][1]+" "+filtered[i][2], fluxo])


#Terceira parte, filtrar as informações, pegar a data e o horario mais movimentado em cada um dos locais e jogar em um .txt de saida
maxi = 0
index = 0
out = open('out.txt', 'w')
for local in range(len(a_logra)-1):
	for data in range(3,len(a_inter)):
		#Pega 4 intervalos de 15min, 1 hora, em todos os dias para decidir qual foi o dia/horario mais movimentado daquele local
		temp = int(a_logra[local][data][1] + a_logra[local][data-1][1] + a_logra[local][data-2][1] + a_logra[local][data-3][1])
		if temp > maxi:
			maxi = temp
			index = data
	
	out.write(a_nomes[local]+" Hora: "+str(a_logra[local][index-3][0])+" ate "+ str(a_logra[local][index][0])+" Fluxo: "+str(maxi)+"\n")
	maxi = 0 
	temp = 0
out.close()	
