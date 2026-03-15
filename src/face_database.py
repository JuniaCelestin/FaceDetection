"""
Face database manager.
Handles saving, loading, and searching saved faces with embeddings.
"""
import os
import json
import numpy as np
import cv2
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class FaceDatabase:
    """Manages saved faces and their embeddings on the filesystem."""

    def __init__(self, data_dir: str = "data"):
        """
        Initialize the face database.

        Args:
            data_dir: Root directory for storing face data
        """
        # TODO: Create Path object for data directory
        self.data_dir = Path(data_dir)

        # TODO: Create path for faces subdirectory
        self.faces_dir = self.data_dir / "faces"

        # TODO: Create path for index.json file
        self.index_file = self.data_dir / "index.json"

        # TODO: Create directories if they don't exist
        # Use mkdir with parents=True and exist_ok=True
        self.faces_dir.mkdir(parents= True, exist_ok= True)

        # TODO: Initialize empty index dictionary
        self.index = {}

        # Load existing index from disk
        self._load_index()




    def _load_index(self): #check if you did write
        """Load the index.json file into memory."""
        # TODO: Check if index_file exists using .exists() method
        if self.index_file.exists():
            # Load existing index
            # TODO: Open file in read mode and load JSON
            with open(self.index_file, 'index.json') as f:
                self.index = json.file(f)
        else:
            # Create new empty index
            self.index = {}
            self._save_index()


