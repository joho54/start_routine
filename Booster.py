import time
import random

# List of reset sentences
reset_sentences = [
    "Starting again. I control the code.",
    "This is focus time. I am immersed.",
    "The system I create is clean and powerful.",
    "Coding is mine, and I will focus.",
]

# Select a random reset sentence
sentence = random.choice(reset_sentences)

# Guide message
print("\n🎯 Focus routine starts! Loosen your fingers and type the reset sentence.")
print("----------------------------------------------------")
print(f"👉 {sentence}")
# Prompt user to type the sentence
user_input = input("\nType the reset sentence exactly as shown above:\n")

# Check if the user input matches the sentence
while user_input != sentence:
    print("❌ Incorrect. Please try again.")
    user_input = input("\nType the reset sentence exactly as shown above:\n")

print("✅ Correct! Well done.")
print("----------------------------------------------------")
print(
    "\n⌨️ Adjust your keyboard home position, and slowly type the following sentence:\n"
)
print("    asdf jkl;  asdf jkl;  asdf jkl;")
print("    asdf jkl;  asdf jkl;  asdf jkl;\n")
# Pause for 10 seconds
print("⏳ Pausing for 10 seconds. Get ready...")
time.sleep(10)
print("\n" * 5)
# 5-second countdown
for i in range(5, 0, -1):
    print(f"{i}...", end=" ", flush=True)
    time.sleep(1)

print("\n🚀 Now entering focus mode!\n")
