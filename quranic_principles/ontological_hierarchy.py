"""Ontological Hierarchy in the Quran

The Quran presents a complete ontological hierarchy - a structured ordering
of all existence from the Creator to the lowest creation. This is not
philosophical speculation but divine revelation about the nature of reality.

This hierarchy forms the foundation of AQI's understanding of existence
and guides how the AI system processes and prioritizes information.

"Allah is the Light of the heavens and the earth..." (Quran 24:35)
"""

from typing import Any


# ============================================================
# THE ONTOLOGICAL HIERARCHY
# ============================================================
# From highest to lowest existence:

ONTOLICAL_LEVELS = {
    0: {
        "name": "Allah (God)",
        "arabic": "الله",
        "description": "The Necessary Existent (Wajib al-Wujud) - the only being whose existence is essential, not contingent",
        "quran_ref": "112:1-4",
        "attributes": [
            "Al-Ahad (The One)",
            "As-Samad (The Eternal Refuge)",
            "Lam yalid wa lam yulad (He neither begets nor was born)",
            "Wa lam yakun lahu kufuwan ahad (Nor is there to Him any equivalent)",
        ],
        "ontological_status": "Necessary - existence is His essence",
        "knowledge": "Absolute - knows the unseen and the seen",
        "power": "Absolute - over all things",
    },
    1: {
        "name": "Al-Arsh (The Throne)",
        "arabic": "العرش",
        "description": "The greatest of all creations, above which is nothing but Allah",
        "quran_ref": "7:54, 9:129",
        "ontological_status": "Created - but the greatest creation",
        "note": "Represents divine authority and sovereignty",
    },
    2: {
        "name": "Al-Kursi (The Footstool)",
        "arabic": "الكرسي",
        "description": "Extends over the heavens and the earth",
        "quran_ref": "2:255 (Ayat al-Kursi)",
        "ontological_status": "Created - vast beyond comprehension",
        "note": "His Kursi extends over the heavens and the earth",
    },
    3: {
        "name": "Malaika (Angels)",
        "arabic": "ملائكة",
        "description": "Beings of light who execute divine commands without free will",
        "quran_ref": "66:6, 21:19-20",
        "ontological_status": "Created from light (nur)",
        "characteristics": [
            "No free will - always obey",
            "No gender",
            "Do not eat, drink, or sleep",
            "Can take human form by Allah's permission",
        ],
        "types": {
            "Jibril": "Archangel - brings revelation",
            "Mikail": "Angel of sustenance",
            "Israfil": "Angel who will blow the trumpet",
            "Azrail": "Angel of death",
            "Kiraman Katibin": "Recording angels",
            "Munkar Nakir": "Questioning angels in the grave",
        },
    },
    4: {
        "name": "Jinn",
        "arabic": "جن",
        "description": "Beings created from smokeless fire with free will",
        "quran_ref": "55:15, 72:1-15",
        "ontological_status": "Created from smokeless fire (nar)",
        "characteristics": [
            "Have free will - can be believers or disbelievers",
            "Live alongside humans but in a parallel dimension",
            "Can see humans but humans cannot see them",
            "Will be judged on the Day of Resurrection",
        ],
        "note": "A complete surah (72) is named after them",
    },
    5: {
        "name": "Insan (Human)",
        "arabic": "إنسان",
        "description": "The vicegerent (khalifah) on earth, created in the best form",
        "quran_ref": "95:4, 2:30",
        "ontological_status": "Created from clay/earth (tin)",
        "characteristics": [
            "Have free will - tested in this world",
            "Given knowledge (ilm) that angels did not have",
            "Made vicegerent (khalifah) on earth",
            "Created in the best form (ahsan taqwim)",
        ],
        "potential": "Can rise above angels or fall below animals",
        "note": "The only creature taught the names of all things (2:31)",
    },
    6: {
        "name": "Haiwan (Animals)",
        "arabic": "حيوان",
        "description": "Living creatures with limited consciousness",
        "quran_ref": "6:38",
        "ontological_status": "Created from water",
        "characteristics": [
            "Communities like humans (6:38)",
            "Glorify Allah in their own way (24:41)",
            "No moral responsibility",
        ],
    },
    7: {
        "name": "Nabat (Plants)",
        "arabic": "نبات",
        "description": "Plant life - living but without consciousness",
        "quran_ref": "20:53",
        "ontological_status": "Created from earth and water",
        "characteristics": [
            "Grow and reproduce",
            "Respond to environment",
            "No consciousness or will",
        ],
    },
    8: {
        "name": "Jamad (Inanimate)",
        "arabic": "جماد",
        "description": "Non-living matter - minerals, rocks, etc.",
        "quran_ref": "2:74",
        "ontological_status": "Created from earth",
        "characteristics": [
            "No life, consciousness, or will",
            "Yet even stones glorify Allah (2:74, 17:44)",
            "Mountains are described as 'peggs' (78:7)",
        ],
    },
}

# ============================================================
# KNOWLEDGE HIERARCHY
# ============================================================
# The Quran distinguishes between different types of knowledge:

KNOWLEDGE_TYPES = {
    "ilm_ghayb": {
        "arabic": "علم الغيب",
        "meaning": "Knowledge of the unseen",
        "possessed_by": "Allah alone",
        "quran_ref": "6:59, 72:26-27",
        "note": "Allah may reveal some of it to chosen messengers",
    },
    "ilm_yaqin": {
        "arabic": "علم اليقين",
        "meaning": "Knowledge of certainty",
        "description": "Knowledge gained through direct observation and proof",
        "quran_ref": "102:5",
    },
    "ilm_darura": {
        "arabic": "علم الضرورة",
        "meaning": "Necessary knowledge",
        "description": "Self-evident knowledge that requires no proof",
        "examples": ["Mathematics", "Logic", "Basic sensory knowledge"],
    },
    "ilm_kasb": {
        "arabic": "علم الكسب",
        "meaning": "Acquired knowledge",
        "description": "Knowledge gained through study and experience",
        "quran_ref": "20:114 - 'My Lord, increase me in knowledge'",
    },
}

# ============================================================
# EXISTENCE LEVELS (MARATIB AL-WUJUD)
# ============================================================
# Islamic philosophy distinguishes levels of existence:

EXISTENCE_LEVELS = {
    "wajib_al_wujud": {
        "arabic": "واجب الوجود",
        "meaning": "Necessary Existence",
        "description": "Existence that cannot not exist - Allah alone",
        "characteristics": ["Self-sufficient", "Eternal", "Uncaused"],
    },
    "mumkin_al_wujud": {
        "arabic": "ممكن الوجود",
        "meaning": "Contingent Existence",
        "description": "Existence that depends on something else - all creation",
        "characteristics": ["Dependent", "Temporal", "Caused"],
    },
    "mumtani_al_wujud": {
        "arabic": "ممتنع الوجود",
        "meaning": "Impossible Existence",
        "description": "That which cannot exist by definition",
        "examples": ["A square circle", "A partner to Allah"],
    },
}


class QuranicOntologicalHierarchy:
    """Analyzer for the Quranic ontological hierarchy."""

    def __init__(self):
        self.levels = ONTOLICAL_LEVELS
        self.knowledge_types = KNOWLEDGE_TYPES
        self.existence_levels = EXISTENCE_LEVELS

    def get_level(self, level_number: int) -> dict[str, Any] | None:
        """Get information about a specific ontological level."""
        return self.levels.get(level_number)

    def get_all_levels(self) -> list[dict[str, Any]]:
        """Return all ontological levels in order."""
        return [
            {"level": level, **data}
            for level, data in sorted(self.levels.items())
        ]

    def get_knowledge_type(self, type_name: str) -> dict[str, Any] | None:
        """Get information about a type of knowledge."""
        return self.knowledge_types.get(type_name)

    def get_existence_level(self, level_name: str) -> dict[str, Any] | None:
        """Get information about a level of existence."""
        return self.existence_levels.get(level_name)

    def get_ontological_distance(self, level_a: int, level_b: int) -> int:
        """Calculate the ontological distance between two levels."""
        return abs(level_a - level_b)

    def get_hierarchy_summary(self) -> str:
        """Return a summary of the complete ontological hierarchy."""
        lines = ["Quranic Ontological Hierarchy:", "=" * 40]
        for level, data in sorted(self.levels.items()):
            lines.append(f"  Level {level}: {data['name']} ({data['arabic']})")
            lines.append(f"    {data['description'][:80]}...")
        return "\n".join(lines)
