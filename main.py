import os
import shutil

files_directory = "/home/clv/UCloud/Files"
save_directories = {
    "image" : "/home/clv/UCloud/Files/Images",
    "docs" : "/home/clv/UCloud/Files/Documents",
    "vids" : "/home/clv/UCloud/Files/Videos",
    "etc" : "/home/clv/UCloud/Files/Others"
}

files = os.listdir(files_directory)
for file in files:
    if os.path.isdir(file) or file.endswith(".py"):
        continue

    if file.endswith((".jpg", ".png", "jpeg", ".gif")):
        shutil.move(os.path.join(files_directory, file), save_directories["image"])
    elif file.endswith((".mkv", ".mp4", ".avi")):
        shutil.move(os.path.join(files_directory, file), save_directories["vids"])
    elif file.endswith((".doc", ".txt", ".pdf")):
        shutil.move(os.path.join(files_directory, file), save_directories["docs"])
    else:
        shutil.move(os.path.join(files_directory, file), save_directories["etc"])