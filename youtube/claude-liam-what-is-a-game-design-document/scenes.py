"""scenes.py — Manim mechanism scenes for claude-liam-what-is-a-game-design-document.
Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
Ghost structure from frame 0; reveals land on cue; font_size >= 32 (titles 40).
No fills behind text; no lines through text; coords inside +-7.1 / +-4.0.
"""
from manim import *

BG = ManimColor("#F2F0E9"); INK = ManimColor("#3D3929"); ACC = ManimColor("#D97757")
SOFT = ManimColor("#6E6A57"); GHOST = ManimColor("#C9C4B4"); CARD = ManimColor("#FFFFFF")

def T(s, size=32, color=INK, weight=None):
    kw = {"font_size": size, "color": color}
    if weight: kw["weight"] = weight
    return Text(s, **kw)

def box(w, h, x, y, color=INK, dashed=False):
    r = Rectangle(width=w, height=h, color=color, stroke_width=3, fill_color=CARD, fill_opacity=1).move_to([x, y, 0])
    return DashedVMobject(r, num_dashes=40) if dashed else r


class B03_OneReason(Scene):
    """Idea -> document -> builder; the builder label becomes 'you, three weeks later'."""
    def construct(self):
        self.camera.background_color = BG
        title = T("A GDD exists for one reason", 40, weight="BOLD").to_edge(UP, buff=0.9)
        head = Circle(radius=0.9, color=INK, stroke_width=3).move_to([-4.6, 0.2, 0])
        doc = box(2.4, 3.0, 0, 0.2)
        builder = Circle(radius=0.9, color=INK, stroke_width=3).move_to([4.6, 0.2, 0])
        l_head = T("the idea", 32).next_to(head, DOWN, buff=0.35)
        l_doc = T("the document", 32).next_to(doc, DOWN, buff=0.35)
        l_builder = T("someone else", 32).next_to(builder, DOWN, buff=0.35)
        a1 = Arrow(head.get_right(), doc.get_left(), color=INK, stroke_width=3, buff=0.15)
        a2 = Arrow(doc.get_right(), builder.get_left(), color=INK, stroke_width=3, buff=0.15)
        lines = VGroup(*[Line([-0.8, 1.0 - i * 0.45, 0], [0.8, 1.0 - i * 0.45, 0], color=GHOST, stroke_width=3) for i in range(5)])
        self.add(title, head, doc, builder, l_head, l_doc, l_builder, lines)
        self.play(Create(a1), run_time=1.0)
        self.play(lines.animate.set_color(INK), run_time=1.2)
        self.play(Create(a2), run_time=1.0)
        self.wait(2.0)
        swap = T("you, in three weeks", 32, color=ACC).next_to(builder, DOWN, buff=0.35)
        self.play(Transform(l_builder, swap), run_time=0.8)
        ring = Circle(radius=1.1, color=ACC, stroke_width=4).move_to(builder.get_center())
        self.play(Create(ring), run_time=0.8)
        self.wait(3.0)


class B05_Threshold(Scene):
    """Decisions accumulate; past the line you forget them; the document holds them."""
    def construct(self):
        self.camera.background_color = BG
        title = T("Small enough to keep in your head?", 40, weight="BOLD").to_edge(UP, buff=0.9)
        base = Line([-5.5, -2.4, 0], [5.5, -2.4, 0], color=INK, stroke_width=3)
        limit = DashedLine([-5.5, 0.6, 0], [5.5, 0.6, 0], color=ACC, stroke_width=3)
        l_limit = T("what one head can hold", 32, color=ACC).next_to(limit, UP, buff=0.25).align_to(limit, LEFT)
        l_base = T("decisions the game depends on", 32, color=SOFT).next_to(base, DOWN, buff=0.3)
        self.add(title, base, limit, l_limit, l_base)
        dots = VGroup()
        for i in range(14):
            col = i % 7; row = i // 7
            d = Dot([-4.8 + col * 1.6, -1.8 + row * 1.0, 0], radius=0.22, color=INK)
            dots.add(d)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in dots[:7]], lag_ratio=0.15), run_time=1.6)
        self.wait(1.2)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in dots[7:]], lag_ratio=0.15), run_time=1.6)
        over = VGroup(*[Dot([-4.8 + c * 1.6, 1.3, 0], radius=0.22, color=ACC) for c in range(4)])
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in over], lag_ratio=0.2), run_time=1.2)
        l_over = T("forgotten by the third build", 32, color=ACC).next_to(over, RIGHT, buff=0.5)
        self.play(FadeIn(l_over), run_time=0.6)
        self.wait(3.0)


class B15_HouseBlueprint(Scene):
    """Same information, two formats: a prose description vs a drawn plan."""
    def construct(self):
        self.camera.background_color = BG
        title = T("Same information, wrong format", 40, weight="BOLD").to_edge(UP, buff=0.9)
        page = box(4.2, 4.6, -3.4, -0.3)
        plan = box(4.6, 4.6, 3.4, -0.3)
        l_page = T("a written description", 32, color=SOFT).next_to(page, DOWN, buff=0.3)
        l_plan = T("a blueprint", 32, color=SOFT).next_to(plan, DOWN, buff=0.3)
        prose = VGroup(*[Line([-5.1, 1.4 - i * 0.5, 0], [-1.7 - (0.6 if i % 3 == 2 else 0), 1.4 - i * 0.5, 0], color=GHOST, stroke_width=4) for i in range(8)])
        # floor plan: outer wall, two inner walls, a door gap, a window mark
        outer = Rectangle(width=3.6, height=3.4, color=GHOST, stroke_width=3).move_to([3.4, -0.3, 0])
        w1 = Line([3.4, 1.4, 0], [3.4, -0.6, 0], color=GHOST, stroke_width=3)
        w2 = Line([1.6, -0.6, 0], [3.4, -0.6, 0], color=GHOST, stroke_width=3)
        door = Arc(radius=0.7, start_angle=PI, angle=-PI / 2, color=GHOST, stroke_width=3).move_arc_center_to([5.2, -2.0, 0])
        win = Line([2.0, 1.4, 0], [2.9, 1.4, 0], color=GHOST, stroke_width=8)
        planlines = VGroup(outer, w1, w2, door, win)
        self.add(title, page, plan, l_page, l_plan, prose, planlines)
        self.play(prose.animate.set_color(INK), run_time=1.5)
        self.wait(1.5)
        self.play(planlines.animate.set_color(INK), run_time=1.5)
        ring = Circle(radius=2.6, color=ACC, stroke_width=4).move_to([3.4, -0.3, 0])
        self.play(Create(ring), run_time=0.9)
        verdict = T("the builder can use this one", 32, color=ACC).next_to(plan, UP, buff=0.25)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(3.0)


class B16_OnePage(Scene):
    """One page: a single focus illustration with callouts that all link back to it."""
    def construct(self):
        self.camera.background_color = BG
        title = T("One page, one focus, callouts for detail", 40, weight="BOLD").to_edge(UP, buff=0.9)
        page = box(11.0, 5.0, 0, -0.4)
        focus = box(3.6, 2.2, 0, -0.4, color=GHOST)
        l_focus = T("the focus", 32, color=SOFT).move_to([0, -0.4, 0])
        callouts = [box(2.4, 1.0, -3.9, 1.1, color=GHOST), box(2.4, 1.0, 3.9, 1.1, color=GHOST), box(2.4, 1.0, -3.9, -1.9, color=GHOST), box(2.4, 1.0, 3.9, -1.9, color=GHOST)]
        leaders = [Line([-2.7, 1.1, 0], [-1.8, 0.3, 0], color=GHOST, stroke_width=3), Line([2.7, 1.1, 0], [1.8, 0.3, 0], color=GHOST, stroke_width=3),
                   Line([-2.7, -1.9, 0], [-1.8, -1.1, 0], color=GHOST, stroke_width=3), Line([2.7, -1.9, 0], [1.8, -1.1, 0], color=GHOST, stroke_width=3)]
        self.add(title, page, focus, l_focus, *callouts, *leaders)
        self.play(focus.animate.set_color(INK), run_time=0.8)
        for c, l in zip(callouts, leaders):
            self.play(c.animate.set_color(INK), l.animate.set_color(INK), run_time=0.5)
            self.wait(0.6)
        ring = RoundedRectangle(width=4.2, height=2.8, corner_radius=0.2, color=ACC, stroke_width=4).move_to([0, -0.4, 0])
        self.play(Create(ring), run_time=0.9)
        cite = T("Stone Librande, One-Page Designs, GDC 2010", 32, color=SOFT).move_to([0, -3.15, 0])
        self.play(FadeIn(cite), run_time=0.5)
        self.wait(2.5)


class B21_LivingFrozen(Scene):
    """A living document grows in pre-production, then freezes at production; later changes are logged marks."""
    def construct(self):
        self.camera.background_color = BG
        title = T("Living, then frozen", 40, weight="BOLD").to_edge(UP, buff=0.9)
        axis = Line([-5.8, -2.2, 0], [5.8, -2.2, 0], color=INK, stroke_width=3)
        l_pre = T("pre-production", 32, color=SOFT).move_to([-3.2, -2.8, 0])
        l_prod = T("production", 32, color=SOFT).move_to([3.0, -2.8, 0])
        freeze = DashedLine([0.2, -2.2, 0], [0.2, 1.9, 0], color=ACC, stroke_width=4)
        l_freeze = T("freeze", 32, color=ACC).next_to(freeze, UP, buff=0.15)
        bars = VGroup(*[Rectangle(width=0.7, height=0.6 + i * 0.45, color=GHOST, stroke_width=3, fill_color=CARD, fill_opacity=1).move_to([-5.0 + i * 1.1, -2.2 + (0.6 + i * 0.45) / 2, 0]) for i in range(5)])
        marks = VGroup(*[Line([1.3 + i * 1.4, -2.2, 0], [1.3 + i * 1.4, -1.5, 0], color=GHOST, stroke_width=4) for i in range(4)])
        self.add(title, axis, l_pre, l_prod, freeze, l_freeze, bars, marks)
        self.play(LaggedStart(*[b.animate.set_color(INK) for b in bars], lag_ratio=0.25), run_time=1.8)
        self.wait(1.0)
        pin = Dot([0.2, -2.2, 0], radius=0.18, color=ACC)
        self.play(Create(pin), marks.animate.set_color(ACC), run_time=1.0)
        l_marks = T("small changes, each with a reason", 32).move_to([3.2, -0.9, 0])
        self.play(FadeIn(l_marks), run_time=0.6)
        self.wait(3.0)
