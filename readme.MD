Objetivo do Case

Construir uma API que permita o cadastro de pessoas e realize operações como, consulta, atualização e exclusão desses registros.

Desenvolviemnto do case:

Optei por desenvolver o case com o framework Django que ja tenho uma familiaridade por ja posssuir uma interface para testes.

Para iniciar o projeto é necessário a instalação de algumas dependências que estão armazenadas no arquivo requirements.txt, para isso basta executar o comando a baixo no terminal:

''' pip install -r requirements.txt '''


Agora vamos configurar o ambiente virtual do projeto, para isso é necessário criar e ativar a venv, com o comando abaixo:

''' python3 -m venv ./venv '''

''' source venv/bin/activate''' (Mac e Linux)

''' venv\Scripts\activate.bat''' (Windows)

E por ultimo só rodar o comando para iniciar a aplicação:

''' python manage.py runserver'''

