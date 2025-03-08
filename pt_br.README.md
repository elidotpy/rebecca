# Rebecca - Uma assistente virtual

- feito por elidotpy por diversão e aprendizagem. (Não espere muito de mim, eu imploro)
- eu tentei manter isso organizado, eu juro


# How to use

### 1 - Clonar o repositorio

```
git clone https://github.com/elidotpy/rebecca
```

### 2 - Instalar dependencias

```
pip install -r requirements.txt
```

### 3 - Executar `main.py`

```
python main.py
```

### 4 - `config.json` foi criado, então edita o arquivo
```json
{
    "GOOGLE_API_KEY": "minha-chave-legal",
    "GOOGLE_MODEL": "gemini-2.0-flash",
    "STREAM": true
}
```

Pegue a sua chave `GOOGLE_API_KEY` do [Google AI Studio](https://aistudio.google.com/apikey).

Eu recomendo usar `"gemini-2.0-flash"` como o modelo.

Se `STREAM` for `true`, a resposta de Rebecca sera mostrada pedaço por pedaço. se não, vai ser mostrado tudo de uma vez

### 5 - Executar `main.py`... DENOVO.
Se tu fez tudo certinho, você deve ser isso
```
> 
```
agora, digite sua mensagem e aperta enter. você deve ver a resposta dela não muito tempo depois.

# Recursos

## Ferramentas

uma ferramenta é o que a Rebecca pode fazer _além_ de conversar. Ela pode fazer qualquer coisa, portanto que tenha uma ferramenta para isso.

### Ferramentas que Rebecca pode usar:

- Ler arquivos
- Deletar arquivos
- Criar arquivos/Escrever em um arquivo
- Listar arquivos
- Ver o diretório que ela está
- Mudar o diretório que ela está

### Ferramentas desabilitadas por padrão:
- Terminal (perigoso)

(leia [docs/tools.md](docs/pt_br.tools.md) para saber como adicionar/remover ferramentas)

# Mudanças

## V1.0.0 - Lançamento inicial

1. Personalidade adicionada
2. Ferramentas adicionadas
