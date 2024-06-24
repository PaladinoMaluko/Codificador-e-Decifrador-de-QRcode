import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import os

def qrcode_mensagem(mensagem:str,path:str=None) -> None:
    """
    Cria um QRCode com a mensagem especificada e salva no caminho fornecido.

    :param mensagem: A mensagem para ser codificada no QRCode.
    :param path: O caminho do arquivo onde o QRCode será salvo.
    :raises ValueError: Se a mensagem não for uma string.
    """
    try:
        #caso o path não possue valor (none), crie um caminho padrão
        if path is None:
            path = os.path.join(os.getcwd(),"qrcode_pasta")
            #evitando que crie a mesma pasta denovo
            if not os.path.exists(path):
                os.makedirs(path)

        #confirmando se os parametros são str
        if not isinstance(mensagem,str):
            raise ValueError("A função qrcode_mensage espera uma string como argumento: mensagem")
        if not isinstance(path,str):
            raise ValueError("A função qrcode_mensage espera uma string como argumento: path")
        
        # criando o caminho completo para pasta
        caminho_completo = os.path.join(path, "qrcode.png")
        file_name = caminho_completo 

        #inicializando a variavel que modifica o nome
        num = 0

        #verifico se existe nome igual na pasta
        while os.path.exists(file_name):
            #caso o nome for igual, adicione +1
            num += 1
            file_name = f"{caminho_completo}_({num}).png"
        
        #crio a imagem na pasta com a mensagem
        data = mensagem
        img = qrcode.make(data)
        img.save(file_name)
        print(f"Arquivo criado na pasta: {path}")

    #verificação de possiveis erros 
    except ValueError as e:
        raise ValueError(f"Erro ao criar QRCode ==> {e}")
    except OSError as e:
        print(f"Erro de sistema ao criar QRCode ==> {e}")

def qrcode_desifrar_mensagem(path:str=None,mostrar_nome_arquivo:bool=False) -> None:
    """
    Procura um QRCode e desifra sua mensagem no caminho fornecido.

    :param path: O caminho do arquivo onde o QRCode está salvo.
    :mostrar_nome_arquivo: Mostra o nome do arquivo.
    """
    try:
        #caso o path não possue valor (none), pegue o caminho padrão
        if path is None:
            path = os.path.join(os.getcwd(),"qrcode_pasta")

        if not isinstance(path,str):
            raise ValueError("A função qrcode_mensage espera uma string como argumento: path")
        
        # Verifica se o diretório existe
        if not os.path.exists(path):
            raise ValueError(f"O caminho especificado não existe: {path}")

        #variavel que controla se algum arquivo foi encontrado
        arq_encontrado = False

        for diretorio, subpastas, arquivos in os.walk(path):
            for arq in arquivos:
                arq_encontrado = True
                try:
                    img = os.path.join(diretorio,arq)
                    img_open = Image.open(img)

                    result = decode(img_open)
                    
                    if result:
                        # Exibe a mensagem decodificada
                        for obj in result:
                            if mostrar_nome_arquivo:
                                print(f"Arquivo: {arq}")
                            print(f"Mensagem decodificada: {obj.data.decode('utf-8')}")

                except (OSError, IOError) as e:
                    print(f"Erro ao abrir ou processar a imagem {arq}: {e}")
        
        if not arq_encontrado:
            print(f"Nenhum arquivo foi encontrado no caminho especificado: {path}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    qrcode_mensagem("oi")
    qrcode_desifrar_mensagem()