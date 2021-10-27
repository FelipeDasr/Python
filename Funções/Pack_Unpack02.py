#!python

def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


def tag_lista(*itens):
    lista = "".join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco("inline e classe", "info", True))
    print(tag_bloco("inline", inline=True))
    print(tag_bloco("falhou", "error"))
    print(tag_lista("ANA", "BEATRIZ", "SOFIA"))
    print(tag_bloco(tag_lista("Item 1", "item 2")))
