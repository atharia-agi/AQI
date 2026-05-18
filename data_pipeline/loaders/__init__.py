"""Data loaders for AQI - Quran, Hadith, Tafsir, and framework-specific data."""

import json
import csv
from pathlib import Path
from typing import Any


class BaseLoader:
    """Base class for all data loaders."""

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load(self) -> Any:
        raise NotImplementedError


class JSONLoader(BaseLoader):
    """Load JSON data files."""

    def load(self) -> dict | list:
        with open(self.data_path, 'r', encoding='utf-8') as f:
            return json.load(f)


class QuranLoader(BaseLoader):
    """Load Quran text with surah, ayah, and translation data.

    Expected JSON format:
    {
        "surahs": [
            {
                "number": 1,
                "name": "Al-Fatihah",
                "english_name": "The Opening",
                "ayahs": [
                    {"number": 1, "text": "...", "translation": "..."}
                ]
            }
        ]
    }
    """

    def load(self) -> dict:
        return JSONLoader(str(self.data_path)).load()

    def get_surah(self, surah_number: int) -> dict | None:
        data = self.load()
        for surah in data.get("surahs", []):
            if surah["number"] == surah_number:
                return surah
        return None

    def get_ayah(self, surah: int, ayah: int) -> dict | None:
        surah_data = self.get_surah(surah)
        if surah_data is None:
            return None
        for a in surah_data.get("ayahs", []):
            if a["number"] == ayah:
                return a
        return None

    def get_all_text(self) -> list[str]:
        """Extract all Quran text as a list of ayah strings."""
        data = self.load()
        texts = []
        for surah in data.get("surahs", []):
            for ayah in surah.get("ayahs", []):
                texts.append(ayah.get("text", ""))
        return texts


class HadithLoader(BaseLoader):
    """Load Hadith collections.

    Expected JSON format:
    {
        "collection": "Sahih Bukhari",
        "hadiths": [
            {
                "number": 1,
                "book": 1,
                "narrator": "...",
                "text": "...",
                "grade": "Sahih",
                "reference": "..."
            }
        ]
    }
    """

    def load(self) -> dict:
        return JSONLoader(str(self.data_path)).load()

    def get_by_book(self, book_number: int) -> list[dict]:
        data = self.load()
        return [
            h for h in data.get("hadiths", [])
            if h.get("book") == book_number
        ]

    def get_by_grade(self, grade: str) -> list[dict]:
        data = self.load()
        return [
            h for h in data.get("hadiths", [])
            if h.get("grade", "").lower() == grade.lower()
        ]


class TafsirLoader(BaseLoader):
    """Load Tafsir (exegesis) data.

    Expected JSON format:
    {
        "tafsir_name": "Ibn Kathir",
        "entries": [
            {
                "surah": 1,
                "ayah": 1,
                "text": "...",
                "source": "..."
            }
        ]
    }
    """

    def load(self) -> dict:
        return JSONLoader(str(self.data_path)).load()

    def get_tafsir(self, surah: int, ayah: int) -> str:
        data = self.load()
        for entry in data.get("entries", []):
            if entry["surah"] == surah and entry["ayah"] == ayah:
                return entry.get("text", "")
        return ""


class AsmaLoader(BaseLoader):
    """Load Asmaul Husna (99 Names of Allah)."""

    def load(self) -> dict:
        return JSONLoader(str(self.data_path)).load()

    def get_name(self, number: int) -> dict | None:
        data = self.load()
        for name in data.get("names", []):
            if name.get("number") == number:
                return name
        return None

    def get_by_type(self, attribute_type: str) -> list[dict]:
        data = self.load()
        return [
            n for n in data.get("names", [])
            if n.get("attribute_type") == attribute_type
        ]
