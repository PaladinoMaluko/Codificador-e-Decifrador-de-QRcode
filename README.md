# CODIFICADOR E DECODIFICADOR DE QRCODE

Este projeto consiste em um scripts em Python:
- `qr.py`: Gera um QR code a partir de uma mensagem.

## Requisitos
- versão do Python utilizada: 3.11.4
- Bibliotecas: `qrcode`, `pyzbar.pyzbar`,`PIL`,`os`

## Como Usar
- Primeiro lugar você deve criar uma mensagem, usando a função `qrcode_mensagem`
para criar uma mensagem
- Depois de criado, você pode desifrar a mensagem usando a função
`qrcode_desifrar_mensagem`

## Considerações
- Projeto simples, mas oferece uma boa noção de como criar arquivos utilizando
path
- Ajuda no entendimento de criar ecessões e evitar erros previsiveis(pasta não
existe, path não colocado, mensagem não colocada...)