import tkinter
import customtkinter
from pytube import YouTube


def beginDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()


        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download("C:/Users/USER\Desktop/Achike's Work/pylab")
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="Couldn't download", text_color="red")


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

# Download button
download = customtkinter.CTkButton(app, text="Download", command=beginDownload)
download.pack(padx=10, pady=10)

# app runner
app.mainloop()
