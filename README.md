<h1 align="center">Bienvenido 👋</h1>
<p>
  <a href="ss" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/BotFuturo?s=08" target="_blank">
    <img alt="Twitter: Agus Bot" src="https://img.shields.io/twitter/follow/BotFuturo.svg?style=social" />
  </a>
</p>

> El repositorio consta de:
> - El script [app.py](app.py) que ejecuta las tareas para el funcionamiento del programa.<br/>
> - 2 clases (una para las funcionalidades de [twitter](Bot/twitterbot.py) y otra para las funcionalidades de [telegram](Bot/telegrambot.py))
> - Un block de notas que se encarga de anotar el ID del último tweet que dice **"CURSOS GRATY"**. <br/>
> El bot detecta la palabra "CURSOS GRATY" en los twetts de Agustina Loker y en caso de que aparezca esa palabra clave envia el siguiente [mensaje](Ejemplo_Bot_Mensaje.jpeg).
> - Las [claves de acceso](keys.dat) para utilizar la api de twitter y telegram.


## 📂 Clonar Reposotorio

```

git clone https://github.com/rodrigotesone1997/Bot_Cursos_Graty.git

```

## 🐍 Versión de Python

```
Python 3.8.5
```

## 👨‍💻 Instalación
Además de los requerimientos que estan [aquí](requirements.txt) se necesita tener una [cuenta developer](https://developer.twitter.com/en/apply-for-access) en twitter que proporcione las llaves de acceso para utilizar el script.
Mas información al respecto en https://developer.twitter.com/en/apply-for-access.

## ⚙️ Uso

1. (Opcional) Crear un entorno virtual `virtualenv` y activarlo.
2. Instalar las depedencias `pip install -r requirements.txt`
3. Leer el código y ver los comentarios para ver su uso.
4. Ejecutar [app.py](app.py)

## 🤔 ⏰ ¿Como hago para que el bot este continuamente activado?

#### 🪟 Usuarios Windows:

Para usuarios Windows conviene ejecutar el script dentro del [Task Scheduler](https://www.jcchouinard.com/python-automation-using-task-scheduler/) y ejecutar cada un minuto.

#### 🐧 Usuarios Linux:

Para usuarios Linux (yo particularmente uso la distribucion Ubuntu 20.04 pero supongo sera similar el proceso para otras distros) se recomienda utilizar [Crontab](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804) con el siguiente comando:
> crontab -e

y luego utilizar:<br />

> \* \* \* \* \* python3 /path/script/app.py

#### ☁️ Otras practicas:

Tambien se puede poner en produccion el script en un servidor externo como por ejemplo:

- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Google Cloud](https://cloud.google.com/)

Y muchos más.</br>
Yo tengo el bot corriendo en un maquina virtual en la plataforma [AWS](https://aws.amazon.com/)

## 🔮 Futuro del Proyecto

Planeo publicar un script que utlize Selenium para automatizar la inscripción a los cursos.</br>
UPDATE: Ya que el navegador debe estar siempre activado y desbloquedo para poder hacer uso de este script perdi interes en desarrollar el proyecto. Tampoco encontre una API para poder inscribirse a cursos en bases de request.

## ✉️ Contacto

Cualquier sugerencia de arquitectura de código,pregunta o problema enviar mail a rodrigotesone97@outlook.com.ar o a mi [twitter](https://twitter.com/rodrigotesone97)

## 🤔 Autor

👤 **Rodrigo Tesone**

<!---* Website: xadec
-->
* Twitter: [@rodrigotesone97](https://twitter.com/rodrigotesone97)
* Github: [rodrigotesone1997](https://github.com/rodrigotesone1997)
<!---* LinkedIn: [@ff](https://linkedin.com/in/ff)
-->

👤 **Federico Locker**

* Website: [https://fedeloker.com.ar](https://fedeloker.com.ar/?i=1)
* Twitter: [@FedeLoker](https://twitter.com/FedeLoker)
* Github: [FedeLoker](https://github.com/FedeLoker)
* LinkedIn: [@fedeloker](https://www.linkedin.com/in/fedeloker/)

## 🤝 Contribuciones y Agradecimientos

Agradezco a [Agustina Loker](https://twitter.com/AgustinaLocke) por su trabajo publicando los cursos, a Fede por sus idea del grupo de telegram y la arquitectura del codigo y a mi hermana por la linda imagen del perfil de twitter.

## 📝 Licencia

Copyright © 2021 [Rodrigo](https://github.com/rodrigotesone1997).<br />
This project is [MIT](LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
