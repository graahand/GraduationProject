import os
import random
import time
import sys

# Step 1: Specify the directory paths for your text files
male_files_directory = '../maletxtfiles'
female_files_directory = '../femaletxtfiles'

# Create a list of your text files from the directories
male_text_files = [f for f in os.listdir(male_files_directory) if f.endswith(".txt")]
female_text_files = [f for f in os.listdir(female_files_directory) if f.endswith(".txt")]

# Function to print text with a typewriter effect
def print_with_typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  # Adjust the sleep duration for the desired typing speed

# Step 2: Prompt the user to enter their name
user_name = input("Enter your name: ")

# Step 3: Prompt the user to enter their gender
user_gender = input("Enter your gender (male/female): ")

# Ensure valid gender input
if user_gender.lower() not in ["male", "female"]:
    print("Invalid gender input. Please enter 'male' or 'female'.")
else:
    # Determine which list of text files to use based on the user's gender
    text_files = male_text_files if user_gender.lower() == "male" else female_text_files

    # Randomly select a text file from the chosen list
    selected_file = random.choice(text_files)

    # Select the correct directory based on the user's gender
    selected_directory = male_files_directory if user_gender.lower() == "male" else female_files_directory

    # Read the content of the selected text file
    with open(os.path.join(selected_directory, selected_file), 'r') as file:
        file_content = file.read()

    # Replace [NAME] with the user's name
    file_content = file_content.replace("[NAME]", user_name)

    # Display the modified content with the typewriter effect
    print(f"Hello, {user_name}! Here is the content based on your gender ({user_gender}):")
    print_with_typewriter_effect(file_content)
