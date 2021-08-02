import json # Paquete que permite manipular archivos .dat y .json
import requests # Paquete para hacer requests

class telegrambot:

    def cargarLlaves(self,name):
        
        # Leer el .dat
        
        retorno = False
        try:
            with open(name + ".dat", "r") as f:
                loaded_keys = json.loads(f.read())
            self.id_grupo=loaded_keys["id_Grupo_Telegram"] # Grupo Telegram
            self.token_telegram=loaded_keys["token_telegram"] # Acceso al bot
            self.id_Rodrigo=loaded_keys["id_Rodrigo"] # Rodrigo
            retorno = True
        except:
            pass
        return retorno
    
    def enviarAlCanal(self, id_tweet):
        
        url_curso="https://twitter.com/AgustinaLocke/status/"+str(id_tweet)
        mensaje=f"Agus esta hablando de **\"CURSOS GRATY\"**\nEntra [acá]({url_curso}) para inscribirte"
        texto="https://api.telegram.org/bot"+self.token_telegram+"/sendMessage?chat_id="+self.id_grupo+"&parse_mode=MarkdownV2&text="+mensaje
        
        response=requests.get(texto)
        
        return response.json()

    def notificarRodrigo(self):
        
        mensaje = "Las llaves no se cargaron"
        texto="https://api.telegram.org/bot"+self.token_telegram+"/sendMessage?chat_id="+self.id_Rodrigo+"&parse_mode=MarkdownV2&text="+mensaje
        
        response=requests.get(texto)
        
        return response.json()