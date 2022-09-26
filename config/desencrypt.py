# Decryption Script .
# Use one of the methods to get a key ( it must be the same as used in encrypting )
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL
from cryptography.fernet import Fernet
from json import loads


class DbConnection:
    meta = MetaData()

    @staticmethod
    def engine_connection():
        key_file = 'config/key.txt'
        input_file = 'config/encrypted'

        with open(key_file, 'rb') as k:
            key = k.read()

        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        config = loads(decrypted)

        # BUILD THE CONNECTION
        engine = create_engine(
            URL(
                username=config["USER"],
                password=config["PASSWORD"],
                database=config["DB"],
                port=config["PORT"],
                host=config["HOST"],
                drivername=config["DRIVER_NAME"]
            )
        )
        # BUILD THE CONNECTION
        return engine.connect()
