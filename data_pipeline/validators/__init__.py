"""Data validators for AQI - validate data integrity and schema compliance."""

import json
from pathlib import Path
from typing import Any


class ValidationError(Exception):
    """Raised when data validation fails."""


class BaseValidator:
    """Base class for all data validators."""

    def validate(self, data: Any) -> list[str]:
        raise NotImplementedError

    def validate_file(self, file_path: str) -> list[str]:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return self.validate(data)


class QuranValidator(BaseValidator):
    """Validate Quran data structure."""

    def validate(self, data: Any) -> list[str]:
        errors = []
        if not isinstance(data, dict):
            errors.append("Root must be a dict")
            return errors
        if "surahs" not in data:
            errors.append("Missing 'surahs' key")
            return errors
        for i, surah in enumerate(data["surahs"]):
            if "number" not in surah:
                errors.append(f"Surah {i}: missing 'number'")
            if "name" not in surah:
                errors.append(f"Surah {i}: missing 'name'")
            if "ayahs" not in surah:
                errors.append(f"Surah {i}: missing 'ayahs'")
            else:
                for j, ayah in enumerate(surah["ayahs"]):
                    if "number" not in ayah:
                        errors.append(f"Surah {i}, Ayah {j}: missing 'number'")
                    if "text" not in ayah:
                        errors.append(f"Surah {i}, Ayah {j}: missing 'text'")
        return errors


class HadithValidator(BaseValidator):
    """Validate Hadith data structure."""

    def validate(self, data: Any) -> list[str]:
        errors = []
        if not isinstance(data, dict):
            errors.append("Root must be a dict")
            return errors
        if "collection" not in data:
            errors.append("Missing 'collection' key")
        if "hadiths" not in data:
            errors.append("Missing 'hadiths' key")
            return errors
        for i, hadith in enumerate(data["hadiths"]):
            if "number" not in hadith:
                errors.append(f"Hadith {i}: missing 'number'")
            if "text" not in hadith:
                errors.append(f"Hadith {i}: missing 'text'")
        return errors


class AsmaValidator(BaseValidator):
    """Validate Asmaul Husna data structure."""

    def validate(self, data: Any) -> list[str]:
        errors = []
        if not isinstance(data, dict):
            errors.append("Root must be a dict")
            return errors
        if "names" not in data:
            errors.append("Missing 'names' key")
            return errors
        numbers = set()
        for i, name in enumerate(data["names"]):
            if "number" not in name:
                errors.append(f"Name {i}: missing 'number'")
            else:
                if name["number"] in numbers:
                    errors.append(f"Name {i}: duplicate number {name['number']}")
                numbers.add(name["number"])
            if "arabic" not in name:
                errors.append(f"Name {i}: missing 'arabic'")
            if "english" not in name:
                errors.append(f"Name {i}: missing 'english'")
        return errors


def validate_all(data_dir: str) -> dict[str, list[str]]:
    """Validate all data files in the project."""
    results = {}
    data_path = Path(data_dir)

    for json_file in data_path.rglob("*.json"):
        rel_path = str(json_file)
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                json.load(f)
            results[rel_path] = []
        except json.JSONDecodeError as e:
            results[rel_path] = [f"Invalid JSON: {e}"]

    return results
