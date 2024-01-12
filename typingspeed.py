import time

def calculate_speed(text, start_time, end_time):
    words = text.split()
    total_words = len(words)
    time_taken = end_time - start_time
    minutes = time_taken / 60
    wpm = total_words / minutes
    
    return wpm

def main():
    passage = "Enter english words of your choice"
    print(passage)

    input("Press Enter to start typing.")
    start_time = time.time()

    user_input = input("Type the sentence and press Enter:\n")

    end_time = time.time()

    typing_speed = calculate_speed(user_input, start_time, end_time)
    print(f"Your typing speed is approximately {typing_speed:.2f} words per minute (WPM).")

if __name__ == "__main__":
    main()
