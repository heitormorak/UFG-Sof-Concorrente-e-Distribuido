import xmlrpc.client
 
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:4000/")
   
print("Digite o nome: ")
nome = str(input())

print("Digite o nível: ")
nivel = str(input())

print("Digite o salario bruto: ")
salario_bruto = float(input())

print("Digite o número de dependentes: ")
dependentes = int(input())
 

resposta = proxy.calculo_salario(nome, nivel, salario_bruto, dependentes)
 
print(resposta)
