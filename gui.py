import easygui as eg

yourname = eg.msgbox(f"hello {name}".center(85))
height = eg.integerbox("How tall are you?")

Buttons = ["Button 1", "Button 2", "Help"]
choice = eg.buttonbox()

Variable = eg.buttonbox("This is an example of buttons", choices=Buttons, image=["a.png", "b.png"])

#################################################################################################################

import easygui as eg
eg.msgbox("Welcome to the quiz", image="question mark.gif")
buttons = ["3.5","3.16","3.15"]
questionone = eg.buttonbox("what is the value of Pi?", choices=buttons, image="pi.gif")


# gui는 이벤트를 loop로 돌려야 한다.
