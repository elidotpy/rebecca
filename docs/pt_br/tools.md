# Ferramentas

`Ferramentas` são as coisas que a Rebecca consegue fazer.

Todas as ferramentas são definidas em `"./rebecca_tools.py"`

# Como criar a sua própria ferramenta?

Primeiro, você precisa declarar uma função com o nome da ferramenta. Digamos que queremos fazer uma função chamada "`miau`"

```python
def miau():
```

e queremos dar a ela o argumento "`vezes`", para que ela imprima miau `{vezes}` vezes.

```python
def miau(vezes):
```

Agora, precisamos dar uma `dica do tipo do argumento.` Isso é necessário, para que a IA não quebre, ou tente usar um tipo diferente do que você pretendia. Neste caso, é um inteiro. Você também pode adicionar uma `dica de tipo de retorno`, mas não é realmente necessário.

```python
def miau(vezes:int):
```

Okay, agora, ela precisa de uma `docstring`, para que a IA saiba o que ela faz.

```python
def miau(vezes:int):
    """
        Imprime a palavra "miau" {vezes} vezes.
    """
```

então, podemos finalmente escrever o conteúdo da função.

```python
def miau(vezes:int):
    """
        Imprime a palavra "miau" {vezes} vezes.
    """
    return "miau " * vezes
```

Finalmente, precisamos fazer a IA saber que a ferramenta existe.
Para fazer isso, basta adicionar um item à lista "`tools`", definida na parte inferior deste arquivo.

```python
tools = [ferramenta1, ferramenta2, miau]
```

(ferramenta1 e ferramenta2 são puramente para fins de demonstração.)

Parabéns, você acabou de criar a sua própria ferramenta, e a IA é capaz de usá-la!

# Como remover ferramentas?

Remova o nome da ferramenta da lista `tools` no final do arquivo.
Por exemplo, você quer remover "ferramenta2"
```python
tools = [ferramenta1, ferramenta3] # era [ferramenta1, ferramenta2, ferramenta3]
```

Agora a Rebecca não consegue mais usar a ferramenta.

###### Creditos: Gemini 2.0 Flash por essa traduçao, tava com muita preguiça. até IAs merece credito, sabia?