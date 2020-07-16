from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
from datetime import datetime
from os import scandir
from random import choice
from hoverable import HoverBehavior

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def recover(self):
        self.manager.transition.direction = "left"
        self.manager.current = "forgot_password_screen"
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    def login(self, username, password):
        with open("users.json") as file:
            users = json.load(file)
        if username in users and users[username]['password'] == password: 
            self.manager.transition.direction = "left"
            self.manager.current = "login_success_screen"
        else:
            self.ids.wrong_login.text = "Wrong username or password"


class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open("users.json") as file:
            users = json.load(file)

        users[username] = {'username': username, 'password': password,
         'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")
         }

        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "sign_up_sucess_screen"
        
class SignUpScreenSuccess(Screen):
    def login_page(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def enlight(self, feeling):
        count = 0
        for feel in scandir(path="./quotes"):
            feel_name = feel.name.replace(".txt", "")
            if (feel_name.lower().strip() == feeling.lower().strip()):
                count += 1
                with open("./quotes/" + feel.name, encoding="utf8") as f:
                    lines = f.readlines()
                    self.ids.message.text = choice(lines)
        if count == 0:
            self.ids.message.text = "Try another feeling"

    class ImageButton(ButtonBehavior, HoverBehavior, Image):
        pass

class ForgotPasswordScreen(Screen):
    def recover_pw(self, username):
        with open("users.json") as file:
            users = json.load(file)
        if username in users:
            self.ids.forgot_pw.text = users[username]['password']
        else:
            self.ids.forgot_pw.text = "User not registered"

            
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()