"""Hidden Patterns in the Quran

Beyond the obvious mathematical codes and scientific references, the Quran
contains deeper hidden patterns that require computational analysis to uncover.

These include:
- Abjad numeral system (each Arabic letter has a numerical value)
- Structural symmetry (ring composition, chiastic structures)
- Letter position patterns
- Word distribution patterns
- Numerical relationships between surahs and verses

"And if all that is in the earth of trees were pens, and the sea [were ink],
 with seven [more] seas added to it, the words of Allah would not be exhausted."
 (Quran 31:27)
"""

import math
from typing import Any


# ============================================================
# ABJAD NUMERAL SYSTEM
# ============================================================
# Each Arabic letter has a numerical value. This system was used
# for centuries and reveals hidden numerical patterns in the Quran.

ABJAD_VALUES = {
    "alif": 1,
    "ba": 2,
    "jim": 3,
    "dal": 4,
    "ha": 5,
    "waw": 6,
    "za": 7,
    "ha_h": 8,
    "ta": 9,
    "ya": 10,
    "kaf": 20,
    "lam": 30,
    "mim": 40,
    "nun": 50,
    "sin": 60,
    "ayn": 70,
    "fa": 80,
    "sad": 90,
    "qaf": 100,
    "ra": 200,
    "shin": 300,
    "ta_t": 400,
    "tha": 500,
    "kha": 600,
    "dha": 700,
    "dad": 800,
    "za_z": 900,
    "ghayn": 1000,
}

# ============================================================
# MYSTERIOUS LETTERS (AL-HURUF AL-MUQATTA'AT)
# ============================================================
# 29 surahs begin with mysterious letter combinations.
# Their meaning is known only to Allah, but computational
# analysis reveals patterns.

MUQATTATAT_SURAHS = {
    "Alif-Lam-Mim": [2, 3, 7, 29, 30, 31, 32],
    "Alif-Lam-Ra": [10, 11, 12, 14, 15],
    "Alif-Lam-Mim-Ra": [13],
    "Kaf-Ha-Ya-Ayn-Sad": [19],
    "Ta-Ha": [20],
    "Ta-Sin-Mim": [26, 27, 28],
    "Ta-Sin": [27],
    "Sad": [38],
    "Ha-Mim": [40, 41, 42, 43, 44, 45, 46],
    "Qaf": [50],
    "Nun": [68],
}

# ============================================================
# STRUCTURAL SYMMETRY
# ============================================================
# The Quran exhibits remarkable structural symmetry:

STRUCTURAL_SYMMETRY = {
    # Center of the Quran
    "center_surah": "Al-Kahf (18)",
    "center_verse": "Let him be gentle" (18:19),
    "total_surahs": 114,
    "surahs_before_center": 18,
    "surahs_after_center": 95,

    # First and last surah relationship
    "first_surah": "Al-Fatihah (1)",
    "last_surah": "An-Nas (114)",
    "total_verses_first": 7,
    "total_verses_last": 6,

    # Opening and closing themes
    "opening_theme": "Praise and guidance",
    "closing_theme": "Seeking refuge from evil",
}

# ============================================================
# RING COMPOSITION PATTERNS
# ============================================================
# Many surahs follow a chiastic (A-B-C-B'-A') structure.

RING_PATTERNS = {
    "Al-Fatihah": {
        "structure": "A-B-C-B'-A'",
        "A": "Praise of Allah (v.1-2)",
        "B": "Mercy and Judgment (v.3-4)",
        "C": "Worship and guidance (v.5-6)",
        "B_prime": "Not the path of those who earned wrath (v.7a)",
        "A_prime": "Nor of those who went astray (v.7b)",
    },
    "Al-Baqarah": {
        "structure": "A-B-C-D-E-F-E'-D'-C'-B'-A'",
        "center": "Verse 143 - 'Thus We have made you a middle nation'",
        "theme": "The middle nation (wasatan) - balance and justice",
    },
}

# ============================================================
# LETTER POSITION PATTERNS
# ============================================================
# Certain letters appear in specific positions that create patterns.

LETTER_POSITION_PATTERNS = {
    "bismillah_pattern": {
        "verse": "1:1",
        "letters": 19,
        "unique_letters": 10,
        "note": "The opening verse contains exactly 19 Arabic letters",
    },
    "first_revelation": {
        "surah": 96,
        "verses": 5,
        "first_word": "Iqra (Read)",
        "letter_count_first_word": 4,
        "note": "The first revelation emphasizes reading/knowledge",
    },
}

# ============================================================
# NUMERICAL RELATIONSHIPS
# ============================================================

NUMERICAL_RELATIONSHIPS = {
    # Surah number and verse count relationships
    "surah_1": {"number": 1, "verses": 7, "product": 7},
    "surah_19": {"number": 19, "verses": 98, "note": "Maryam - contains Kaf-Ha-Ya-Ayn-Sad"},
    "surah_96": {"number": 96, "verses": 19, "note": "Al-Alaq - first revelation, 19 verses"},

    # 19 x 19 = 361 = sum of first 19 odd numbers
    "nineteen_squared": 361,
    "sum_first_19_odd_numbers": 361,

    # 114 = 19 x 6 = sum of digits pattern
    "surah_count": 114,
    "digit_sum_114": 6,  # 1 + 1 + 4 = 6
    "114_divided_by_19": 6,

    # 6346 verses (counting bismillah as 1:1)
    "total_verses": 6346,
    "6346_divided_by_19": 334,
}


class QuranicHiddenPatterns:
    """Analyzer for hidden patterns in the Quran."""

    def __init__(self):
        self.abjad_values = ABJAD_VALUES
        self.muqattatat = MUQATTATAT_SURAHS
        self.ring_patterns = RING_PATTERNS

    def calculate_abjad_value(self, word: str) -> int:
        """Calculate the abjad numerical value of an Arabic word.

        Args:
            word: Arabic word (transliterated)

        Returns:
            Sum of abjad values for each letter
        """
        total = 0
        for letter in word.lower():
            for abjad_letter, value in self.abjad_values.items():
                if letter in abjad_letter or abjad_letter.startswith(letter):
                    total += value
                    break
        return total

    def get_muqattatat_for_surah(self, surah_number: int) -> str | None:
        """Get the mysterious letters for a given surah."""
        for letters, surahs in self.muqattatat.items():
            if surah_number in surahs:
                return letters
        return None

    def get_ring_composition(self, surah_name: str) -> dict[str, Any] | None:
        """Get the ring composition structure for a surah."""
        return self.ring_patterns.get(surah_name)

    def check_nineteen_relationship(self, surah_number: int, verse_count: int) -> dict[str, Any]:
        """Check if a surah has a 19-based relationship."""
        return {
            "surah_number": surah_number,
            "verse_count": verse_count,
            "surah_divisible_by_19": surah_number % 19 == 0,
            "verses_divisible_by_19": verse_count % 19 == 0,
            "product": surah_number * verse_count,
            "product_divisible_by_19": (surah_number * verse_count) % 19 == 0,
        }

    def get_all_muqattatat(self) -> list[dict[str, Any]]:
        """Return all mysterious letter combinations."""
        results = []
        for letters, surahs in self.muqattatat.items():
            results.append({
                "letters": letters,
                "surahs": surahs,
                "count": len(surahs),
            })
        return results
