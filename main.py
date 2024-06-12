"""
Main app file
"""
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

# Создание приложения
app = FastAPI(
    title="Trading App"
)


