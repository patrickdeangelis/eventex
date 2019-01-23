# Eventex 
[![Build Status](https://travis-ci.org/patrickdeangelis/eventex.svg?branch=master)](https://travis-ci.org/patrickdeangelis/eventex)

sistema de eventos encomendado pela morena

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv com Python 3.7
3. Ative o seu virtualenv
4. Instale as dependecias
5. Configure a instancia com o .env
6. Execute os testes

```console
git clone git@github.com:patrickdeangelis/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requiriments-dev.txt
cp contrib/env-sample.env
python manage.py test
```

## como fazer o deploy?
1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=True
5. Configure o serviço de email
6. envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configura o email
git push heroku master --force
```      