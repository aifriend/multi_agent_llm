import pytest

from src.service import Tools as tools_module
from src.service.Tools import Tools


@pytest.fixture(autouse=True)
def no_dotenv(monkeypatch):
    # Never read a developer's real .env file during tests.
    monkeypatch.setattr(tools_module, "load_dotenv", lambda *a, **k: None)


def test_openai_key_is_returned(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    assert Tools.get_openai_api_key() == "sk-test"


def test_openai_key_missing_raises(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        Tools.get_openai_api_key()


def test_serper_key_is_returned(monkeypatch):
    monkeypatch.setenv("SERPER_API_KEY", "serper-test")
    assert Tools.get_serper_api_key() == "serper-test"


def test_serper_key_missing_raises(monkeypatch):
    monkeypatch.delenv("SERPER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="SERPER_API_KEY"):
        Tools.get_serper_api_key()
