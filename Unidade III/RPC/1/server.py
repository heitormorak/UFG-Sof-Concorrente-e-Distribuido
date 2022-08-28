from xmlrpc.server import SimpleXMLRPCServer
 
def reajuste(nome, cargo, salario):
 
    if cargo == "operador":
        salario = salario + (0.2 * salario)
    if cargo == "programador":
        salario = salario + (0.18 * salario)
   
 
    print("funcionario: " + nome + " novo salario: " + str(salario))
 
    return ("funcionario: " + nome + " novo salario: " + str(salario))
 
server = SimpleXMLRPCServer(("127.0.0.1", 4000))
print("Listening on port 4000...")
server.register_function(reajuste, 'reajuste')
 
server.serve_forever()
