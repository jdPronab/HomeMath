from View.base_screen import BaseScreenView
from View.MainScreen.components.SubjectCard.subject_card import SubjectCard
from View.MainScreen.components.SearchBar.search_bar import SearchBar
from View.ContentScreen.components.HeaderCard.header_card import HeaderCard


class MainScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
