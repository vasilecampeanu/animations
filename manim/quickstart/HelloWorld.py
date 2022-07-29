from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world!")
        self.play(Write(text))
        return super().construct()
