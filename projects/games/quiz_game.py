import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "high_scores.json")

def load_high_score() -> int:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data.get("high_score", 0)
    return 0

def save_high_score(score: int):
    current_high = load_high_score()
    if score > current_high:
        with open(DATA_FILE, "w") as f:
            json.dump({"high_score": score}, f)
        print(f"🎉 New High Score: {score}!")

def main():
    print("Welcome to my computer quiz!")
    
    playing = input("Do you want to play? (yes/no): ").lower().strip()
    if playing != "yes":
        print("Maybe next time!")
        return

    print("Okay! Let's play ;)")
    score = 0
    questions = [
        ("What does CPU stand for?", "central processing unit"),
        ("What does GPU stand for?", "graphics processing unit"),
        ("What does RAM stand for?", "random access memory"),
        ("What does PSU stand for?", "power supply unit")
    ]

    for question, correct_answer in questions:
        answer = input(f"{question} ").lower().strip()
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}")

    print(f"\nYou got {score} questions correct!")
    percentage = (score / len(questions)) * 100
    print(f"Your score: {percentage}%")
    
    save_high_score(score)
    print(f"Current High Score: {load_high_score()}")

if __name__ == "__main__":
    main()
