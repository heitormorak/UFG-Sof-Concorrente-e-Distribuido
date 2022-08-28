import xmlrpc.client
 
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:4000/")
   
print("Digite o saldo medio: ")
saldo_medio = float(input())


resposta = proxy.credito(saldo_medio)
 
print(resposta)
