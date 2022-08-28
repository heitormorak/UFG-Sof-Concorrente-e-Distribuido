import xmlrpc.client
 
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:4000/")
   
print("Digite a altura: ")
altura = float(input())
 
print("Digite o sexo:")
sexo = str(input())

resposta = proxy.peso_ideal(altura, sexo)
 
print(resposta)
