import kivy
import mysql.connector

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen



class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line















# class Touch(Widget):
#     def __init__(self, **kwargs):
#         super(Touch, self).__init__(**kwargs)
#
#         with self.canvas:
#             Color(0, 1, 0, .5, mode='rgba')
#             Line(points=(20,30,400,500,60,500))
#             Color(1, 0, 0, .5, mode='rgba')
#             self.rect = Rectangle(pos=(0,0), size=(50,50))
#
#     def on_touch_down(self, touch):
#         self.rect.pos = touch.pos
#         print("Mouse Down", touch)
#
#
#
#     def on_touch_move(self, touch):
#         self.rect.pos = touch.pos
#         print("Mouse Move", touch)







# class MyGrid(Widget):
#     name = ObjectProperty(None)
#     email = ObjectProperty(None)
#
#     def btn(self):
#         print("Name:", self.name.text, "email:", self.email.text)
#         self.name.text = ""
#         self.email.text = ""
#     pass



    # def __init__(self, **kwargs):
    #     super(MyGrid, self).__init__(**kwargs)
    #     self.cols = 1
    #
    #
    #     self.inside = GridLayout()
    #     self.inside.cols = 2
    #
    #     self.inside.add_widget(Label(text="First Name: "))
    #     self.name = TextInput(multiline=False)
    #     self.inside.add_widget(self.name)
    #
    #     self.inside.add_widget(Label(text="Last Name: "))
    #     self.lastName = TextInput(multiline=False)
    #     self.inside.add_widget(self.lastName)
    #
    #     self.inside.add_widget(Label(text="Email: "))
    #     self.email = TextInput(multiline=False)
    #     self.inside.add_widget(self.email)
    #
    #     self.add_widget(self.inside)
    #
    #     self.submit = Button(text="Submit", font_size=40)
    #     self.submit.bind(on_press=self.pressed)
    #     self.add_widget(self.submit)
    #
    # def pressed(self, instance):
    #     name = self.name.text
    #     last = self.lastName.text
    #     email = self.email.text
    #
    #     print("Name:", name, "Last Name:", last, "Email:", email)
    #     self.name.text = ""
    #     self.lastName = ""
    #     self.email = ""

kv = Builder.load_file("my.kv")
class My_App(App):
    def build(self):
        return kv



if __name__ == "__main__":
    My_App().run()