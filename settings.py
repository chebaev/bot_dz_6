import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import SecretStr, StrictStr

load_dotenv()

class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv("SITE_API_NUMBER", None)
    host_api: StrictStr = os.getenv("HOST_API_NUMBER", None)

    api_key_num: SecretStr = os.getenv("SITE_API_NUMBER", None)
    host_api_num: StrictStr = os.getenv("HOST_API_NUMBER", None)

    api_key_trans: SecretStr = os.getenv("SITE_API_TRANSLATOR", None)
    host_api_trans: StrictStr = os.getenv("HOST_API_TRANSLATOR", None)

class BotSettings(BaseSettings):

    token: SecretStr = os.getenv("TOKEN", None)



# if __name__ == '__main__':
#     settings = Settings()
#     print(settings.token.get_secret_value())