import pygame

from src.configs.default_config import DefaultConfig
from src.models.player_model import PlayerModel
from src.ui.interface_game import InterfaceGame


class TestInterfaceGameTitle:
    def test_title_is_string(self) -> None:
        assert isinstance(InterfaceGame.TITLE, str)

    def test_title_value(self) -> None:
        assert InterfaceGame.TITLE == "Template Pygame"


class TestInterfaceGameInitialState:
    def test_game_started_is_false(self, interface_game: InterfaceGame) -> None:
        assert interface_game.game_started is False

    def test_game_started_is_bool(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.game_started, bool)

    def test_screen_is_surface(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.screen, pygame.Surface)

    def test_screen_width(self, interface_game: InterfaceGame) -> None:
        assert interface_game.screen.get_width() == 800

    def test_screen_height(self, interface_game: InterfaceGame) -> None:
        assert interface_game.screen.get_height() == 400

    def test_clock_is_clock(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.clock, pygame.time.Clock)


class TestInterfaceGameConfig:
    def test_config_is_returned(self, interface_game: InterfaceGame, default_config: DefaultConfig) -> None:
        assert interface_game.config is default_config

    def test_config_is_default_config_instance(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.config, DefaultConfig)

    def test_config_debug_flag(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.config.DEBUG, bool)

    def test_config_testing_flag(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.config.TESTING, bool)


class TestInterfaceGamePlayer:
    def test_player_single_group_is_group_single(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.player_single_group, pygame.sprite.GroupSingle)

    def test_player_single_group_has_one_sprite(self, interface_game: InterfaceGame) -> None:
        assert len(interface_game.player_single_group.sprites()) == 1

    def test_player_is_player_model(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.player, PlayerModel)

    def test_player_is_sprite(self, interface_game: InterfaceGame) -> None:
        assert isinstance(interface_game.player, pygame.sprite.Sprite)

    def test_player_in_group(self, interface_game: InterfaceGame) -> None:
        assert interface_game.player in interface_game.player_single_group.sprites()
