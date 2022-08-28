from xmlrpc.server import SimpleXMLRPCServer

def aprosentar(idade, tempo):  
        
    if (idade >= 65) and (tempo >= 30):
        return ("Pode aposentar")
    
    elif (idade >= 60) and (tempo >= 25):
        return ("Pode aposentar")
    
    else:
        return ("Não pode aposentar")
    
        
server = SimpleXMLRPCServer(("127.0.0.1", 4000))
print("Listening on port 4000...")
server.register_function(aprosentar, 'aprosentar')


server.serve_forever()


