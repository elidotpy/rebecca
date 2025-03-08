# Rebecca - An AI virtual assistant

(Para a versão em portugues, [clique aqui.](./pt_br.README.md) (atualizado para V1.0.0))

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

### 4 - `config.json` should be created. So, edit it.
```json
{
    "GOOGLE_API_KEY": "my-epic-api-key",
    "GOOGLE_MODEL": "gemini-2.0-flash",
    "STREAM": true
}
```

Get your `GOOGLE_API_KEY` from [Google AI Studio](https://aistudio.google.com/apikey).

I recommend using `"gemini-2.0-flash"` as the model.

If `STREAM` is set to true, Rebecca's response will be outputted chunk by chunk. If not, it will wait until it is fully generated, then output the whole message at once.

### 5 - run main.py... **again**
If you've done it correctly, you should see this:
```
> 
```
Now, type your message and press enter. You should see Rebecca's response not long after.

# Features

## Tools

a tool is what the AI can do _besides_ chatting. with tools, it can do basically anything, as long as there's a tool for that.

### Tools Rebecca can use:

- Read files
- Delete files
- Write files/Create files
- List files
- Get the current directory Rebecca is on
- Change the directory Rebecca is on

### Tools disabled by default:

- Terminal (dangerous)

(read [docs/tools.md](docs/tools.md) to know how to create your own or remove tools)

# Changelogs

## V1.0.0 - First release

1. Added personality
2. Added tools
