import time
import pyautogui

def main():
    try:
        while True:
            # Move cursor to a specific position (adjust coordinates as needed)
            pyautogui.moveTo(100, 100, duration=1)
            # Click at the current cursor position
            pyautogui.click()
            # Wait for 15 minutes
            time.sleep(15 * 60)
    except KeyboardInterrupt:
        print("Script stopped.")

if __name__ == "__main__":
    main()
