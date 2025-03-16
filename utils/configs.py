import os
import json
general_configs = {
    "GOOGLE_API_KEY": "",
    "GOOGLE_MODEL": "",
    "USE_TOOLS": True,
    "VERBOSITY": 0
}

generation_configs = {
    "TEMPERATURE": 0.7,
    "MAX_TOKENS": 1024,
    "STREAM": False
}

def check_config(file_path, base_config, kill_if_not_found=True):
    os.makedirs("configs", exist_ok=True)
    if os.path.exists("./configs/"+ file_path):
        error = False
        try:
            with open("./configs/"+ file_path, "r", encoding="utf-8") as f:
                jsonconfig = json.load(f)
            # check if the config is valid
            for config in base_config:
                if not config in jsonconfig:
                    jsonconfig[config] = base_config[config]
                    error = True
            if error:
                with open("./configs/"+ file_path, "w", encoding="utf-8") as f:
                    json.dump(jsonconfig, f, indent=4)
                if kill_if_not_found:
                    raise ValueError(f"One or more of the configurations are not set in {file_path}.")
        except json.JSONDecodeError as e:
            print(f"Invalid {file_path}: " + e.msg)
                    
            with open("./configs/"+ file_path, "w", encoding="utf-8") as f:
                json.dump(base_config, f, indent=4)
            raise ValueError(f"The config file ({file_path}) is invalid.") from e
    else:
        with open("./configs/"+ file_path, "w", encoding="utf-8") as f:
            json.dump(base_config, f, indent=4)
        if kill_if_not_found:
            raise FileNotFoundError(f"{file_path} didn't exist. It was created, Go edit it.")
        return base_config
    
    return jsonconfig