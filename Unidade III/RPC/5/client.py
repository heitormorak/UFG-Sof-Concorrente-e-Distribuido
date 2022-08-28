import xmlrpc.client
 
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:4000/")
   
print("Digite a idade: ")
idade = int(input())
 

resposta = proxy.classificaçao(idade)
 
print(resposta)
