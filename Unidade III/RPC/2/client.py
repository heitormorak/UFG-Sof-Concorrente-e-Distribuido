import xmlrpc.client
 
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:4000/")
   
print("Digite o nome: ")
nome = str(input())
 
print("Digite o sexo:")
sexo = str(input())
 
print("Digite a idade:")
idade = int(input())
 
resposta = proxy.maior_idade(nome, sexo, idade)
 
print(resposta)
