from manim import *

class ManimBannerAnimation(Scene):
    def construct(self):
        banner = ManimBanner().scale(0.5)
        self.play(
            banner.expand(direction = "center")
        )
        self.wait()
        return super().construct()