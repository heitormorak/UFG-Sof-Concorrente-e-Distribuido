from xmlrpc.server import SimpleXMLRPCServer

def classificaçao(idade):  
        
    if (idade >= 5) and (idade <= 7):
        return ("infantil A")
     
    elif (idade >= 8) and (idade <= 10):
        return ("infantil B")
    
    elif (idade >= 11) and (idade <= 13):
        return ("juvenil A")
    
    elif (idade >= 14) and (idade <= 17):
        return ("juvenil B")
    
    elif (idade >= 18):
        return ("adulto")
        
server = SimpleXMLRPCServer(("127.0.0.1", 4000))
print("Listening on port 4000...")
server.register_function(classificaçao, 'classificaçao')


server.serve_forever()


