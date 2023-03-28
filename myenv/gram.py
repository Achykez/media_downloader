import tkinter
import customtkinter
import os
import requests
import json


# Function to get download folder based on operating system
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


# Function to start downloading Instagram video
# Function to start downloading Instagram video
def beginDownload():
    finishLabel.configure(text="", text_color="black")
    try:
        instaLink = link.get()
        resp = requests.get(instaLink)
        shortcode = resp.url.split("/")[-2]
        instaApiUrl = "https://www.instagram.com/p/{shortcode}/?__a=1"
        instaApiResp = requests.get(instaApiUrl)
        instaData = json.loads(instaApiResp.text)
        videoUrl = instaData["graphql"]["shortcode_media"]["video_url"]
        resp = requests.get(videoUrl, stream=True)
        total_size = int(resp.headers.get('content-length', 0))
        block_size = 1024
        download_folder = get_download_folder()
        filePath = os.path.join(download_folder, f"{shortcode}.mp4")
        with open(filePath, 'wb') as f:
            for data in resp.iter_content(block_size):
                if data:
                    f.write(data)
                    bytes_downloaded = len(data)
                    percentage_done = bytes_downloaded / total_size * 100
                    per = str(int(percentage_done))
                    pPercentage.configure(text=per + "%")
                    pPercentage.update()
                    progressBar.set(float(percentage_done) / 100)
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Couldn't download", text_color="red")


# System settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme("green")

# Our Application frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Instagram downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert Instagram link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Bar
pPercentage = customtkinter.CTkLabel(app, text="0 %")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=beginDownload)
download.pack(padx=10, pady=10)

# app runner
app.mainloop()
