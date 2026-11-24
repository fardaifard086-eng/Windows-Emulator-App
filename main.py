import datetime
def show_time():
    now = datetime.datetime.now()
    print("Hello! This is your Windows-Emulator app.")
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
if __name__ == "__main__":
    show_time()
