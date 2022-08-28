from xmlrpc.server import SimpleXMLRPCServer

def credito(saldo_medio):  
        
    if (saldo_medio >= 0) and (saldo_medio <= 200):
        return ("Nenhum crédito")
    
    elif (saldo_medio >= 301) and (saldo_medio <= 400):
        credito = saldo_medio + (saldo_medio*0.2)
        return (credito)
    
    elif (saldo_medio >= 401) and (saldo_medio <= 600):
        credito = saldo_medio + (saldo_medio*0.3)
        return (credito)
    
    elif (saldo_medio >= 601):
        credito = saldo_medio + (saldo_medio*0.4)
        return (credito)
    
        
server = SimpleXMLRPCServer(("127.0.0.1", 4000))
print("Listening on port 4000...")
server.register_function(credito, 'credito')


server.serve_forever()


