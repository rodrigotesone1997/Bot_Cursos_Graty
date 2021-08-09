from Bot.twitterbot import *
from Bot.telegrambot import *

# Las lineas comentadas son solo por si es necesario debugear

if __name__ == "__main__":
    twbot = twitterbot()
    tgbot = telegrambot()

    success = twbot.cargarLlaves("Bot_Cursos_Graty/keys")
#    print(success)
    success = success and tgbot.cargarLlaves("Bot_Cursos_Graty/keys")
#    print(success)
    if success:

        idCurso = twbot.hayCursos()
#        print(idCurso)
        if idCurso > 0:
            twbot.responderTweet(idCurso)
            twbot.retweetear(idCurso)
            tgbot.enviarAlCanal(idCurso)
            twbot.enviarMensaje(idCurso)
    else:
        tgbot.notificarRodrigo()