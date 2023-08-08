import tkinter as tk
import customtkinter
from PIL import Image
import subprocess
from tkinter import filedialog
from EasyOCR import perform_ocr  # Import the OCR function from ocr.py

app = None


def open_camera():
    global app
    subprocess.call(['python', "C:\\Users\\21011083\\PycharmProjects\\EasyOCR\\PracticeCameraGUI.py"], text=True, shell=True)
    app.destroy()


def open_file_explorer():
    # Open the file explorer and get the path of the selected image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

    if file_path:
        # Call the OCR function with the image path
        app.destroy()
        perform_ocr(file_path)
        # 'texts' contains the extracted text from the OCR.

def ocr_image_selection_gui():
    global app
    # OCR Image Selection GUI
    # System setting
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    # GUI frame for Image Selection
    app = customtkinter.CTk()
    app.geometry("800x500+450+200")
    app.title("OCR Image Selection")
    app.attributes("-topmost", True)

    # Adding UI elements
    company_logo = customtkinter.CTkImage(dark_image=Image.open("C:\\Users\\21011083\\PycharmProjects\\EasyOCR\\Image.png"), size=(420, 130))
    title = customtkinter.CTkLabel(app, image=company_logo, text="How do you want to select your photo?", compound="top")
    title.pack(padx=10, pady=60)

    # Configure the label to add bottom padding and increase font size
    title.configure(pady=40, font=("Helvetica", 16))

    # Frame to contain the buttons
    button_frame = customtkinter.CTkFrame(app)
    button_frame.pack()

    cam_label = tk.Label(app)

    # Camera button
    camera_button = customtkinter.CTkButton(button_frame, text="Open Camera", cursor="hand2", command=open_camera)
    camera_button.pack(side=tk.LEFT, padx=20, pady=10)

    # File Explorer button
    file_explorer_button = customtkinter.CTkButton(button_frame, text="Open File Explorer", cursor="hand2", command=open_file_explorer)
    file_explorer_button.pack(side=tk.LEFT, padx=20, pady=10)

    # Run application
    app.mainloop()
    return app

# Call the function to create and run the GUI
app = ocr_image_selection_gui()