import os

# Get the absolute path of the current directory and append the folder name
target_folder = os.path.join(os.getcwd(), "originallms")

# Create and open the text file
with open(".txt", "w") as f:
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            # Grab any image file, regardless of exact extension
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                f.write(os.path.join(root, file) + "\n")

print("List generated successfully! Check imageFileList.txt")