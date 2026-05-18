"""Unit tests for PDI-GPT - Prophetic Dream Interpreter."""

import sys
import pytest

sys.path.insert(0, '5.PDI-GPT/src')
from dream_engine import DreamSymbolDictionary, DreamScriptGenerator


@pytest.fixture
def sym_dict():
    return DreamSymbolDictionary("5.PDI-GPT/data/dream_symbols.json")


@pytest.fixture
def generator(sym_dict):
    return DreamScriptGenerator(sym_dict)


class TestDreamSymbolDictionary:
    """Tests for DreamSymbolDictionary class."""

    def test_load_symbols(self, sym_dict):
        assert len(sym_dict.symbols) > 0

    def test_load_actions(self, sym_dict):
        assert len(sym_dict.actions) > 0

    def test_interpret_finds_symbols(self, sym_dict):
        result = sym_dict.interpret("I saw water and a key")
        assert "interpretations" in result
        assert len(result["interpretations"]) > 0

    def test_interpret_returns_verdict(self, sym_dict):
        result = sym_dict.interpret("I saw water")
        assert "verdict" in result
        assert isinstance(result["verdict"], str)

    def test_interpret_no_symbols(self, sym_dict):
        result = sym_dict.interpret("I saw something unknown")
        assert "verdict" in result


class TestDreamScriptGenerator:
    """Tests for DreamScriptGenerator class."""

    def test_generate_returns_dict(self, generator):
        result = generator.generate(goal="guidance", length=3)
        assert isinstance(result, dict)

    def test_generate_has_required_keys(self, generator):
        result = generator.generate(goal="guidance", length=3)
        for key in ["goal", "symbols_used", "narrative", "interpretation"]:
            assert key in result

    def test_generate_with_unknown_goal(self, generator):
        result = generator.generate(goal="unknown_goal", length=3)
        assert result["goal"] == "guidance"  # Falls back to guidance

    def test_generate_different_goals(self, generator):
        for goal in ["healing", "peace", "wealth"]:
            result = generator.generate(goal=goal, length=2)
            assert result["goal"] == goal
