"""Scientific References in the Quran

The Quran contains numerous references to natural phenomena that were unknown
in 7th century Arabia but have been confirmed by modern science. These are not
scientific textbooks, but signs (ayat) for those who reflect.

Key categories:
- Embryology (stages of human development)
- Cosmology (expanding universe, big bang)
- Oceanography (barriers between seas)
- Geology (mountains as pegs)
- Biology (water as source of life)
- Astronomy (orbits, celestial bodies)

"Allah will show them Our signs in the horizons and within themselves
 until it becomes clear to them that it is the truth." (Quran 41:53)
"""

from typing import Any


# ============================================================
# EMBRYOLOGY - STAGES OF HUMAN DEVELOPMENT
# ============================================================
# "Then We made the sperm-drop into a clinging clot, and We made
#  the clot into a lump [of flesh], and We made [from] the lump,
#  bones, and We covered the bones with flesh; then We developed
#  him into another creation. So blessed is Allah, the best of
#  creators." (Quran 23:14)

EMBRYOLOGY_STAGES = {
    "nutfah": {
        "arabic": "نُطْفَة",
        "meaning": "Sperm-drop / zygote",
        "quran_ref": "76:2, 80:19",
        "modern_science": "Fertilized egg (zygote) - single cell formed by union of sperm and egg",
        "stage_number": 1,
    },
    "alaqah": {
        "arabic": "عَلَقَة",
        "meaning": "Clinging clot / leech-like structure",
        "quran_ref": "23:14, 96:2",
        "modern_science": "Implantation stage (days 7-24) - embryo clings to uterine wall like a leech",
        "stage_number": 2,
    },
    "mudghah": {
        "arabic": "مُضْغَة",
        "meaning": "Chewed lump of flesh",
        "quran_ref": "23:14",
        "modern_science": "Somite stage (days 24-28) - embryo looks like chewed gum with tooth marks",
        "stage_number": 3,
    },
    "izam": {
        "arabic": "عِظَام",
        "meaning": "Bones",
        "quran_ref": "23:14",
        "modern_science": "Skeleton formation (week 6-7) - cartilage model of skeleton forms",
        "stage_number": 4,
    },
    "lahm": {
        "arabic": "لَحْم",
        "meaning": "Flesh/muscles covering bones",
        "quran_ref": "23:14",
        "modern_science": "Muscle formation (week 7-8) - muscles form around the bones",
        "stage_number": 5,
    },
    "nash'ah_ukhra": {
        "arabic": "نَشْأَةً أُخْرَى",
        "meaning": "Another creation",
        "quran_ref": "23:14",
        "modern_science": "Fetal stage (week 9+) - distinct human features develop",
        "stage_number": 6,
    },
}

# ============================================================
# COSMOLOGY
# ============================================================

COSMOLOGY_REFERENCES = {
    "big_bang": {
        "quran_ref": "21:30",
        "arabic": "رَأَيْتَ الَّذِينَ كَفَرُوا أَنَّ السَّمَاوَاتِ وَالْأَرْضَ كَانَتَا رَتْقًا فَفَتَقْنَاهُمَا",
        "translation": "Have those who disbelieved not considered that the heavens and the earth were a joined entity, and We separated them?",
        "modern_science": "Big Bang theory - universe began as a singularity and expanded",
        "year_discovered": 1927,  # Lemaitre proposed Big Bang
    },
    "expanding_universe": {
        "quran_ref": "51:47",
        "arabic": "وَالسَّمَاءَ بَنَيْنَاهَا بِأَيْدٍ وَإِنَّا لَمُوسِعُونَ",
        "translation": "And the heaven We constructed with strength, and indeed, We are [its] expander.",
        "modern_science": "Hubble's discovery (1929) - universe is expanding",
        "year_discovered": 1929,
    },
    "orbital_motion": {
        "quran_ref": "21:33",
        "arabic": "وَهُوَ الَّذِي خَلَقَ اللَّيْلَ وَالنَّهَارَ وَالشَّمْسَ وَالْقَمَرَ كُلٌّ فِي فَلَكٍ يَسْبَحُونَ",
        "translation": "And it is He who created the night and the day and the sun and the moon; all [heavenly bodies] in an orbit are swimming.",
        "modern_science": "Celestial bodies move in orbits (Kepler's laws, 1609)",
        "year_discovered": 1609,
    },
    "iron_sent_down": {
        "quran_ref": "57:25",
        "arabic": "وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ وَمَنَافِعُ لِلنَّاسِ",
        "translation": "And We sent down iron, wherein is great military might and benefits for the people.",
        "modern_science": "Iron is formed in supernovae and was delivered to Earth via meteorites",
        "year_discovered": 1950,  # Stellar nucleosynthesis theory
    },
}

# ============================================================
# OCEANOGRAPHY
# ============================================================

OCEANOGRAPHY_REFERENCES = {
    "barrier_between_seas": {
        "quran_ref": "55:19-20",
        "arabic": "مَرَجَ الْبَحْرَيْنِ يَلْتَقِيَانِ بَيْنَهُمَا بَرْزَخٌ لَّا يَبْغِيَانِ",
        "translation": "He released the two seas, meeting [side by side]; Between them is a barrier [so] neither of them transgresses.",
        "modern_science": "Pycnocline zone - density barrier between different bodies of water",
        "year_discovered": 1870,  # Oceanographic research
    },
    "internal_waves": {
        "quran_ref": "24:40",
        "arabic": "أَوْ كَظُلُمَاتٍ فِي بَحْرٍ لُّجِّيٍّ يَغْشَاهُ مَوْجٌ مِّن فَوْقِهِ مَوْجٌ",
        "translation": "Or [they are] like darknesses within an unfathomable sea which is covered by waves, upon which are waves, over which are clouds.",
        "modern_science": "Internal waves in deep ocean - discovered only with modern oceanography",
        "year_discovered": 1900,
    },
    "darkness_in_deep_sea": {
        "quran_ref": "24:40",
        "translation": "Darknesses within an unfathomable sea",
        "modern_science": "No light penetrates below 200m in ocean (aphotic zone)",
        "year_discovered": 1930,  # Bathysphere exploration
    },
}

# ============================================================
# GEOLOGY
# ============================================================

GEOLOGY_REFERENCES = {
    "mountains_as_pegs": {
        "quran_ref": "78:6-7",
        "arabic": "أَلَمْ نَجْعَلِ الْأَرْضَ مِهَادًا وَالْجِبَالَ أَوْتَادًا",
        "translation": "Have We not made the earth a resting place? And the mountains as stakes (pegs)?",
        "modern_science": "Mountains have deep roots (isostasy) - like pegs driven into the earth",
        "year_discovered": 1850,  # Airy's theory of isostasy
    },
    "earth_spherical": {
        "quran_ref": "39:5",
        "arabic": "يُكَوِّرُ اللَّيْلَ عَلَى النَّهَارِ وَيُكَوِّرُ النَّهَارَ عَلَى اللَّيْلِ",
        "translation": "He wraps the night over the day and wraps the day over the night.",
        "modern_science": "The word 'yukawwiru' (wraps) implies spherical shape - wrapping only makes sense on a sphere",
        "year_discovered": 500,  # Known since ancient times, but Quran confirms
    },
}

# ============================================================
# BIOLOGY
# ============================================================

BIOLOGY_REFERENCES = {
    "water_source_of_life": {
        "quran_ref": "21:30",
        "arabic": "وَجَعَلْنَا مِنَ الْمَاءِ كُلَّ شَيْءٍ حَيٍّ",
        "translation": "And We made from water every living thing.",
        "modern_science": "All living cells are primarily composed of water (70-90%)",
        "year_discovered": 1600,
    },
    "pairing_in_creation": {
        "quran_ref": "51:49",
        "arabic": "وَمِن كُلِّ شَيْءٍ خَلَقْنَا زَوْجَيْنِ لَعَلَّكُمْ تَذَكَّرُونَ",
        "translation": "And of all things We created two mates; perhaps you will remember.",
        "modern_science": "All matter exists in pairs (matter/antimatter, positive/negative charge)",
        "year_discovered": 1932,  # Discovery of antimatter
    },
    "frontal_lobe": {
        "quran_ref": "96:15-16",
        "arabic": "كَذَّابًا خَاطِئًا فَلَنَسْفَعًا بِالنَّاصِيَةِ نَاصِيَةٍ كَاذِبَةٍ خَاطِئَةٍ",
        "translation": "A lying, sinning forelock - the forelock of a liar, a sinner.",
        "modern_science": "Prefrontal cortex (front of brain) controls lying and sinning behavior",
        "year_discovered": 1848,  # Phineas Gage case study
    },
    "pain_receptors_in_skin": {
        "quran_ref": "4:56",
        "arabic": "كُلَّمَا نَضِجَتْ جُلُودُهُمْ بَدَّلْنَاهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا الْعَذَابَ",
        "translation": "Every time their skins are roasted through, We will replace them with other skins so they may taste the punishment.",
        "modern_science": "Pain receptors (nociceptors) are located in the skin",
        "year_discovered": 1660,
    },
}

# ============================================================
# METEOROLOGY
# ============================================================

METEOROLOGY_REFERENCES = {
    "wind_fertilization": {
        "quran_ref": "15:22",
        "arabic": "وَأَرْسَلْنَا الرِّيَاحَ لَوَاقِحَ",
        "translation": "And We have sent the fertilizing winds.",
        "modern_science": "Wind carries pollen and also helps form rain clouds",
        "year_discovered": 1700,
    },
    "rain_from_clouds": {
        "quran_ref": "24:43",
        "translation": "Do you not see that Allah drives clouds? Then He brings them together, then He makes them into a mass, and you see the rain emerge from within it.",
        "modern_science": "Cloud formation and precipitation process",
        "year_discovered": 1800,
    },
}


class QuranicScientificReferences:
    """Analyzer for scientific references in the Quran."""

    def __init__(self):
        self.embryology = EMBRYOLOGY_STAGES
        self.cosmology = COSMOLOGY_REFERENCES
        self.oceanography = OCEANOGRAPHY_REFERENCES
        self.geology = GEOLOGY_REFERENCES
        self.biology = BIOLOGY_REFERENCES
        self.meteorology = METEOROLOGY_REFERENCES

    def get_embryology_stages(self) -> list[dict[str, Any]]:
        """Return all embryology stages in order."""
        return sorted(
            self.embryology.values(),
            key=lambda x: x["stage_number"],
        )

    def get_references_by_category(self, category: str) -> dict[str, Any]:
        """Get scientific references by category."""
        categories = {
            "embryology": self.embryology,
            "cosmology": self.cosmology,
            "oceanography": self.oceanography,
            "geology": self.geology,
            "biology": self.biology,
            "meteorology": self.meteorology,
        }
        return categories.get(category, {})

    def get_all_references(self) -> list[dict[str, Any]]:
        """Return all scientific references."""
        all_refs = []
        for category in [
            self.embryology,
            self.cosmology,
            self.oceanography,
            self.geology,
            self.biology,
            self.meteorology,
        ]:
            for key, data in category.items():
                ref = {"category": key, **data}
                all_refs.append(ref)
        return all_refs

    def count_total_references(self) -> int:
        """Count total scientific references."""
        total = 0
        for category in [
            self.embryology,
            self.cosmology,
            self.oceanography,
            self.geology,
            self.biology,
            self.meteorology,
        ]:
            total += len(category)
        return total
