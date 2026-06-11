import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

while True:
    print("1 - Capital do país")
    print("2 - Nome do país") 
    print("3 - Código telefone do país")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        country_code = input("Digite o código do país:")
    
        payload = f"""<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                        <soap:Body>
                            <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                                <sCountryISOCode>{country_code}</sCountryISOCode>
                            </CapitalCity>
                        </soap:Body>
                    </soap:Envelope>"""

        headers = {
            'Content-Type': 'text/xml; charset=utf-8'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            dom = parseString(response.text)
            resultado = dom.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue
            print("A capital do país é:", resultado)
        
    elif opcao == "2":
        country_code = input("Digite o código do país:")

        payload = f"""<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                        <soap:Body>
                            <CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                                <sCountryISOCode>{country_code}</sCountryISOCode>
                            </CountryName>
                        </soap:Body>
                    </soap:Envelope>"""

        headers = {
            'Content-Type': 'text/xml; charset=utf-8'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            print("O nome do país é: " + parseString(response.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue)

    elif opcao == "3":
        country_code = input("Digite o código do país: ")

        payload = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <CountryIntPhoneCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>{country_code}</sCountryISOCode>
                </CountryIntPhoneCode>
            </soap:Body>
        </soap:Envelope>"""

        headers = {
            "Content-Type": "text/xml; charset=utf-8"
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            dom = parseString(response.text)
            resultado = dom.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue
            print("O código de telefone do país é:", resultado)

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")