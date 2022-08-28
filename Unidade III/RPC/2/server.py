from xmlrpc.server import SimpleXMLRPCServer
 
def maior_idade(nome, sexo, idade):
 
    if (sexo == "masculino"):        
        if (idade >= 18):
            return ("maior de idade")
        else:
            return ("nao é maior de idade")
       
       
    elif (sexo == "feminino"):
        if (idade >= 21):
            return ("maior de idade")
        else:
            return ("nao é maior de idade")
   
server = SimpleXMLRPCServer(("127.0.0.1", 4000))
print("Listening on port 4000...")
server.register_function(maior_idade, 'maior_idade')
 
server.serve_forever()
