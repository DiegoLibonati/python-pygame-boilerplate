import os

from src.constants import paths


class TestSoundPaths:
    def test_sound_music_is_str(self) -> None:
        assert isinstance(paths.SOUND_MUSIC, str)

    def test_sound_music_extension(self) -> None:
        assert paths.SOUND_MUSIC.endswith(".wav")

    def test_sound_music_file_exists(self) -> None:
        assert os.path.isfile(paths.SOUND_MUSIC)

    def test_sound_player_jump_is_str(self) -> None:
        assert isinstance(paths.SOUND_PLAYER_JUMP, str)

    def test_sound_player_jump_extension(self) -> None:
        assert paths.SOUND_PLAYER_JUMP.endswith(".mp3")

    def test_sound_player_jump_file_exists(self) -> None:
        assert os.path.isfile(paths.SOUND_PLAYER_JUMP)


class TestFontPaths:
    def test_font_primary_is_str(self) -> None:
        assert isinstance(paths.FONT_PRIMARY, str)

    def test_font_primary_extension(self) -> None:
        assert paths.FONT_PRIMARY.endswith(".ttf")

    def test_font_primary_file_exists(self) -> None:
        assert os.path.isfile(paths.FONT_PRIMARY)


class TestGraphicPaths:
    def test_graphic_sky_is_str(self) -> None:
        assert isinstance(paths.GRAPHIC_SKY, str)

    def test_graphic_sky_extension(self) -> None:
        assert paths.GRAPHIC_SKY.endswith(".png")

    def test_graphic_sky_file_exists(self) -> None:
        assert os.path.isfile(paths.GRAPHIC_SKY)

    def test_graphic_ground_is_str(self) -> None:
        assert isinstance(paths.GRAPHIC_GROUND, str)

    def test_graphic_ground_extension(self) -> None:
        assert paths.GRAPHIC_GROUND.endswith(".png")

    def test_graphic_ground_file_exists(self) -> None:
        assert os.path.isfile(paths.GRAPHIC_GROUND)

    def test_graphic_player_stand_is_str(self) -> None:
        assert isinstance(paths.GRAPHIC_PLAYER_STAND, str)

    def test_graphic_player_stand_extension(self) -> None:
        assert paths.GRAPHIC_PLAYER_STAND.endswith(".png")

    def test_graphic_player_stand_file_exists(self) -> None:
        assert os.path.isfile(paths.GRAPHIC_PLAYER_STAND)

    def test_graphic_player_walk_1_is_str(self) -> None:
        assert isinstance(paths.GRAPHIC_PLAYER_WALK_1, str)

    def test_graphic_player_walk_1_extension(self) -> None:
        assert paths.GRAPHIC_PLAYER_WALK_1.endswith(".png")

    def test_graphic_player_walk_1_file_exists(self) -> None:
        assert os.path.isfile(paths.GRAPHIC_PLAYER_WALK_1)

    def test_graphic_player_walk_2_is_str(self) -> None:
        assert isinstance(paths.GRAPHIC_PLAYER_WALK_2, str)

    def test_graphic_player_walk_2_extension(self) -> None:
        assert paths.GRAPHIC_PLAYER_WALK_2.endswith(".png")

    def test_graphic_player_walk_2_file_exists(self) -> None:
        assert os.path.isfile(paths.GRAPHIC_PLAYER_WALK_2)

    def test_graphic_player_jump_is_str(self) -> None:
        assert isinstance(paths.GRAPHIC_PLAYER_JUMP, str)

    def test_graphic_player_jump_extension(self) -> None:
        assert paths.GRAPHIC_PLAYER_JUMP.endswith(".png")

    def test_graphic_player_jump_file_exists(self) -> None:
        assert os.path.isfile(paths.GRAPHIC_PLAYER_JUMP)
