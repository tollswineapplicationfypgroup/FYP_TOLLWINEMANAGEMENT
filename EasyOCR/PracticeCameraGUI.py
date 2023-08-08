import cv2
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter
from customtkinter import CTkImage
from EasyOCR import perform_ocr


# Global variables to store PhotoImage and GUI windows
photo_image = None
captured_image = None
countdown_label = None
captured_photo_image = None
image_label = None
img_counter = 0
img_name = ""
cam = None  # Initialize cam to None


def capture_image():
    global countdown_label
    countdown_label.config(text="5", fg="white", bg="black")  # Set background to transparent
    camera_app.update()  # Update the GUI to show the countdown label
    camera_app.after(1000, update_countdown, 5)  # Start the countdown after 1 second


def update_countdown(remaining):
    global countdown_label
    if remaining > 0:
        countdown_label.config(text=str(remaining), fg="white", bg="black")  # Update the countdown label with the current number
        camera_app.update()
        camera_app.after(1000, update_countdown, remaining - 1)  # Schedule the next countdown update after 1 second
    else:
        countdown_label.config(text="", bg="black")  # Clear the countdown label text and set a black background
        capture_and_show_image()


def capture_and_show_image():
    global img_counter, captured_image, frame, image_label, img_name  # Declare variables as global
    img_name = "Captured_image_{}.png".format(img_counter)
    print("Photo Captured")
    img_counter += 1

    if captured_image is not None:
        captured_image.destroy()  # Close the captured image GUI if it's open

    # Create the customtkinter GUI window to display the captured image
    captured_image = customtkinter.CTkToplevel(camera_app)
    captured_image.geometry("1100x680+100+100")
    captured_image.title("Captured Image")

    # Make the captured_image window pop up above the camera_app window
    captured_image.grab_set()

    # Create a label to display the captured image
    image_label = customtkinter.CTkLabel(captured_image, text="")
    image_label.pack(padx=10, pady=20)

    # Frame to contain the buttons
    button_frame = customtkinter.CTkFrame(captured_image)
    button_frame.pack()

    # Buttons
    savephoto_button = customtkinter.CTkButton(button_frame, text="Save Image", cursor="hand2", command=save_image_and_retake)
    savephoto_button.pack(side=tk.LEFT, padx=20, pady=10)

    retakephoto_button = customtkinter.CTkButton(button_frame, text="Retake Photo", cursor="hand2", command=retake_photo)
    retakephoto_button.pack(side=tk.LEFT, padx=20, pady=10)

    # Convert the frame to RGB before displaying
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame_rgb)
    captured_photo_image = CTkImage(dark_image=image, size=(1050, 570))

    image_label.configure(image=captured_photo_image)  # Use the global image_label variable

    # Show the captured image GUI
    captured_image.deiconify()


def correct_color(image):
    lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # Apply histogram equalization to the L-channel
    l_channel_eq = cv2.equalizeHist(l_channel)

    # Merge the equalized L-channel back with the original a and b channels
    lab_image_eq = cv2.merge((l_channel_eq, a_channel, b_channel))

    # Convert the corrected LAB image back to RGB
    corrected_image = cv2.cvtColor(lab_image_eq, cv2.COLOR_LAB2RGB)
    return corrected_image


def unsharp_mask(image):
    blurred = cv2.GaussianBlur(image, (0, 0), 3)
    sharpened = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
    return sharpened


def retake_photo():
    global captured_image
    try:
        if captured_image is not None and captured_image.winfo_exists():
            captured_image.destroy()  # Close the captured image GUI if it exists and hasn't been destroyed
    except tk.TclError:
        # Ignore the error if the widget has already been destroyed
        pass


def save_image_and_retake():
    save_image()
    retake_photo()


def save_image():
    global captured_image, img_name
    frame_corrected = correct_color(frame)
    frame_sharpened = unsharp_mask(frame_corrected)
    cv2.imwrite(img_name, frame_sharpened)
    if captured_image is not None:
        captured_image.withdraw()  # Hide the captured image GUI
    camera_app.destroy()  # Close the camera GUI
    #app.destory() # Close the main GUI and exit the application
    perform_ocr(img_name)  # Pass the file path of the captured image to the OCR function


def update(label):
    global frame, photo_image
    ret, frame = cam.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo_image = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
        label.config(image=photo_image)
        label.image = photo_image
    camera_app.after(10, update, label)  # Pass the label parameter to the next update() call


def run_camera(label):
    global cam
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    update(label)


def main():
    global camera_app, label, countdown_label, captured_image, cam

    # Create the customtkinter GUI window for the camera
    camera_app = customtkinter.CTk()
    camera_app.geometry("1100x670+275+100")
    camera_app.title("Camera")

    # Create a label to display the camera feed
    label = tk.Label(camera_app)
    label.pack()

    # Start running the camera and pass the label parameter
    run_camera(label)  # Pass the label parameter to the run_camera() function

    # Create a 'Capture Image' button
    capture_button = customtkinter.CTkButton(camera_app, text="Capture Image", command=capture_image)
    capture_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER, y=20)  # y=15 for a slight padding below the bottom

    # Create a label to display the countdown
    countdown_label = tk.Label(camera_app, text="", font=("Helvetica", 30), fg="white")
    countdown_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Run the customtkinter GUI app for the camera
    camera_app.mainloop()

    # Release the camera
    cam.release()


if __name__ == "__main__":
    main()
