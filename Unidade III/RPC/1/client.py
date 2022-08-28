import xmlrpc.client
 
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:4000/")
 
print("Digite o nome do funcionario:")
nome = str(input())
 
print("Digite o cargo do funcionario:")
cargo = str(input())
 
print("Digite o salario do funcionario:")
salario = int(input())
 
resposta = proxy.reajuste(nome,cargo,salario)
 
print(resposta)
