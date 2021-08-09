# Importo los paquetes necesarios

import tweepy # Paquete para interactuar con la api de twitter
import re # Paquete para utilizar expresiones regulares
import json # Paquete que permite manipular archivos .dat y .json
from datetime import datetime # Paquete para manipular fechas
import pytz # Obtiene fecha y hora en distintos paises
import time # Paquete para usar funcionalidades de tiempo

class twitterbot:

    def __init__(self):

        # Variables globales

        self.tweets_cargados=25
        self.NombreDeUsuario = "AgustinaLocke"
        self.palabra_clave="CURSOS GRATY"
        self.path_bot_cursos_graty="your/path/Bot_Cursos_Graty/"

    def cargarLlaves(self,name):

        retorno = False

        try:
            with open(name + ".dat", "r") as f:
                loaded_keys = json.loads(f.read())
            auth = tweepy.OAuthHandler(loaded_keys['consumer_key'], loaded_keys['consumer_secret'])
            auth.set_access_token(loaded_keys['access_token'], loaded_keys['access_token_secret'])
            self.twAPI = tweepy.API(auth,wait_on_rate_limit=True)
            retorno = True
        except:
            pass
        return retorno

    def leerID(name):

        retorno = False

        try:
            file = open(name + ".txt","r",encoding = 'utf-8')
            lista_lineas=file.readlines()
            retorno = lista_lineas[0].replace("\n","")
        except:
            pass
        finally:
            file.close()
        return retorno

    def guardarID(id_,name):

        retorno = False

        try:
            file = open(name + ".txt","w")
            file.write(id_)
            retorno = True
        except:
            pass
        finally:
            file.close()
        return retorno

    def hayCursos(self):

        # Verifica si hay cursos nuevos
        # Si los hay retorna el id del tweet (como int)
        # Si no los hay retorna -1

        retorno=-1

        ultimo_id = twitterbot.leerID(self.path_bot_cursos_graty+"id")
        lista_tweets = self.twAPI.user_timeline(screen_name=self.NombreDeUsuario,tweet_mode="extended",count=self.tweets_cargados+1)

        for tweet in lista_tweets:
            if re.search(self.palabra_clave, tweet._json["full_text"]) and (re.search("^RT ",tweet._json["full_text"]) is None):
                id_str = tweet._json["id_str"]
                if (id_str != ultimo_id):
                    twitterbot.guardarID(id_str,self.path_bot_cursos_graty+"id")

                    retorno = tweet._json["id"]
        return retorno

    def responderTweet(self,id_tweet):

        # Respondo el tweet con el nuevo curso

        self.twAPI.update_status("Si queres que te avise cuando Agus publique \"CURSOS GRATY\" dame \"Follow\", activa la campanita y yo me voy a encargar de avisarte.\nRecorda leer el tweet fijado de Agus antes de preguntar por el idioma, como inscribirse y demas preguntas.",in_reply_to_status_id=id_tweet,auto_populate_reply_metadata=True)

    def retweetear(self, id_tweet):

        # Retweeteo el tweet con el nuevo curso

        self.twAPI.retweet(id_tweet)

    def enviarMensaje(self, id_tweet):

        # Notifica nuevos cursos por DM

        dia=str(datetime.now(pytz.timezone('America/Buenos_Aires')).day)
        mes=str(datetime.now(pytz.timezone('America/Buenos_Aires')).month)
        screen_name = "BotFuturo"
        cursor_followers=tweepy.Cursor(self.twAPI.followers,screen_name).items(1100)
        url_curso="https://twitter.com/AgustinaLocke/status/"+str(id_tweet)
        cantidad_request_fallidas=0
        for follower in cursor_followers:
            text=f"Hola, el dia {dia}/{mes} @AgustinaLocke esta hablando de \"CURSOS GRATY\"\n¡Apurate a inscribirte!\nRecorda leer el tweet fijado de Agus antes de preguntar por el idioma, como inscribirse y demas preguntas.\n\n"+url_curso
            try:
                direct_message=self.twAPI.send_direct_message(follower._json["id"],text)
                direct_message.message_create["message_data"]["text"]
                time.sleep(2.5)
            except:
                if cantidad_request_fallidas == 100:
                    break
                cantidad_request_fallidas+=1