from dotenv import load_dotenv, find_dotenv
import os


from constants import ERROR_MESSAGES


from pathlib import Path

load_dotenv(find_dotenv("../.env"))


####################################
# File Upload
####################################


UPLOAD_DIR = "./data/uploads"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)


####################################
# ENV (dev,test,prod)
####################################

ENV = os.environ.get("ENV", "dev")

####################################
# OLLAMA_API_BASE_URL
####################################

OLLAMA_API_BASE_URL = os.environ.get(
    "OLLAMA_API_BASE_URL", "http://localhost:11434/api"
)

####################################
# WEBUI_VERSION
####################################

WEBUI_VERSION = os.environ.get("WEBUI_VERSION", "v1.0.0-alpha.61")

####################################
# WEBUI_AUTH (Required for security)
####################################

WEBUI_AUTH = True

####################################
# WEBUI_JWT_SECRET_KEY
####################################

WEBUI_JWT_SECRET_KEY = os.environ.get("WEBUI_JWT_SECRET_KEY", "t0p-s3cr3t")

if WEBUI_AUTH and WEBUI_JWT_SECRET_KEY == "":
    raise ValueError(ERROR_MESSAGES.ENV_VAR_NOT_FOUND)
