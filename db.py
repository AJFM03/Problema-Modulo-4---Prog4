from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Configura la cadena de conexión
# Para local: "mongodb://localhost:27017/"
# Para Atlas: "mongodb+srv://usuario:password@cluster.mongodb.net/"

MONGO_URI = "mongodb://localhost:27017/"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Verifica la conexión
    print("✅ Conectado a MongoDB")
except ConnectionFailure:
    print("❌ Error: No se pudo conectar a MongoDB")
    exit()

# Base de datos y colección
db = client["biblioteca_db"]
coleccion_libros = db["libros"]
