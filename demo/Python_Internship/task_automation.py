# Filename: task_automation.py

import os
import shutil
import re
import requests


def move_jpg_files():
    """Task 1: Move all .jpg files from source folder to destination folder"""
    source_folder = input("Enter source folder path: ")
    dest_folder = input("Enter destination folder path: ")

    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    moved_count = 0

    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return

    # Move all .jpg files
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(source_path, dest_path)
            print(f"Moved: {filename}")
            moved_count += 1

    print(f"\nTotal files moved: {moved_count}")


def extract_emails():
    """Task 2: Extract all email addresses from a text file"""
    input_file = input("Enter input text file name: ")
    output_file = input("Enter output file name to save emails: ")

    try:
        with open(input_file, 'r') as f:
            content = f.read()

        # Regular expression pattern to match email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)

        # Remove duplicates
        unique_emails = list(set(emails))

        # Save to output file
        with open(output_file, 'w') as f:
            for email in unique_emails:
                f.write(email + '\n')

        print(f"\nFound {len(unique_emails)} unique email(s):")
        for email in unique_emails:
            print(f"  - {email}")

        print(f"\nEmails saved to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def scrape_webpage_title():
    """Task 3: Scrape the title of a webpage and save it"""
    url = input("Enter webpage URL: ")
    output_file = input("Enter output file name to save title: ")

    try:
        # Send GET request to the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Extract title using regex
        title_pattern = r'<title>(.*?)</title>'
        match = re.search(title_pattern, response.text, re.IGNORECASE)

        if match:
            title = match.group(1).strip()
            print(f"\nWebpage Title: {title}")

            # Save to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"URL: {url}\n")
                f.write(f"Title: {title}\n")

            print(f"Title saved to '{output_file}'")
        else:
            print("No title found on the webpage.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main menu-driven program"""
    while True:
        print("\n" + "=" * 50)
        print("TASK AUTOMATION MENU")
        print("=" * 50)
        print("1. Move all .jpg files from a folder to another")
        print("2. Extract email addresses from a text file")
        print("3. Scrape webpage title and save it")
        print("4. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\n--- Task 1: Move JPG Files ---")
            move_jpg_files()
        elif choice == '2':
            print("\n--- Task 2: Extract Emails ---")
            extract_emails()
        elif choice == '3':
            print("\n--- Task 3: Scrape Webpage Title ---")
            scrape_webpage_title()
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
