import tkinter
import customtkinter
import os
from pytube import YouTube


# System settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme("green")

def get_download_folder():
    if os.name == "nt":
        # Windows
        return os.path.join(os.environ["USERPROFILE"], "Downloads")
    elif os.name == "posix":
        # Linux or macOS
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        # Unsupported OS
        raise OSError("Unsupported operating system")

def beginDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=in_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="blue")
        finishLabel.configure(text="")
        download_folder = get_download_folder()
        file_path = os.path.join(download_folder, ytObject.title + ".mp4")
        if os.path.isfile(file_path):
            # Prompt the user to choose whether to overwrite or rename the file
            choice = customtkinter.CTkMessageBox.askquestion(
                "File already exists",
                "A file with this name already exists in your downloads folder. Do you want to overwrite it?",
                icon="warning"
            )
            if choice == "no":
                # Prompt the user to enter a new file name
                file_name = customtkinter.CTkSimpleDialog.askstring(
                    "File name",
                    "Please enter a new name for the file:"
                )
                if file_name:
                    file_path = os.path.join(download_folder, file_name + ".mp4")
                else:
                    # If the user didn't enter a new file name, stop the download
                    return
        video.download(file_path)
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Couldn't download", text_color="red")



def in_progress(stream, chunk, bytes_remaining):
    total_size= stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_done = bytes_downloaded/ total_size * 100
    per = str(int(percentage_done)) 
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    progressBar.set(float(percentage_done) / 100)
# System settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme("green")

# Our Application frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert youtube link")
title.pack(padx=10, pady=10)
# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress Bar

pPercentage =customtkinter.CTkLabel(app, text="0 %")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=beginDownload)
download.pack(padx=10, pady=10)

# app runner
app.mainloop()
