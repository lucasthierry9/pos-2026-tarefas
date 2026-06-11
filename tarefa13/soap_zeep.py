import zeep

wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)
numero = input("Digite um número para transformar em escrito: ")

resultado = client.service.NumberToWords(ubiNum=numero)
print(f"O número {numero} em palavras é: {resultado}")
