import tkinter as tk
from tkinter import messagebox

# Define the main characters and their traits
characters = {
    "Pi Patel": {
        "description": "You are like Pi Patel! A resourceful, spiritual, and determined person who never gives up, even in the face of impossible odds.",
        "traits": {"bravery": 5, "spirituality": 5, "resourcefulness": 4, "curiosity": 4, "compassion": 3}
    },
    "Richard Parker": {
        "description": "You are like Richard Parker! You rely on your instincts to survive. You have a strong presence and demand respect, but deep down, you are vulnerable.",
        "traits": {"bravery": 5, "survival": 5, "independence": 4, "loyalty": 2, "compassion": 1}
    },
    "Gita Patel": {
        "description": "You are like Gita Patel! A loving, nurturing soul who deeply cares for your family and the people you cherish.",
        "traits": {"compassion": 5, "nurturing": 5, "wisdom": 3, "courage": 2, "spirituality": 3}
    },
    "Santosh Patel": {
        "description": "You are like Santosh Patel! Practical and pragmatic, you believe in what you can see, and take responsibility seriously.",
        "traits": {"practicality": 5, "bravery": 3, "wisdom": 4, "spirituality": 1, "curiosity": 3}
    },
    "Francis Adirubasamy (Mamaji)": {
        "description": "You are like Mamaji! Wise and philosophical, you believe in passing down knowledge and supporting others in their journey.",
        "traits": {"wisdom": 5, "spirituality": 4, "compassion": 4, "patience": 3, "curiosity": 3}
    }
}

# Questions and answers
questions = [
    {
        "question": "How do you react in life-threatening situations?",
        "options": [
            {"text": "Stay calm and resourceful", "traits": {"bravery": 2, "resourcefulness": 2}},
            {"text": "Panic but then figure it out", "traits": {"bravery": 1, "compassion": 1}},
            {"text": "Fight for survival", "traits": {"bravery": 3, "survival": 2}},
            {"text": "Try to help others first", "traits": {"compassion": 2, "nurturing": 1}},
        ]
    },
    {
        "question": "How important is spirituality to you?",
        "options": [
            {"text": "Very important", "traits": {"spirituality": 3}},
            {"text": "Somewhat important", "traits": {"spirituality": 2}},
            {"text": "Not important", "traits": {"spirituality": 0}},
            {"text": "I'm more of a practical person", "traits": {"practicality": 3}},
        ]
    },
    {
        "question": "How do you approach learning new things?",
        "options": [
            {"text": "With curiosity and an open mind", "traits": {"curiosity": 3}},
            {"text": "By following a structured method", "traits": {"wisdom": 2}},
            {"text": "By trying hands-on experience", "traits": {"resourcefulness": 2}},
            {"text": "I prefer to learn from others", "traits": {"patience": 2, "wisdom": 1}},
        ]
    },
    {
        "question": "How do you handle tough decisions?",
        "options": [
            {"text": "Rely on instincts", "traits": {"independence": 2}},
            {"text": "Think through logically", "traits": {"practicality": 3}},
            {"text": "Follow my heart", "traits": {"compassion": 2}},
            {"text": "Seek advice from others", "traits": {"wisdom": 2}},
        ]
    }
]

# Function to calculate the result based on user choices
def get_character(trait_scores):
    highest_score = 0
    chosen_character = None
    for character, info in characters.items():
        match_score = sum([trait_scores.get(trait, 0) * value for trait, value in info['traits'].items()])
        if match_score > highest_score:
            highest_score = match_score
            chosen_character = character
    return chosen_character

# Class to manage the game GUI
class LifeOfPiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Which Life of Pi Character Are You?")
        
        self.welcome_screen()
        self.trait_scores = {"bravery": 0, "spirituality": 0, "resourcefulness": 0, "curiosity": 0, "compassion": 0, "survival": 0, "independence": 0, "nurturing": 0, "practicality": 0, "wisdom": 0, "patience": 0}
        self.current_question = 0

    def welcome_screen(self):
        self.clear_window()
        welcome_label = tk.Label(self.root, text="Welcome to the 'Which Life of Pi Character Are You?' game!", font=("Arial", 18), pady=20)
        welcome_label.pack()

        start_button = tk.Button(self.root, text="Start", font=("Arial", 14), command=self.start_game)
        start_button.pack(pady=20)

    def start_game(self):
        self.current_question = 0
        self.trait_scores = {trait: 0 for trait in self.trait_scores}
        self.ask_question()

    def ask_question(self):
        self.clear_window()

        # Show the current question
        q = questions[self.current_question]
        question_label = tk.Label(self.root, text=q["question"], font=("Arial", 16), pady=20)
        question_label.pack()

        # Create buttons for each option
        for option in q["options"]:
            option_button = tk.Button(self.root, text=option["text"], font=("Arial", 14),
                                      command=lambda traits=option["traits"]: self.answer_question(traits))
            option_button.pack(pady=10)

    def answer_question(self, traits):
        for trait, value in traits.items():
            self.trait_scores[trait] += value
        
        self.current_question += 1
        if self.current_question < len(questions):
            self.ask_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_window()
        character = get_character(self.trait_scores)
        
        if character:
            result_label = tk.Label(self.root, text=f"You are most like {character}!", font=("Arial", 18), pady=20)
            result_label.pack()

            description_label = tk.Label(self.root, text=characters[character]["description"], font=("Arial", 14), wraplength=500)
            description_label.pack(pady=20)

            restart_button = tk.Button(self.root, text="Play Again", font=("Arial", 14), command=self.welcome_screen)
            restart_button.pack(pady=20)
        else:
            messagebox.showerror("Error", "We couldn't determine your character. Try again!")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = LifeOfPiGame(root)
    root.geometry("600x400")
    root.mainloop()

