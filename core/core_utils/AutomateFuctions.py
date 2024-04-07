import pywhatkit as kit
import pyautogui as gui


class DesktopAssistant:
    def __init__(self):
        pass

    def press_key(self, key: str):
        gui.press(key)

    def type_text(self, text: str):
        gui.write(text)

    def screenshot(self, filename: str):
        gui.screenshot(filename)

    def search_on_google(self, query: str):
        kit.search(query)


    def close_current_window(self):
        gui.hotkey('ctrl', 'w')

    def minimize_current_window(self):
        gui.hotkey('win', 'down')

    def maximize_current_window(self):
        gui.hotkey('win', 'up')

