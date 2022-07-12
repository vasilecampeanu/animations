from manim import *

# Constants
OBSIDIAN_MACOS_THEME_BLACK: str = "#1E1E1E"

# We can set it globaly like this:
config.background_color = RED

# Or using a dictionary style
config["background_color"] = RED

class SetBackgroundColor(Scene):
    def construct(self):
        self.camera.background_color = OBSIDIAN_MACOS_THEME_BLACK
        text = Text("Hello world!")
        self.add(text)
        return super().construct()