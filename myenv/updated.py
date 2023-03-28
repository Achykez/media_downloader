# import tkinter
# import customtkinter
# import os
# from pytube import YouTube

# # System settings
# customtkinter.set_appearance_mode('System')
# customtkinter.set_default_color_theme("green")

# def get_download_folder():
#     if os.name == "nt":
#         # Windows
#         return os.path.join(os.environ["USERPROFILE"], "Downloads")
#     elif os.name == "posix":
#         # Linux or macOS
#         return os.path.join(os.path.expanduser("~"), "Downloads")
#     else:
#         # Unsupported OS
#         raise OSError("Unsupported operating system")

# def beginDownload():
#     try:
#         ytLink = link.get()
#         ytObject = YouTube(ytLink, on_progress_callback=in_progress)
#         # Get selected resolution from dropdown
#         selected_res = resolution_var.get()
#         # Filter streams by resolution
#         if selected_res == "Highest":
#             video = ytObject.streams.get_highest_resolution()
#         elif selected_res == "Lowest":
#             video = ytObject.streams.get_lowest_resolution()
#         else:
#             video = ytObject.streams.filter(resolution=selected_res).first()
#         title.configure(text=ytObject.title, text_color="blue")
#         finishLabel.configure(text="")
#         download_folder = get_download_folder()
#         video.download(download_folder)
#         finishLabel.configure(text="Downloaded", text_color="green")
#     except:
#         finishLabel.configure(text="Couldn't download", text_color="red")

# def in_progress(stream, chunk, bytes_remaining):
#     total_size= stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percentage_done = bytes_downloaded/ total_size * 100
#     per = str(int(percentage_done)) 
#     pPercentage.configure(text=per + "%")
#     pPercentage.update()

#     progressBar.set(float(percentage_done) / 100)

# # Our Application frame
# app = customtkinter.CTk()
# app.geometry("720x480")
# app.title("YouTube downloader")

# # Adding UI elements
# title = customtkinter.CTkLabel(app, text="Insert youtube link")
# title.pack(padx=10, pady=10)

# # Link input
# url_var = tkinter.StringVar()
# link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
# link.pack()

# # Resolution selection dropdown
# resolutions = ["Highest", "Lowest", "360p", "480p", "720p", "1080p"]
# resolution_var = tkinter.StringVar(app)
# resolution_var.set(resolutions[0])
# resolution_dropdown = customtkinter.CTkOptionMenu(app, resolution_var, *resolutions)
# resolution_dropdown.pack(pady=10)

# # Finished Downloading
# finishLabel = customtkinter.CTkLabel(app, text="")
# finishLabel.pack()

# # Progress Bar
# pPercentage =customtkinter.CTkLabel(app, text="0 %")
# pPercentage.pack()

# progressBar = customtkinter.CTkProgressBar(app, width=400)
# progressBar.set(0)
# progressBar.pack(padx=10, pady=10)

# # Download button
# download = customtkinter.CTkButton(app, text="Download", command=beginDownload)
# download.pack(padx=10, pady=10)

# # app runner
# app.mainloop()
