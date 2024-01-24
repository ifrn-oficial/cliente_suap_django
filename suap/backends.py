from social_core.backends.oauth import BaseOAuth2

from app.models import Usuario
from utils.user import formatar_url_foto


class SuapOAuth2(BaseOAuth2):
    name = 'suap'
    AUTHORIZATION_URL = 'https://suap.ifrn.edu.br/o/authorize/'
    ACCESS_TOKEN_URL = 'https://suap.ifrn.edu.br/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    ID_KEY = 'identificacao'
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = 'https://suap.ifrn.edu.br/api/eu/'
    EXTRA_USER_DATA_URL = 'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/'
    DEFAULT_SCOPE = [
        'identificacao', 'email', 'documentos_pessoais'
    ]

    def user_data(self, access_token, *args, **kwargs):
        """
        Retorna uma resposta contendo os dados do usuário.
        
        A coleta dos dados é feita através de duas requisições em duas URLs
        diferentes: USER_DATA_URL e EXTRA_USER_DATA_URL.
        """
        method = 'GET'
        data = {
            'scope': kwargs.get('response').get('scope')
        }
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = self.request(
            url=self.USER_DATA_URL,
            method=method,
            data=data,
            headers=headers
        ).json()
        extra_response = self.request(
            url=self.EXTRA_USER_DATA_URL,
            method=method,
            headers=headers
        ).json()
        curso = extra_response.get('vinculo').get('curso')
        response['curso'] = curso
        return response

    def get_user_details(self, response):
        """
        Retorna um dicionário mapeando os campos de settings.AUTH_USER_MODEL.

        Aqui, você pode fazer várias coisas, como salvar os dados do usuário em
        outro model, como mostrado abaixo, onde um objeto de Usuario é criado.
        """
        nome_completo = response.get('nome_registro')
        if nome_social := response.get('nome_social'):
            nome_completo = nome_social
        primeiro_nome, *_, ultimo_nome = nome_completo.split()
        url_foto = formatar_url_foto(response.get('foto'))
        dados_usuario = {
            'matricula': response.get('identificacao'),
            'nome_completo': nome_completo,
            'primeiro_nome': primeiro_nome,
            'ultimo_nome': ultimo_nome,
            'cpf': response.get('cpf'),
            'campus': response.get('campus'),
            'curso': response.get('curso'),
            'email_pessoal': response.get('email_secundario'),
            'email_escolar': response.get('email_google_classroom'),
            'email_academico': response.get('email_academico'),
            'sexo': response.get('sexo'),
            'tipo_vinculo': response.get('tipo_usuario'),
            'data_nascimento': response.get('data_de_nascimento'),
            'url_foto': url_foto
        }
        if Usuario.objects.filter(matricula=response.get('identificacao')).first() is None:
            Usuario.objects.create(**dados_usuario)
        return {
            'username': response.get('identificacao'),
            'first_name': primeiro_nome,
            'last_name': ultimo_nome,
            'email': response.get('email_preferencial')
        }
