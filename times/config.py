from typing import Optional
from pydantic import BaseSettings

# The service settings, here you can find the parameters like table names and such required to run the service


class Settings(BaseSettings):
    app_name: str = "times"
    aws_default_region: str = ''
    aws_access_key_id: Optional[str]
    aws_secret_access_key: Optional[str]
    aws_session_token: Optional[str]
    database_host: str = 'db'
    current_environment: str = ''
    database_default_name: str = 'postgres'
    database_user: str = 'postgres'
    database_port: int = 5431
    rds_endpoint: Optional[str]
    rds_port: Optional[str]
    rds_user: Optional[str]
    rds_password: Optional[str]
    rds_database: Optional[str]
    database_password: str = 'postgres'


    class Config:
        env_file = ".env"


settings = Settings()
