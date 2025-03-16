"""
The main module, the one that makes rebecca work.
"""

# imports 
import os
import time
import warnings
from utils import errors

from google import genai
from google.genai import types

from rebecca_tools import tools
from utils import configs, persona
from utils.history import History
from utils.logs import Logger, VerbosityLevel

# initial setups
GENERATIONCONFIG = configs.check_config(
    file_path="generation_config.json",
    base_config=configs.generation_configs,
    kill_if_not_found=False
    )
GENERALCONFIG = configs.check_config(
    file_path="config.json",
    base_config=configs.general_configs
    )

LOGGER = Logger("rebecca", GENERALCONFIG["VERBOSITY"])
LOGGER.debug("Logger initialized.")
chat_history = History()
try:
    chat_history.load_history("history.json")
except errors.historyInvalid as e:
    LOGGER.log(e.msg, verbosity_level=VerbosityLevel.WARNING)
LOGGER.debug("History loaded/created.")

# Supress pydantic warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

# tools - the things that Rebecca can do (Defined in rebecca_tools.py)

# Getting the personality
prompt = persona.get_persona()
LOGGER.info(f"Persona {prompt[1]} successfully loaded.") # prompt[1] is the name of the persona

generation_config = types.GenerateContentConfig(
    temperature=GENERATIONCONFIG["TEMPERATURE"],
    max_output_tokens=GENERATIONCONFIG["MAX_TOKENS"],
    system_instruction=prompt[0], # prompt[0] is the actual prompt
    tools=tools,
    safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_CIVIC_INTEGRITY,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE,
        ),
    ],
)

client = genai.Client(api_key=GENERALCONFIG["GOOGLE_API_KEY"])
chat = client.chats.create(model=GENERALCONFIG["GOOGLE_MODEL"], config=generation_config, history=chat_history.history_to_google())
LOGGER.debug("Client and Chat session created.")


def get_user_input():
    """
    Gets the user input, and attaches useful information to it
    """
    return input("> ")+ f"[Current Time: {time.ctime()}, Current directory: {os.getcwd()}]"


def try_to_get_response(message, stream):
    """
    Tries to get a response from the AI
    """
    chat_history.add_to_history(message=message, role="user")
    if stream:
        response = ""
        for chunk in chat.send_message_stream(message):
            try:
                response += chunk.text
                print(chunk.text, end="")
            except ValueError:
                pass
        try:
            if not chunk.text[len(chunk.text)-1] == "\n":
                print("\n")
        except IndexError:
            pass
        chat_history.add_to_history(response, "model")
    else:
        response = chat.send_message(message)
        print(response.text)
        chat_history.add_to_history(response.text, "model")

try:
    while True:
        message = get_user_input()
        try_to_get_response(message, GENERATIONCONFIG["STREAM"])
except KeyboardInterrupt:
    print("\nSaving history...")
    chat_history.save_history("history.json")
