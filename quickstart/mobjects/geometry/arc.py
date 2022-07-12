from manim import *

class ArcExample(Scene):
    def construct(self):
        arc = Arc(angle = PI).scale(2)
        self.add(arc)
        return super().construct()

class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius = 2, color = RED)
        
        dot_01 = Dot(color = YELLOW).move_to([2, 0, 0])
        dot_02 = Dot(color = YELLOW).move_to([0, 2, 0])

        dot_01_text = Text("(0, 2)").next_to(dot_01, RIGHT).set_color(BLUE).scale(0.5)
        dot_02_text = Text("(2, 0)").next_to(dot_02, UP).set_color(BLUE).scale(0.5)

        arc = ArcBetweenPoints(start = 2 * RIGHT, end = 2 * UP, color = YELLOW)

        self.add(circle, dot_01, dot_02, dot_01_text, dot_02_text)
        self.play(Create(arc))
        self.wait()

        return super().construct()