import pywhatkit
import pyautogui
import time

# Define the dictionary
contact_dict = {
    "shama": "+91 7985799968",
    "kulsoom": "+91 8881727388",
    "khala": "+91 8382811207",
    "nani": "+91 7800887732",
    "sadiq": "+91 8423362828",
    "yunus": "+91 8004357524"
}


# Function to send WhatsApp message
def send_whatsapp_message(name, message):
    if name in contact_dict:
        number = contact_dict[name]

        # Use pywhatkit to send the message
        pywhatkit.sendwhatmsg_instantly(number, message)

        time.sleep(5)

        # Close the WhatsApp tab using pyautogui (you may need to adjust the coordinates)
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.press("enter")
    else:
        print(f"Contact {name} not found in the dictionary.")

