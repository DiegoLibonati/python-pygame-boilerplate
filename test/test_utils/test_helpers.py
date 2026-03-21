import os

from src.utils.helpers import resource_path


class TestResourcePath:
    def test_returns_string(self) -> None:
        assert isinstance(resource_path("any/path.txt"), str)

    def test_returns_absolute_path(self) -> None:
        result = resource_path("any/path.txt")
        assert os.path.isabs(result)

    def test_starts_with_cwd_in_dev_mode(self) -> None:
        result = resource_path("test.txt")
        assert result.startswith(os.path.abspath("."))

    def test_ends_with_relative_path(self) -> None:
        relative = os.path.join("assets", "img.png")
        result = resource_path(relative)
        assert result.endswith(relative)

    def test_relative_path_is_preserved(self) -> None:
        result = resource_path("foo.txt")
        assert "foo.txt" in result

    def test_nested_relative_path_is_preserved(self) -> None:
        relative = os.path.join("src", "assets", "sounds", "game.wav")
        result = resource_path(relative)
        assert result.endswith(relative)
