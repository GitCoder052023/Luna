import pywhatkit
import pyautogui
import time

# Define the dictionary
contact_dict = {
    "Person 1": "+91 12355545414", # Replace with your own numbers and names
    "Person 2": "+91 87691573512", # Replace with your own numbers and names
    "Person 3": "+91 78203165008", # Replace with your own numbers and names
    "Person 4": "+91 72064089603", # Replace with your own numbers and names
    "Person 5": "+91 78013548920", # Replace with your own numbers and names
    "Person 6": "+91 796135870355" # Replace with your own numbers and names
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

