import os
import environ

# Inicializa entorno
env = environ.Env()

# Cargar variables desde .env si existe
environ.Env.read_env(os.path.join(os.path.dirname(__file__), "../../.env"))

# Variables de entorno
DATABASE_URL = env("DATABASE_URL")
ECHO_SQL = env.bool("ECHO_SQL")
DEBUG = env.bool("DEBUG")
