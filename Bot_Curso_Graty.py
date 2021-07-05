# Importo los paquetes necesarios

import tweepy # Paquete para interactuar con la api de twitter
import re # Paquete para utilizar expresiones regulares
from datetime import datetime # Paquete para utilizar funciones de tiempo
import pytz # Obtiene fecha y hora en distintos paises
import time # Da funciones para poner un delay artificial
import json # Da funcionalidades para manipular archivos json

# Declaro como strings todas las llaves necesarias para interactuar con la apí de twitter
# Para obtenerlas se necesita tener una cuenta developer en twitter

path_folder_cursos_graty="path/Bot_Curso_Graty/"

with open(path_folder_cursos_graty+"keys_bot_cursos_graty.json","r") as f:
    loaded_keys=json.loads(f.read())

consumer_key=loaded_keys["consumer_key"]

consumer_secret=loaded_keys["consumer_secret"]

access_token=loaded_keys["access_token"]

access_token_secret=loaded_keys["access_token_secret"]

# Utilizo las llaves para autenticar los request y acceder a la api de twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# El parametro define cuantos twetts van a leerse en la iteracion

parametro=25
tweets_cargados=parametro+1

# Abro el archivo "id.txt" y obtengo la primera linea que es el id del ultimo twitt que contenia las
# palabras clave "CURSOS GRATY"

path=path_folder_cursos_graty+"id.txt"
with open(path,"r") as f:
    lista_lineas=f.readlines()
ultimo_id=lista_lineas[0].replace("\n","")

# =============================================================================
# Obtengo el id, el url y el texto de los ultimos 25 twetts en cada iteracion.
# Si la palabra clave se encuentra en el tweet comparo el id de ese twett con el ultimo id registrado.
# En caso de ser iguales significa que el bot ya notifico del twett y si no son iguales significa que es
# una nueva publicacion que contiene la palabra clave.
# Al mismo tiempo se exige que el url sea no nulo ya que si ese fuera el caso se trataria de un retwett
# de una publicacion que contiene la palabra clave y no una publicacion original.
# Si el twett cumple ambas condiciones se reescribe el id por el nuevo id, 
# comenta la publicacion para publicitarse, retwitea la publicacion y envia un 
# mensaje a todos los seguidores del bot avisando que hay
# nuevos "CURSOS GRATY".
# Por ultimo se abre "id.txt" y se escribe el id del ultimo twett con la palabra "CURSOS GRATY" para evitar
# que el bot notifique 2 o mas veces la misma publicacion
# =============================================================================

for numero in range(parametro):
    user_object=api.user_timeline(screen_name="AgustinaLocke",tweet_mode="extended",count=tweets_cargados)[numero]
    tweet_actual=user_object._json["full_text"]
    _id=user_object._json["id"]
    _id_str=user_object._json["id_str"]
    try:
        url=api.user_timeline(screen_name="AgustinaLocke",count=tweets_cargados)[numero]._json["entities"]["urls"][0]["expanded_url"]
    except:
        url=""

    palabra_clave="CURSOS GRATY"
    if re.search(palabra_clave,tweet_actual) is not None :
        
        _id_viejo=ultimo_id
        _id_nuevo=_id_str
        
        if (_id_viejo != _id_nuevo ) and (url != ""):
            with open(path,"w") as f:
                f.write(_id_nuevo)
            api.update_status("Si queres que te avise cuando Agus publique \"CURSOS GRATY\" dame \"Follow\", activa la campanita y yo me voy a encargar de avisarte.\nLee mi tweet fijado.",in_reply_to_status_id=_id,auto_populate_reply_metadata=True)
            api.retweet(_id)
            dia=str(datetime.now(pytz.timezone('America/Buenos_Aires')).day)
            mes=str(datetime.now(pytz.timezone('America/Buenos_Aires')).month)
            screen_name = "BotFuturo"
            cursor_followers=tweepy.Cursor(api.followers,screen_name).items()
            url_curso="https://twitter.com/AgustinaLocke/status/"+_id_nuevo
            for follower in cursor_followers:
                text=f"Hola, el dia {dia}/{mes} @AgustinaLocke esta hablando de \"CURSOS GRATY\"\n\n¡Apurate a inscribirte!\n\n"+url_curso
                try:
                    direct_message=api.send_direct_message(follower._json["id"],text)
                    direct_message.message_create["message_data"]["text"]
                    time.sleep(2)
                    
                except:
                    pass
            break
        else:
            pass