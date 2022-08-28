from xmlrpc.server import SimpleXMLRPCServer

def peso_ideal(altura, sexo):  
        
    if sexo == "masculino":
        peso = (72.7 * altura) - 58
        return (peso)
     
    elif sexo == "feminino":
        peso = (62.1 * altura) - 44.7
        
server = SimpleXMLRPCServer(("127.0.0.1", 4000))
print("Listening on port 4000...")
server.register_function(peso_ideal, 'peso_ideal')


server.serve_forever()


