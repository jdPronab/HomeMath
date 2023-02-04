from Model.base_model import BaseScreenModel


class ContentScreenModel(BaseScreenModel):
    subjects = {"Geomertry": {"Point", "Line",
                              "Triangle", "Rectangle",
                              "Other Shapes"},

                "Arithmatics": {"Additio", "Substractio",
                                "Multiplication", "Devision",
                                "Idices", "Real Number"},

                "Algebra": {"Polinomials", "Quadratic Equations",
                            "Leniar Algebra"},

                "Statistics": {"Median", "Mean",
                               "Mode"}
               }
    def __init__(self, **kw):
        super().__init__(**kw)



    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
