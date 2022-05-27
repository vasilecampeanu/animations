from manim import *

# https://stackoverflow.com/questions/71133158/manim-set-z-index-with-value-tracker

class RatioHF(MovingCameraScene):
        def bar_mouvante(self, x_position, y_position, pourcentage_homme):
            rectangle_de_base = Rectangle(height = 1, width = 4, stroke_color = BLACK).move_to([x_position, y_position, 0]).set_fill(PINK, opacity = 0.8)
            remplissage_de_base = Rectangle(height = 1, width = 2, stroke_color = BLACK).move_to([x_position -1, y_position, 0]).set_fill(BLUE, opacity = 0.8)
    
            tracker = ValueTracker(0.5).set_z_index(1)
            pourcentage_de_base = DecimalNumber(0.5, color = BLACK).move_to(remplissage_de_base.get_critical_point(LEFT) + np.array([0.5, 0, 0])).set_z_index(1)
            pourcentage_de_base.add_updater(lambda m: m.set_value(tracker.get_value())).set_z_index(1)
    
            self.play(FadeIn(rectangle_de_base, remplissage_de_base, pourcentage_de_base))
    
            self.play(
                remplissage_de_base.animate.become(
                    Rectangle(
                        height = remplissage_de_base.height,
                        width = pourcentage_homme * 4,
                        stroke_color = BLACK
                    ).align_to(rectangle_de_base, LEFT + UP).set_fill(BLUE, opacity = 0.8)
                ),
                tracker.animate.set_value(pourcentage_homme)
            )
    
            self.wait()
    
        def construct(self):
            self.wait()
            self.bar_mouvante(0, 0, 0.8)
            self.wait()