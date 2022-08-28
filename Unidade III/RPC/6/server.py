from xmlrpc.server import SimpleXMLRPCServer

def calculo_salario(nome, nivel, salario_bruto, dependentes):  
        
    if (nivel == "A"):
        if (dependentes == 0):
            salario_liquido = salario_bruto - (salario_bruto*0.03)
        else:
            salario_liquido = salario_bruto - (salario_bruto*0.08)
        return (salario_liquido)
    
    if (nivel == "B"):
        if (dependentes == 0):
            salario_liquido = salario_bruto - (salario_bruto*0.05)
        else:
            salario_liquido = salario_bruto - (salario_bruto*0.1)
        return (salario_liquido)
    
    if (nivel == "C"):
        if (dependentes == 0):
            salario_liquido = salario_bruto - (salario_bruto*0.08)
        else:
            salario_liquido = salario_bruto - (salario_bruto*0.15)
        return (salario_liquido)
    
    if (nivel == "D"):
        if (dependentes == 0):
            salario_liquido = salario_bruto - (salario_bruto*0.1)
        else:
            salario_liquido = salario_bruto - (salario_bruto*0.17)
        return (salario_liquido)  
    
        
server = SimpleXMLRPCServer(("127.0.0.1", 4000))
print("Listening on port 4000...")
server.register_function(calculo_salario, 'calculo_salario')


server.serve_forever()


