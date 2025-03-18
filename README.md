# Rebecca - An AI virtual assistant

(Para a versão em portugues, [clique aqui.](./docs/pt_br/README.md) (atualizado para V1.0.1))

- made by elidotpy, for fun, and for learning (don't expect much from me. please.)
- i tried to keep it organized, i swear

# How to use

### 1 - Clone the repository

```
git clone https://github.com/elidotpy/rebecca
```

### 2 - Install dependencies

```
pip install -r requirements.txt
```

### 3 - run `main.py`

```
python main.py
```

### 4 - `config.json` and `generation_config.json` should be created in the `configs`. So, we need to edit them now.
* First, let's edit `config.json`
```json
{
    "GOOGLE_API_KEY": "my-epic-api-key",
    "GOOGLE_MODEL": "gemini-2.0-flash",
    "VERBOSITY": 1
}
```

Get your `GOOGLE_API_KEY` from [Google AI Studio](https://aistudio.google.com/apikey).

I recommend using `"gemini-2.0-flash"` as the model.

`VERBOSITY` is how much information the output will contain.
1 - NONE (will show only the essentials)
2 - INFO (will show some information)
3 - DEBUG (will show information that is meant for debugging)

if you just plan on using it, leave it on 1.

* Then, `generation_config.json`. Editing `generation_config.json` isn't really necessary, but you can do it if you want.
```json
{
    "TEMPERATURE": 0.7,
    "MAX_TOKENS": 1024,
    "STREAM": false
}
```
`TEMPERATURE` is how creative Rebecca's response is.
`MAX TOKENS` is how long Rebecca's response can be.

If `STREAM` is set to true, Rebecca's response will be outputted chunk by chunk. If not, it will wait until it is fully generated, then output the whole message at once.

### 5 - run main.py... **again**
If you've done it correctly, you should see this:
```
> 
```
Now, type your message and press enter. You should see Rebecca's response not long after.

# Features

## Tools

a `tool` is what the AI can do _besides_ chatting. with tools, it can do basically anything, as long as there's a tool for that.

### Tools Rebecca can use:

- Read files
- Delete files
- Write files/Create files
- List files
- Get the current directory Rebecca is on
- Change the directory Rebecca is on

### Tools disabled by default:

- Terminal (dangerous)

(read [docs/tools.md](./docs/en/tools.md) to know how to create your own or remove tools)

# Changelogs

## V1.0.0 - First release

1. Added personality
2. Added tools

## V1.0.1 - Multiple Personalities And the history update

1. Added [personas](./docs/en/personas.md)
2. Added history!!
3. (internal) Made it more organized