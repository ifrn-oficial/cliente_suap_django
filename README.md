# Cliente SUAP Django

## Sobre

O **Cliente SUAP Django** implementa a integração com o SUAP, tendo 2 principais funcionalidades:

- Logar com SUAP via OAuth2
- Consumir API (via OAuth2) obtendo recursos em nome do usuário

## QuickStart

### Crie sua Aplicação no SUAP

Crie sua aplicação em https://suap.ifrn.edu.br/api/ com as seguintes informações:

- **Client Type:** Confidential
- **Authorization Grant Type:** Authorization Code
- **Redicert URIs**: http://localhost:8888/complete/suap/

### Instalando, Configurando e Rodando o Cliente SUAP Django

Considerando que você já tenha clonado o repositório **cliente_suap_django** e instalado o PIP (https://pip.pypa.io/en/stable/installing/), abra o terminal:

	pip install -U virtualenv virtualenvwrapper
	cd cliente_suap_django
	mkvirtualenv cliente_suap_django
	workon cliente_suap_django
	pip install -r requirements.txt
	./manage.py migrate
	cp cliente_suap_django/local_settings_sample.py cliente_suap_django/local_settings.py

Faça os ajustes necessários, definindo as variáveis `SOCIAL_AUTH_SUAP_KEY` e `SOCIAL_AUTH_SUAP_SECRET` no **local_settings.py**.

Rode a aplicação cliente:

	./manage.py runserver 0.0.0.0:8888

Abra seu browser em http://localhost:8888/
