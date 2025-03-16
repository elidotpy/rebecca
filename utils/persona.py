import os
import getpass

def get_persona():
    if os.path.exists("./personas/cur_persona.txt"):
        try:
            with open("./personas/cur_persona.txt", "r", encoding="utf-8") as f:
                persona = f.read()
                with open(f"./personas/{persona}.txt", "r", encoding="utf-8") as f:
                    prompt = f.read().replace("{user}", getpass.getuser())
        except Exception as exc:
            raise FileNotFoundError(f"Persona {persona} not found.") from exc
    else:
        raise FileExistsError("personas/cur_persona.txt File not found.")
    return [prompt, persona]