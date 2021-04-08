import os
from typing import Dict
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(os.getcwd(), '.env')
load_dotenv(dotenv_path)

class SecretsStore:

    def __init__(self) -> None:
        self.stored_secrets_keys = [
            "discord_token",
            "reddit_client_id",
            "reddit_client_secret"
        ]

    def get_secret(self, secret_key):
        try:
            secret = os.environ[secret_key]
        except:
            return False
        finally:
            return { secret_key : secret }
    
    def get_all_secrets(self) -> Dict:
        secrets = {}
        try:
            for i in self.stored_secrets_keys:
                secrets[i] = os.environ[i]
        except:
            return False
        finally:
            return secrets
