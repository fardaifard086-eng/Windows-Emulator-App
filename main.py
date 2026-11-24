import datetime
import sys
import time

def show_menu():
    print("\n" + "="*35)
    print("       🪟 Windows-Emulator       ")
    print("="*35)
    print(" 1. ⏰ Date and Time")
    print(" 2. 🔵 Bluetooth Manager")
    print(" 3. 📶 Wi-Fi Manager")
    print(" 4. 🔄 Zapia (File Transfer)")
    print(" 5. ⚙️  Settings")
    print(" 0. ❌ Exit")
    print("="*35)

def show_time():
    now = datetime.datetime.now()
    print("\n--- Current Date & Time ---")
    print(">>>", now.strftime("%Y-%m-%d %H:%M:%S"))

def bluetooth_menu():
    print("\n--- 🔵 Bluetooth Manager ---")
    print("Status: Scanning for devices...")
    time.sleep(1)
    print("No devices found yet. (Feature under construction)")

def wifi_menu():
    print("\n--- 📶 Wi-Fi Manager ---")
    print("Network: Connected to Home-WiFi")
    print("IP Address: 192.168.1.102")
    print("Signal Strength: Excellent")

def zapia_menu():
    print("\n--- 🔄 Zapia (File Transfer) ---")
    print("This feature will allow you to transfer files.")
    print("Currently in development...")

def settings_menu():
    print("\n--- ⚙️ Settings ---")
    print("Theme: Dark Mode")
    print("Language: English")
    print("(More settings coming soon)")

def main():
    while True:
        show_menu()
        choice = input("\n👉 Enter your choice: ")
        
        if choice == '1':
            show_time()
        elif choice == '2':
            bluetooth_menu()
        elif choice == '3':
            wifi_menu()
        elif choice == '4':
            zapia_menu()
        elif choice == '5':
            settings_menu()
        elif choice == '0':
            print("\nGoodbye! Exiting program.")
            sys.exit()
        else:
            print("\n❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main()
