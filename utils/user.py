from re import sub


def formatar_url_foto(url: str) -> str:
    if not isinstance(url, str):
        raise TypeError('A URL deve ser uma string.')
    nova_url = 'https://suap.ifrn.edu.br' + sub(r'[0-9]{2,3}x[0-9]{3}\/', '', url)
    return nova_url
