# Template-Pygame

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

Personal template for creating games with PyGame.

## Technologies used

1. Python >= 3.11

## Libraries used

#### Requirements.txt

```
pygame==2.6.1
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio link

[`https://www.diegolibonati.com.ar/#/project/Template-Pygame`](https://www.diegolibonati.com.ar/#/project/Template-Pygame)

## Video

https://user-images.githubusercontent.com/99032604/201543320-020d09af-9266-4a0b-8fff-dbaf4083f587.mp4

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Env Keys

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.
2. `ENV_NAME`: A custom environment variable for template demonstration purposes.

```
ENVIRONMENT=development
ENV_NAME=template_value
```

## Project Structure

```
Template-Pygame/
├── src/
│   ├── configs/
│   │   ├── __init__.py
│   │   ├── default_config.py
│   │   ├── development_config.py
│   │   ├── production_config.py
│   │   ├── testing_config.py
│   │   └── logger_config.py
│   ├── constants/
│   │   ├── __init__.py
│   │   └── paths.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── player_model.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── interface_game.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── assets/
│   │   ├── fonts/
│   │   ├── graphics/
│   │   └── sounds/
│   ├── __init__.py
│   └── __main__.py
├── test/
│   ├── test_configs/
│   │   ├── __init__.py
│   │   ├── test_default_config.py
│   │   ├── test_development_config.py
│   │   ├── test_logger_config.py
│   │   ├── test_production_config.py
│   │   └── test_testing_config.py
│   ├── test_constants/
│   │   ├── __init__.py
│   │   └── test_paths.py
│   ├── test_models/
│   │   ├── __init__.py
│   │   └── test_player_model.py
│   ├── test_ui/
│   │   ├── __init__.py
│   │   └── test_interface_game.py
│   ├── test_utils/
│   │   ├── __init__.py
│   │   └── test_helpers.py
│   ├── __init__.py
│   └── conftest.py
├── app.py
├── pyproject.toml
├── requirements.txt
├── requirements.dev.txt
├── requirements.test.txt
├── requirements.build.txt
├── app.spec
├── build.bat
├── build.sh
├── .env
├── .env.example.dev
├── .env.example.prod
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
└── README.md
```

1. `src` -> Root directory of the source code. Contains the full application logic following a **layered architecture** pattern.
2. `configs` -> Contains all **configuration classes** organized by environment (development, production, testing). Includes logging setup and application settings.
3. `constants` -> Holds **static values** like asset paths, centralized in `paths.py` for use across the entire application.
4. `models` -> Defines **Pygame sprite subclasses** that represent game entities. Each model manages its own input, physics, animation, and boundaries.
5. `ui` -> Contains the **game interface logic**. `interface_game.py` acts as the main orchestrator: handles the game loop, event processing, and rendering states (intro / in-game).
6. `utils` -> Contains **shared utilities**. `helpers.py` provides `resource_path()` to resolve asset paths both in development and inside a PyInstaller bundle.
7. `assets` -> Static game files: **graphics** (sprites, backgrounds), **sounds** (music, effects), and **fonts**.
8. `test` -> Contains **tests** organized to mirror the `src/` structure.
9. `conftest.py` -> Defines **pytest fixtures** for application setup and test data.
10. `app.py` -> The **application entry point**. Loads the environment, selects the config class, and launches the game.
11. `pyproject.toml` -> **Unified project configuration** for pytest, ruff, and project metadata.
12. `requirements.txt` -> Lists **production dependencies**.
13. `requirements.dev.txt` -> Lists **development dependencies** (pre-commit, pip-audit).
14. `requirements.test.txt` -> Lists **testing dependencies** (pytest and plugins).
15. `requirements.build.txt` -> Lists **build dependencies** (PyInstaller).
16. `app.spec` -> **PyInstaller configuration** for generating standalone executables. Bundles `src/assets/` and `.env` into the binary.

## Architecture & Design Patterns

### Layered Architecture

The project follows a **layered architecture** that separates responsibilities into distinct layers. Each layer only communicates with the one directly below it, which makes the codebase easier to maintain, test, and extend.

```
┌─────────────────────────────┐
│         Entry Point         │  app.py
├─────────────────────────────┤
│        UI / Interface       │  src/ui/
├─────────────────────────────┤
│           Models            │  src/models/
├─────────────────────────────┤
│     Configs / Constants     │  src/configs/  src/constants/
├─────────────────────────────┤
│           Utils             │  src/utils/
└─────────────────────────────┘
```

---

### Design Patterns Used

#### 1. Environment-based Configuration (Strategy Pattern)
Configuration is selected at runtime based on the `ENVIRONMENT` variable. All config classes inherit from `DefaultConfig`, and `app.py` uses a `CONFIG_MAP` dictionary to pick the right class without conditionals.

```python
# app.py
CONFIG_MAP = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
config = CONFIG_MAP.get(environment, ProductionConfig)()
```

This makes it trivial to add a new environment by defining a new class and registering it in the map.

---

#### 2. Game Loop Pattern
`InterfaceGame` implements the standard **game loop**: process input → update state → render → repeat at a fixed frame rate. The loop is split into focused private methods to keep each responsibility isolated.

```python
def game_loop(self) -> None:
    while True:
        self._handle_events()   # input
        if self._game_started:
            self._render_game() # update + render
        else:
            self._render_intro()
        pygame.display.update()
        self._clock.tick(_FPS)
```

---

#### 3. Sprite Pattern (Pygame)
Game entities extend `pygame.sprite.Sprite` and are managed through **sprite groups** (`GroupSingle`, `Group`). The group handles drawing and updating all sprites with a single call, decoupling the game loop from individual entity logic.

```python
self._player_single_group.draw(surface=self._screen)
self._player_single_group.update()
```

---

#### 4. Template Method Pattern
`PlayerModel.update()` defines a fixed sequence of steps, each delegated to a private method. Subclasses or future entities can override individual steps without altering the overall update order.

```python
def update(self) -> None:
    keys = pygame.key.get_pressed()
    self._input(keys)
    self._apply_gravity()
    self._animate(keys)
    self._clamp_position()
```

---

#### 5. State Machine (Intro / In-Game)
`InterfaceGame` uses a simple boolean state (`_game_started`) to switch between the two game states. Each state has its own dedicated render method, making it straightforward to add new states (e.g., pause, game over) in the future.

---

#### 6. Centralized Asset Paths (Constants Module)
All file paths are defined once in `src/constants/paths.py` using `resource_path()`, which resolves them correctly both during development and inside a PyInstaller bundle. No path string is ever duplicated across the codebase.

```python
# src/constants/paths.py
GRAPHIC_PLAYER_WALK_1 = resource_path("src/assets/graphics/player_walk_1.png")
```

## Known Issues

None at the moment.