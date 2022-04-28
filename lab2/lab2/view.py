import controller
from model import LinkedList

def main():
    countryList = LinkedList()

    while True:
        commands = input().split()

        if commands[0] == "RPI":
            countryList.push(commands[1])

            for x in countryList:
                #print de todos os elementos

        #if commands[0] == "RPF":
        #if commands[0] == "RPDE":
        #if commands[0] == "RPAE":
        #if commands[0] == "RPII":

        if commands[0] == "VNE":

            número_elementos = len(countryList)
            print(f"O número de elementos são {número_elementos}.")
        
        if commands[0] == "VP":
            nome_país = [1]

            if nome_país in countryList:
                print(f"O país {nome_país} encontra-se na lista.")
            else:
                print(f"O país {nome_país} não se encontra na lista.")

        if commands[0] == "EPE":

            nome_país_eliminado = countryList.push(commands[1])
            print(f"O país {nome_país_eliminado} foi eliminado da lista.")

        if commands[0] == "EUE":

            nome_país_eliminado = countryList.append
            print(f"O país {nome_país_eliminado} foi eliminado da lista.")

        if commands[0] == "EP":
            nome_país = [1]

            if nome_país in countryList:
                print(f"O país {nome_país_eliminado} foi eliminado da lista.")
            else:
                print(f"O país {nome_país_eliminado} não se encontra na lista.")
