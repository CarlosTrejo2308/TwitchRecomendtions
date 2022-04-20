import requests
from twitch import TwitchClient, TwitchHelix


# Esta es la forma en la que se obtiene el numero de seguidores en base al id de usuario

#cantidad = client.channels.get_by_id(31894912)
# print(cantidad["followers"])

# En esta funcion se toma el usuario de twitch para regresar una lista con las personas que sigue
def canales_de_cliente(username):
    helix = TwitchHelix(client_id='vnsbdjciw4fcif1k57w1c07a65wk03',
                        oauth_token='oauth:17qyf4koyvfdqjs4me7zr451lccmtn')
    HEADS = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": "vnsbdjciw4fcif1k57w1c07a65wk03"
        # "Authorization" : "OAuth 17qyf4koyvfdqjs4me7zr451lccmtn"
    }
    nombre = username
    URL = "https://api.twitch.tv/kraken/users?login={}".format(nombre)
    r = requests.get(url=URL, headers=HEADS)
    temp = r.json()
    id = temp["users"][0]["_id"]
    print(id)
    namefollows = []
    t = helix.get_user_follows(from_id=id)
    namefollows = []
    for i in t:
        namefollows.append(i["to_id"])
    # print(namefollows)
    return namefollows

#canales = canales_de_cliente("albertto1198")
#print("Estos son tus canales")
# print(canales)
#####################################################################################################################################################################

# En esta funcion seda el nombre del ususario para obtener su id de twitch


def name_to_id(nombre):
    helix = TwitchHelix(client_id='vnsbdjciw4fcif1k57w1c07a65wk03',
                        oauth_token='oauth:17qyf4koyvfdqjs4me7zr451lccmtn')
    HEADS = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": "vnsbdjciw4fcif1k57w1c07a65wk03"
        # "Authorization" : "OAuth 17qyf4koyvfdqjs4me7zr451lccmtn"
    }
    #print("Favor de ingresar su usuario de Twitch")
    name = nombre
    URL = "https://api.twitch.tv/kraken/users?login={}".format(name)
    r = requests.get(url=URL, headers=HEADS)
    temp = r.json()
    id = temp["users"][0]["_id"]
    return id

#####################################################################################################################################################################

# En esta funcion se toman dos Streamers de cada Streames que sigues para agregarlos a la lista de evaluacion


def agrupacioncanales(lista):
    channels = lista
    lista_por_canal = []
    for i in range(0, len(channels)):
        name = channels[i]
        print(name)
        listname = canales_de_cliente(name)
        for j in range(0, 2):
            lista_por_canal.append(listname[j])
    print(lista_por_canal)
    return lista_por_canal

#prueba2 = agrupacioncanales(canales)
#print("estos se van a evaluar")
# print(prueba2)
# print(len(prueba2))

#####################################################################################################################################################################

# En esta funcion se crea una lista donde se guardaran el numero de usuarios que siguen a cada Streamer de la lista generada en la funcion agrupacioncanales


def evaluacion(lista):
    client = TwitchClient(client_id='vnsbdjciw4fcif1k57w1c07a65wk03',
                          oauth_token='oauth:17qyf4koyvfdqjs4me7zr451lccmtn')
    HEADS = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": "vnsbdjciw4fcif1k57w1c07a65wk03"
        # "Authorization" : "OAuth 17qyf4koyvfdqjs4me7zr451lccmtn"
    }
    listaaevaluar = lista
    print("Lista antes de ser modificada para recomendar")
    print(listaaevaluar)
    lista_nombres = []
    lista_seguidores = []
    for i in range(0, len(listaaevaluar)):
        # Se toma el nombre del Streamer para obtener el numero de seguidores
        nombreStreamer = listaaevaluar[i]
        print("nombre de streamer", nombreStreamer)
        idStreamer = name_to_id(nombreStreamer)
        print("id de Streamer", idStreamer)
        lista_nombres.append(nombreStreamer)
        print("lista de nombres")
        print(lista_nombres)
        # Aqui se obtienen los datos para sacar el numero de seguidores
        seguidoresStreamer = client.channels.get_by_id(idStreamer)
        # Aqui se obtiene el numero de seguidores
        lista_seguidores.append(seguidoresStreamer["followers"])
        print("Lista de numero de seguidores")
        print(lista_seguidores)
    #print("esta es la lista a evaluar")
    # print(listaaevaluar)
    #print("esta es la lista de nombres")
    # print(lista_nombres)
    # print("----------------------------------------------------------------------------------")
    # print(len(lista_nombres))
    #print("Esta es la lista con numero de seguidores")
    # print(lista_seguidores)
    # print("----------------------------------------------------------------------------------")
    # print(len(lista_seguidores))
    # ya que no se pueden regresar dos listas en un return agregue la lista de los nombres y de los seguidores en una sola lista
    listas = [lista_nombres, lista_seguidores]
    return listas

#####################################################################################################################################################################

# En esta funcio se toma la lista del metodo evaluacion para regresar una lista de N recomendaciones para el usuario final


def recomendaciones(lista):
    nombres = lista[0]
    numeros = lista[1]
    lista_temporal = []
    lista_recomendados = []
    lista_num_seguidores = []
    for i in range(0, len(numeros)):
        lista_temporal.append(int(numeros[i]))
    # Esto simula un Do/While para poder crear el ciclo donde se va tomando el Streamer con mayor numero de seguidores
    j = 1
    while True:
        num_mayor = max(lista_temporal)
        posicion = lista_temporal.index(num_mayor)
        lista_recomendados.append(nombres[posicion])
        lista_num_seguidores.append(num_mayor)
        print("El Streamer {} ha sido agregado a las recomendaciones".format(
            nombres[posicion]))
        j = j + 1
        lista_temporal.pop(posicion)
        nombres.pop(posicion)
        if(j > 11):
            break
    # for i in range(0, len(numeros)):
    #    lista_temporal.append(int(numeros[i]))--
    #    num_mayor = max(lista_temporal)--
    #    print(num_mayor)
    #    posicion = lista_temporal.index(num_mayor)--
    #    lista_recomendados.append(nombres[posicion])
    #    print("la posicion en la que esta el numero mayor es: ", posicion)
    #    print("El nombre del Streamer es: ", nombres[posicion])
    #    streamerR_seguidores = lista_temporal.pop(posicion)
    #    streamer_recomendado = nombres.pop(posicion)
    #    print("STREAMER RECOMENDADO: ", streamer_recomendado)
    #    print("seguidores de Streamer recomendado: ", streamerR_seguidores)

    # print(lista_recomendados)
    # print(lista_num_seguidores)
    return lista_recomendados


#####################################################################################################################################################################

def ban_list(lista):
    client = TwitchClient(client_id='vnsbdjciw4fcif1k57w1c07a65wk03',
                          oauth_token='oauth:17qyf4koyvfdqjs4me7zr451lccmtn')
    HEADS = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": "vnsbdjciw4fcif1k57w1c07a65wk03"
        # "Authorization" : "OAuth 17qyf4koyvfdqjs4me7zr451lccmtn"
    }
    recomendados = lista
    lista_baneados = []
    j = 0
    while True:
        id_streamer = name_to_id(recomendados[j])
        print("id de Streamer")
        print(id_streamer)
        baneados = client.users.get_user_block_list(id_streamer)
        lista_baneados.append(baneados)
        if(j > len(recomendados)):
            break
    print(lista_baneados)
    return lista_baneados


def main():
    # Aqui debe de estar el input() para que el cliente ponga su nombre de twitch
    canales = canales_de_cliente("Delt4Forc3")
    print("Estos son tus canales")
    print(canales)


"""
    prueba2 = agrupacioncanales(canales)
    print("estos se van a evaluar")
    print(prueba2)

    evaluation = evaluacion(prueba2)

    streamers = recomendaciones(evaluation)

    print("RECOMENDACIONES")
    print(streamers)

    #lista_baneados = ban_list(streamers)

    #print("Listas de baneados")
    #print(lista_baneados)"""
if __name__ == "__main__":
    main()
