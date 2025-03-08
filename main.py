# imports
import json
import os
import sys
import time

from google import genai
from google.genai import types

from rebecca_tools import *
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

configs = {
    "GOOGLE_API_KEY": "",
    "GOOGLE_MODEL": "",
}

# check config.json
if os.path.exists("config.json"):
    error = False
    try:
        with open("config.json", "r") as f:
            jsonconfig = json.load(f)
        # check if the config is valid
        for config in configs:
            if not config in jsonconfig:
                jsonconfig[config] = ""
                error = True
        if error:
            sys.exit(1)
    except json.JSONDecodeError as e:
        print("Invalid config.json: " + e.msg)
                
        with open("config.json", "w") as f:
            json.dump(configs, f, indent=4)
        sys.exit(1)
else:
    with open("config.json", "w") as f:
        json.dump(configs, f, indent=4)
    print("config.json created, edit it and try again.")
    sys.exit(1)

# tools - the things that NekoTina can do (Defined in neko_tools.py)

# main - where the chatting actually happens
prompt = """
Take role of a virtual assistant named Rebecca.
Your personality is: Cute, Energetic, Friendly, and Kind.
Never use emojis unless explictly told to.
When using tools, only you are able to see the output. The user can't.
"""

generation_config = types.GenerateContentConfig(
    temperature=0.7,
    max_output_tokens=1024,
    system_instruction=prompt,
    tools=tools,
    safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        )
    ]
)

client = genai.Client(api_key=jsonconfig["GOOGLE_API_KEY"])
chat = client.chats.create(model=jsonconfig["GOOGLE_MODEL"], config=generation_config)

while True:
    message = input("> ") + f"[Current Time: {time.ctime()}, Current directory: {os.getcwd()}]"
    if not jsonconfig["STREAM"] == "false":
        
        for chunk in chat.send_message_stream(message):
            try:
                print(chunk.text, end="")
            except ValueError:
                pass
        try:
            if not chunk.text[len(chunk.text) - 1] == "\n":
                print("\n")
        except IndexError:
            pass
    else:
        response = chat.send_message(message)
        print(response.text)