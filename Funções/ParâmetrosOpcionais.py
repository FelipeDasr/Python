def tag_bloco(texto, classe='success'):
    return '<div class="{}">{}</div>'.format(classe, texto)


if __name__ == '__main__':
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'
    print(tag_bloco('bloco'))
