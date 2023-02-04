import importlib

import View.ContentScreen.content_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.ContentScreen.content_screen)




class ContentScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.ContentScreenModel
        self.view = View.ContentScreen.content_screen.ContentScreenView(controller=self, model=self.model)

    def get_view(self) -> View.ContentScreen.content_screen:
        return self.view

    def get_contents(self, subject):
        return self.model.subjects[subject]
