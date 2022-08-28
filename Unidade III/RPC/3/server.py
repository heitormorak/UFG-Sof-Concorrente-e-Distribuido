from xmlrpc.server import SimpleXMLRPCServer

def notas(n1, n2, n3):

    media = (n1 + n2)/2   
        
    if media >= 7:
        return ("aluno aprovado")
     
    elif ((media > 3) and (media < 7)):
        media = (media+n3)/2

        if media >= 5:
            return("aluno aprovado")
        else:
            return ("aluno reprovado")

    else:
        return ("aluno reprovado") 
              
server = SimpleXMLRPCServer(("127.0.0.1", 4000))
print("Listening on port 4000...")
server.register_function(notas, 'notas')


server.serve_forever()


