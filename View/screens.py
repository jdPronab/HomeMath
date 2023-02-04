# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.content_screen import ContentScreenModel
from Controller.content_screen import ContentScreenController


screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },

    "content screen": {
        "model": ContentScreenModel,
        "controller": ContentScreenController,
    },
}
