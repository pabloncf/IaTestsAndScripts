# Instalar a biblioteca: pip install --upgrade pyqt5 lxml

import os
import subprocess  # serve para rodar comandos de terminal no python

LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')

subprocess.run("pip install --upgrade pyqt5 lxml", shell=True)

if not os.path.exists(LABELIMG_PATH):
    subprocess.run(f"mkdir {LABELIMG_PATH}", shell=True)
    subprocess.run(  # esse comando roda comando de terminais dentro do python. Lembrando que funciona apenas se os caracteres sejam separados com "" e ,
        ["git", "clone", "https://github.com/tzutalin/labelImg", LABELIMG_PATH], shell=True
    )

if os.name == 'posix':
    # Aqui, usamos uma f-string para inserir o valor da variável LABELIMG_PATH na string do comando. O argumento shell=True é usado para executar o comando em um shell, o que permite o uso do operador && para executar vários comandos consecutivamente.
    subprocess.run(f"cd {LABELIMG_PATH} && make qt5py3", shell=True)
if os.name == 'nt':
    subprocess.run(
        f"cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc", shell=True)

subprocess.run(f"cd {LABELIMG_PATH} && python labelImg.py", shell=True)
