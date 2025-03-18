import json
import os

from google.genai import types

from .errors import historyInvalid


class History:
    def __init__(self):
        self.history = []
    
    def add_to_history(self, message:str, role:str):
        self.history.append({
            "content": message,
            "role": role
        })
    
    def load_history(self, file_path:str):
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.history = json.load(f)
            except json.JSONDecodeError:
                self.save_history(file_path=file_path)
                raise historyInvalid("The history file is corrupted, so it has been deleted.")
                
    def history_to_google(self):
        return [types.Content(role=message["role"], parts=[types.Part.from_text(text=message["content"])]) for message in self.history] # actual first time using list comprehension on whatever it is called
    
    def save_history(self, file_path:str):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=4)