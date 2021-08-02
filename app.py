from Bot.twitterbot import *
from Bot.telegrambot import *

if __name__ == "__main__":
    twbot = twitterbot()
    tgbot = telegrambot()

    success = twbot.cargarLlaves("keys")
    success = success and tgbot.cargarLlaves("keys")

    if success:

        idCurso = twbot.hayCursos()

        if idCurso > 0:
            twbot.responderTweet(idCurso)
            twbot.retweetear(idCurso)
            tgbot.enviarAlCanal(idCurso)
            twbot.enviarMensaje(idCurso)
    else:
        tgbot.notificarRodrigo()