# Cliente SUAP Django

![Django 5.0.1](https://img.shields.io/badge/Django-5.0.1-brightgreen)
![Python 3.12.1](https://img.shields.io/badge/Python-3.12.1-blue)

## Sobre

O Cliente SUAP Django implementa a integração com o SUAP, tendo 2 principais funcionalidades:

- Logar com SUAP via OAuth2;
- Consumir API via OAuth2 obtendo recursos em nome do usuário.

## Utilização

### Criação da Aplicação no SUAP

Crie sua aplicação em <https://suap.ifrn.edu.br/admin/api/aplicacaooauth2/> com as seguintes informações:

- **Authorization Grant Type:** Authorization Code;
- **Redirect URIs:** <http://127.0.0.1:8000/complete/suap/>;
- **Client Type:** Confidential.

Em **Redirect URIs** você também pode adicionar o endereço do servidor externo, caso ele esteja rodando na nuvem. No valor definido acima, o servidor está rodando localmente (localhost).

### Instalação e Configuração

Clone o repositório para a máquina, crie um ambiente virtual e instale as dependências:

```bash
git clone https://github.com/sergiodantasz/cliente-suap-django.git
cd cliente-suap-django
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Duplique o arquivo `.env.example` e renomeie a cópia para `.env`. Agora, configure corretamente as variáveis de ambiente no arquivo.

Os valores das variáveis `SOCIAL_AUTH_SUAP_KEY` e `SOCIAL_AUTH_SUAP_SECRET` são disponibilizados ao criar a aplicação no SUAP.

Feito isso, aplique as migrações, colete os arquivos estáticos e rode a aplicação:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

Abra o navegador em <http://127.0.0.1:8000/>.

### Exemplo

A aplicação `app` foi criada como modelo e possui três URLs:

- **Login:** <http://127.0.0.1:8000/login/>;
- **Logout:** <http://127.0.0.1:8000/logout/>;
- **Perfil:** <http://127.0.0.1:8000/accounts/profile/>;

Ao fazer o login, o usuário será redirecionado para o perfil, onde todos os seus dados são exibidos. E quando o logout é realizado, a autenticação do usuário é removida e ele é redirecionado para a página de login.

Observe a estruturação desse exemplo e replique no seu projeto de forma que ele se adapte à sua configuração de maneira adequada.
