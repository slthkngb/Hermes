import os
from pydantic import BaseModel

class TrainingConfig(BaseModel):
    batch_size: int = 32
    learning_rate: float = 0.001
    epochs: int = 10

class HermesConfig(BaseModel):
    training: TrainingConfig = TrainingConfig()
    log_level: str = "INFO"
    # Add more sections as needed

def load_config(path: str = None) -> HermesConfig:
    # 1. If the path is provided, parse the file
    # 2. Otherwise, load defaults or environment variables
    # 3. Return a validated HermesConfig
    return HermesConfig()

