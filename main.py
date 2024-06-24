import qr

#exemplo de uso:

#Criando a mensagem
#Caso não passe um path, será criado um path padrão a onde esse projeto
#foi baixado
qr.qrcode_mensagem("teste")

#Desifrando a mensagem
#Necessita de um path, mas como o passo anterior, ele usa um path padrão para 
#encontrar a mensagem
qr.qrcode_desifrar_mensagem()

#OBS: toda vez que usar a função "qrcode_mensagem", vai ser criado um QRcode.
#Isso significa que um novo png sera criado sempre, com a mesma mensagem.