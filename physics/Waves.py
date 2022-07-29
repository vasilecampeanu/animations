from manim import *
from manim_physics import *

class LinearWaveExampleScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 * DEGREES, -45 * DEGREES)
        wave = LinearWave()
        self.add(wave)
        wave.start_wave()
        self.wait(5)
        wave.stop_wave()
        return super().construct()

class RadialWaveExampleScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 * DEGREES, -45 * DEGREES)
        wave = RadialWave(
            LEFT * 2 + DOWN * 5,
            RIGHT * 2 + DOWN * 5,
            checkerboard_colors = [BLUE_D],
            stroke_width = 0,
        )
        self.add(wave)
        wave.start_wave()
        self.wait(5)
        wave.stop_wave()
        return super().construct()
        