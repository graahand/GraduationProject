import os
import random

# txt folders
male_files_directory = '../maletxtfiles'
female_files_directory = '../femaletxtfiles'

# txt list
male_text_files = [f for f in os.listdir(male_files_directory) if f.endswith(".txt")]
female_text_files = [f for f in os.listdir(female_files_directory) if f.endswith(".txt")]

# Function to generate and display a message
def generate_and_display_message(user_name, user_gender):
    if not user_name:
        print("Please enter your name.")
        return
    if user_gender.lower() not in ["male", "female"]:
        print("Invalid gender input. Please enter 'male' or 'female'.")
        return
    
    text_files = male_text_files if user_gender.lower() == "male" else female_text_files
    selected_file = random.choice(text_files)
    selected_directory = male_files_directory if user_gender.lower() == "male" else female_files_directory

    with open(os.path.join(selected_directory, selected_file), 'r') as file:
        file_content = file.read()

    file_content = file_content.replace("[NAME]", user_name)

    display_typewriter_effect(file_content)

# Function to display text with typewriter effect
def display_typewriter_effect(text, index=0):
    if index < len(text):
        print(text[:index+1], end='', flush=True)
        index += 1
        display_typewriter_effect(text, index)
    else:
        print()  # Print a newline after the typewriter effect

# Input from the user
user_name = input("Enter your name: ").capitalize()
user_gender = input("Enter your gender (male or female): ")

generate_and_display_message(user_name, user_gender)
