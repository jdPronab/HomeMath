
from kivymd.uix.list import OneLineListItem


from View.base_screen import BaseScreenView
from View.ContentScreen.components.HeaderCard.header_card import HeaderCard

class ContentScreenView(BaseScreenView):

    def model_is_changed(self) -> None:
        """"""""

    #def __init__(self, **kwargs):
    #    super().__init__(**kwargs)

    def generate_content_list(self, subject):
        content_list = self.ids.content_list
        for content in self.controller.get_contents(subject):
            content_item = OneLineListItemi(text=content)
            content_list.add_widget(content_item)


