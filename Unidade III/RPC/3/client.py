import xmlrpc.client
 
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:4000/")
   
print("Digite a n1: ")
n1 = int(input())
 
print("Digite a n2:")
n2 = int(input())
 
print("Digite a n3:")
n3 = int(input())
 
resposta = proxy.notas(n1, n2, n3)
 
print(resposta)
