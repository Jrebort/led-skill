from mycroft import MycroftSkill, intent_file_handler


class Led(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('led.intent')
    def handle_led(self, message):
        self.speak_dialog('led')


def create_skill():
    return Led()

