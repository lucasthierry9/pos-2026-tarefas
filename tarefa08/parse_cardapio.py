from xml.dom.minidom import parse

dom = parse("cardapio.xml")

# Elemento raiz do XML (biblioteca)
cardapio = dom.documentElement

# Recebe uma lista dos elementos com tag "livro"
pratos = cardapio.getElementsByTagName('prato')

id_prato = 0
# Acessa as informações de cada livro
for prato in pratos:
    id_prato+=1
    descricao = prato.getAttribute('categoria')
    elemento_nome = prato.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue
    print(f'{id_prato} - {nome}')

id_lido = int(input("Digite o id do prato para saber mais: "))
prato = pratos[id_lido-1]
print("---\n")

elemento_nome = prato.getElementsByTagName('nome')[0]
nome = elemento_nome.firstChild.nodeValue
elemento_descricao = prato.getElementsByTagName('descricao')[0]
descricao = elemento_descricao.firstChild.nodeValue
elemento_preco = prato.getElementsByTagName('preco')[0]
preco = elemento_preco.firstChild.nodeValue
elemento_calorias = prato.getElementsByTagName('calorias')[0]
calorias = elemento_calorias.firstChild.nodeValue

print("Nome:", nome)
print("Descrição:", descricao)
print("Preço:", preco)
print("Calorias:", calorias)