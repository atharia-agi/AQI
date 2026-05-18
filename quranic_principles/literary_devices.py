"""Literary Devices in the Quran

The Quran's literary excellence is considered its primary miracle (i'jaz).
No human has been able to produce anything comparable, despite the challenge
being issued repeatedly.

"Say, 'If mankind and the jinn gathered in order to produce the like of this
 Quran, they could not produce the like of it, even if they were to each
 other assistants.'" (Quran 17:88)

Key literary devices:
- Metaphor and simile (tashbih, isti'arah)
- Parable (mathal)
- Oath (qasam)
- Rhetorical questions
- Chiasmus (ring composition)
- Repetition with variation
- Wordplay and phonetic patterns
"""

from typing import Any


# ============================================================
# METAPHOR AND SIMILE
# ============================================================

METAPHORS = {
    "light_verse": {
        "quran_ref": "24:35",
        "type": "extended_metaphor",
        "text": "Allah is the Light of the heavens and the earth. The example of His light is like a niche within which is a lamp, the lamp is within glass, the glass as if it were a pearly [white] star lit from [the oil of] a blessed olive tree...",
        "layers": 7,  # Seven layers of metaphor in this single verse
        "theme": "Divine guidance and knowledge",
    },
    "hypocrites_fire": {
        "quran_ref": "2:17-20",
        "type": "extended_metaphor",
        "text": "Their example is that of one who kindled a fire, but when it illuminated what was around him, Allah took away their light and left them in darkness...",
        "theme": "Hypocrisy and loss of guidance",
    },
    "spider_web": {
        "quran_ref": "29:41",
        "type": "simile",
        "text": "The example of those who take allies other than Allah is like that of the spider who takes a home. And indeed, the weakest of homes is the home of the spider.",
        "theme": "False reliance on anything other than Allah",
    },
    "good_word_good_tree": {
        "quran_ref": "14:24-25",
        "type": "simile",
        "text": "Have you not considered how Allah presents an example, [making] a good word like a good tree, whose root is firmly fixed and its branches [high] in the sky?",
        "theme": "Faith and its stability",
    },
}

# ============================================================
# PARABLES (AMTHAL)
# ============================================================

PARABLES = {
    "two_paths": {
        "quran_ref": "90:10",
        "text": "And have We not shown him the two ways?",
        "theme": "Free will and moral choice",
    },
    "blind_and_seeing": {
        "quran_ref": "35:19-20",
        "text": "Not equal are the blind and the seeing, nor are the darknesses and the light.",
        "theme": "Knowledge vs ignorance",
    },
    "dead_and_alive": {
        "quran_ref": "35:22",
        "text": "Not equal are the living and the dead.",
        "theme": "Spiritual life vs spiritual death",
    },
    "owner_of_two_gardens": {
        "quran_ref": "18:32-44",
        "type": "narrative_parable",
        "theme": "Arrogance of wealth and its loss",
    },
    "companion_of_two_men": {
        "quran_ref": "18:37-39",
        "type": "narrative_parable",
        "theme": "Faith vs materialism",
    },
}

# ============================================================
# OATHS (QASAM)
# ============================================================
# The Quran frequently begins surahs with oaths by natural phenomena.

OATHS = {
    "by_the_fig": {
        "quran_ref": "95:1",
        "text": "By the fig and the olive",
        "significance": "Fruits mentioned for their nutritional and symbolic value",
    },
    "by_the_morning_brightness": {
        "quran_ref": "93:1-2",
        "text": "By the morning brightness, and [by] the night when it covers with darkness",
        "significance": "Contrast between light and darkness as metaphor for guidance",
    },
    "by_the_sun": {
        "quran_ref": "91:1-2",
        "text": "By the sun and its brightness, and [by] the moon when it follows it",
        "significance": "Celestial order as witness to divine design",
    },
    "by_the_night": {
        "quran_ref": "92:1-2",
        "text": "By the night when it covers, and [by] the day when it appears",
        "significance": "Cycle of day and night as sign of Allah's power",
    },
    "by_time": {
        "quran_ref": "103:1",
        "text": "By time, indeed mankind is in loss",
        "significance": "Time as the most precious resource",
    },
}

# ============================================================
# RHETORICAL QUESTIONS
# ============================================================

RHETORICAL_QUESTIONS = {
    "is_there_any_creator": {
        "quran_ref": "35:3",
        "text": "Is there any creator other than Allah who provides for you from the heaven and earth?",
        "expected_answer": "No",
        "purpose": "Affirmation of Allah as the sole creator",
    },
    "do_they_not_look": {
        "quran_ref": "88:17-20",
        "text": "Do they not look at the camels - how they are created? And at the sky - how it is raised? And at the mountains - how they are erected? And at the earth - how it is spread out?",
        "expected_answer": "Yes, they should look",
        "purpose": "Encouragement to observe and reflect on creation",
    },
    "who_provides_for_you": {
        "quran_ref": "67:21",
        "text": "Who is it that could provide for you if He withheld His provision?",
        "expected_answer": "No one",
        "purpose": "Reminder of dependence on Allah",
    },
}

# ============================================================
# REPETITION WITH VARIATION
# ============================================================
# The Quran repeats certain phrases with subtle variations that
# create deeper meanings.

REPETITION_PATTERNS = {
    "which_of_favors": {
        "phrase": "فَبِأَيِّ آلَاءِ رَبِّكُمَا تُكَذِّبَانِ",
        "translation": "So which of the favors of your Lord would you deny?",
        "repetitions": 31,
        "surah": "Ar-Rahman (55)",
        "pattern": "Repeated after each blessing mentioned",
        "effect": "Builds emotional and spiritual impact",
    },
    "bismillah": {
        "phrase": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
        "translation": "In the name of Allah, the Most Gracious, the Most Merciful",
        "repetitions": 114,
        "pattern": "Opens every surah except At-Tawbah",
        "effect": "Constant reminder of divine mercy",
    },
}


class QuranicLiteraryDevices:
    """Analyzer for literary devices in the Quran."""

    def __init__(self):
        self.metaphors = METAPHORS
        self.parables = PARABLES
        self.oaths = OATHS
        self.rhetorical_questions = RHETORICAL_QUESTIONS
        self.repetition_patterns = REPETITION_PATTERNS

    def get_metaphors(self) -> list[dict[str, Any]]:
        """Return all metaphors."""
        return [
            {"name": name, **data}
            for name, data in self.metaphors.items()
        ]

    def get_parables(self) -> list[dict[str, Any]]:
        """Return all parables."""
        return [
            {"name": name, **data}
            for name, data in self.parables.items()
        ]

    def get_oaths(self) -> list[dict[str, Any]]:
        """Return all oaths."""
        return [
            {"name": name, **data}
            for name, data in self.oaths.items()
        ]

    def get_rhetorical_questions(self) -> list[dict[str, Any]]:
        """Return all rhetorical questions."""
        return [
            {"name": name, **data}
            for name, data in self.rhetorical_questions.items()
        ]

    def get_repetition_patterns(self) -> list[dict[str, Any]]:
        """Return all repetition patterns."""
        return [
            {"name": name, **data}
            for name, data in self.repetition_patterns.items()
        ]

    def analyze_literary_complexity(self, verse_ref: str) -> dict[str, Any]:
        """Analyze the literary complexity of a verse.

        This is a placeholder - in production, this would use NLP to
        identify literary devices in any given verse.
        """
        return {
            "verse": verse_ref,
            "devices_found": [],
            "complexity_score": 0.0,
            "note": "Full NLP analysis requires Quran text corpus",
        }
