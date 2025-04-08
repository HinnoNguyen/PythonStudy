import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Countdown: {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's up!")

def main():
    try:
        total_seconds = int(input("Enter countdown time in seconds: "))
        countdown(total_seconds)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
