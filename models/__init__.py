#!/usr/bin/python3
"""Module executes package initialization."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
