from kivy.properties import ObjectProperty
import sqlite3
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp


class ScreenTwo(BoxLayout):
    conn = sqlite3.connect('problems.db')
    c = conn.cursor()
    search_button = ObjectProperty()
    problem_search_input = ObjectProperty()
    problem_search_slider = ObjectProperty()
    """ TODO load problems from database"""

    def load_problem(self):
        pass

    def filter_problems_by_name(self):
        if self.problem_search_input.text == "":
            self.c.execute("SELECT * FROM problems")
        else:
            self.c.execute("SELECT * FROM problems WHERE NAME LIKE ? COLLATE NOCASE",
                           ('%' + self.problem_search_input.text + '%',))
        rows = self.c.fetchall()
        for row in rows:
            print(row)
        MDApp.get_running_app().filter_problem_list(rows)

    def filter_problems_by_grade(self):
        self.c.execute("SELECT * FROM problems WHERE GRADE LIKE ?", (str(self.problem_search_slider.value) + '%',))
        rows = self.c.fetchall()
        for row in rows:
            print(row)
        MDApp.get_running_app().filter_problem_list(rows)
