import pygame

from src.models.player_model import PlayerModel
from test.conftest import MockKeys


class TestPlayerModelInitialState:
    def test_walk_index_is_zero(self, player: PlayerModel) -> None:
        assert player._walk_index == 0.0

    def test_walk_index_is_float(self, player: PlayerModel) -> None:
        assert isinstance(player._walk_index, float)

    def test_gravity_is_zero(self, player: PlayerModel) -> None:
        assert player._gravity == 0

    def test_is_grounded_on_spawn(self, player: PlayerModel) -> None:
        assert player.is_grounded is True

    def test_is_not_jumping_on_spawn(self, player: PlayerModel) -> None:
        assert player.is_jumping is False

    def test_spawn_bottom_at_ground(self, player: PlayerModel) -> None:
        assert player.rect.bottom == 300

    def test_spawn_midx(self, player: PlayerModel) -> None:
        assert player.rect.midbottom[0] == 80

    def test_image_is_surface(self, player: PlayerModel) -> None:
        assert isinstance(player.image, pygame.Surface)

    def test_rect_is_rect(self, player: PlayerModel) -> None:
        assert isinstance(player.rect, pygame.Rect)

    def test_walk_frames_count(self, player: PlayerModel) -> None:
        assert len(player._walk_frames) == 2

    def test_walk_frames_are_surfaces(self, player: PlayerModel) -> None:
        assert all(isinstance(f, pygame.Surface) for f in player._walk_frames)

    def test_jump_frame_is_surface(self, player: PlayerModel) -> None:
        assert isinstance(player._jump_frame, pygame.Surface)


class TestPlayerModelProperties:
    def test_is_grounded_true_when_at_ground(self, player: PlayerModel) -> None:
        player.rect.bottom = 300
        assert player.is_grounded is True

    def test_is_grounded_true_when_below_ground(self, player: PlayerModel) -> None:
        player.rect.bottom = 350
        assert player.is_grounded is True

    def test_is_grounded_false_when_above_ground(self, player: PlayerModel) -> None:
        player.rect.bottom = 200
        assert player.is_grounded is False

    def test_is_jumping_false_when_grounded(self, player: PlayerModel) -> None:
        player.rect.bottom = 300
        assert player.is_jumping is False

    def test_is_jumping_true_when_above_ground(self, player: PlayerModel) -> None:
        player.rect.bottom = 100
        assert player.is_jumping is True

    def test_is_jumping_is_inverse_of_is_grounded(self, player: PlayerModel) -> None:
        player.rect.bottom = 150
        assert player.is_jumping is not player.is_grounded


class TestPlayerModelGravity:
    def test_gravity_increments_each_call(self, player: PlayerModel) -> None:
        player._gravity = 0
        player.rect.bottom = 100
        player._apply_gravity()
        assert player._gravity == 1

    def test_rect_moves_down_when_gravity_applied(self, player: PlayerModel) -> None:
        player._gravity = 5
        player.rect.bottom = 100
        old_y = player.rect.y
        player._apply_gravity()
        assert player.rect.y > old_y

    def test_gravity_resets_on_landing(self, player: PlayerModel) -> None:
        player._gravity = 10
        player.rect.bottom = 310
        player._apply_gravity()
        assert player._gravity == 0

    def test_bottom_clamped_at_ground_level(self, player: PlayerModel) -> None:
        player._gravity = 100
        player.rect.bottom = 400
        player._apply_gravity()
        assert player.rect.bottom == 300

    def test_gravity_accumulates_while_airborne(self, player: PlayerModel) -> None:
        player._gravity = 0
        player.rect.bottom = 50
        player._apply_gravity()
        player._apply_gravity()
        assert player._gravity == 2


class TestPlayerModelClampPosition:
    def test_clamp_at_left_boundary(self, player: PlayerModel) -> None:
        player.rect.x = -50
        player._clamp_position()
        assert player.rect.x == 0

    def test_clamp_at_right_boundary(self, player: PlayerModel) -> None:
        player.rect.x = 1000
        player._clamp_position()
        assert player.rect.x == 735

    def test_no_clamp_when_within_bounds(self, player: PlayerModel) -> None:
        player.rect.x = 400
        player._clamp_position()
        assert player.rect.x == 400

    def test_no_clamp_at_left_edge(self, player: PlayerModel) -> None:
        player.rect.x = 0
        player._clamp_position()
        assert player.rect.x == 0

    def test_no_clamp_at_right_edge(self, player: PlayerModel) -> None:
        player.rect.x = 735
        player._clamp_position()
        assert player.rect.x == 735


class TestPlayerModelInput:
    def test_jump_sets_gravity_when_grounded(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 300
        player._input(mock_keys({pygame.K_SPACE}))
        assert player._gravity == -20

    def test_jump_not_triggered_when_airborne(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 100
        player._gravity = -10
        player._input(mock_keys({pygame.K_SPACE}))
        assert player._gravity == -10

    def test_move_right_increments_x(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        initial_x = player.rect.x
        player._input(mock_keys({pygame.K_d}))
        assert player.rect.x == initial_x + 2

    def test_move_left_decrements_x(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.x = 200
        player._input(mock_keys({pygame.K_a}))
        assert player.rect.x == 198

    def test_no_input_does_not_change_state(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        initial_x = player.rect.x
        initial_gravity = player._gravity
        player._input(mock_keys())
        assert player.rect.x == initial_x
        assert player._gravity == initial_gravity

    def test_space_takes_priority_over_d_when_grounded(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 300
        initial_x = player.rect.x
        player._input(mock_keys({pygame.K_SPACE, pygame.K_d}))
        assert player._gravity == -20
        assert player.rect.x == initial_x


class TestPlayerModelAnimate:
    def test_jump_frame_when_airborne(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 100
        player._animate(mock_keys())
        assert player.image is player._jump_frame

    def test_walk_frame_when_moving_right(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 300
        player._animate(mock_keys({pygame.K_d}))
        assert player.image in player._walk_frames

    def test_walk_frame_when_moving_left(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 300
        player._animate(mock_keys({pygame.K_a}))
        assert player.image in player._walk_frames

    def test_idle_frame_when_not_moving(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 300
        player._animate(mock_keys())
        assert player.image is player._walk_frames[0]

    def test_walk_index_advances_when_moving(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 300
        player._walk_index = 0.0
        player._animate(mock_keys({pygame.K_d}))
        assert player._walk_index > 0.0

    def test_walk_index_resets_when_idle(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 300
        player._walk_index = 1.5
        player._animate(mock_keys())
        assert player._walk_index == 0.0

    def test_walk_index_wraps_around(self, player: PlayerModel, mock_keys: type[MockKeys]) -> None:
        player.rect.bottom = 300
        player._walk_index = 1.95
        player._animate(mock_keys({pygame.K_d}))
        assert player._walk_index < 1.0
