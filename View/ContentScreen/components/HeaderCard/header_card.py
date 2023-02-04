from kivy.properties import StringProperty

from kivymd.uix.relativelayout import MDRelativeLayout


class HeaderCard(MDRelativeLayout):
    source = StringProperty()
    text = StringProperty()
