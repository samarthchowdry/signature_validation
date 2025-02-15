import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Label, Frame
from PIL import Image, ImageTk
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Function to open file dialog and load image
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        return img, file_path
    return None, None

# Function to preprocess image
def preprocess_image(img):
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)
    _, img_thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return img_thresh

# Function to compare images and calculate accuracy
def compare_images(img1, img2):
    img1 = preprocess_image(img1)
    img2 = preprocess_image(img2)
    img1 = cv2.resize(img1, (200, 100))
    img2 = cv2.resize(img2, (200, 100))
    ssim_index, _ = ssim(img1, img2, full=True)
    accuracy = ssim_index * 100
    return accuracy

# Function to handle the comparison
def compare_signatures():
    if img1_path is None or img2_path is None:
        messagebox.showwarning("Warning", "Both signature images must be selected")
        return
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
    accuracy = compare_images(img1, img2)
    display_result(accuracy)

# Function to display result in GUI
def display_result(accuracy):
    if accuracy >= 85:
        result_label.config(text=f"Signature Verified\nAccuracy: {accuracy:.2f}%", bg='green')
    else:
        result_label.config(text=f"Signature Not Verified\nAccuracy: {accuracy:.2f}%", bg='red')

# Function to display images in the GUI
def display_images(img_path, label):
    img = Image.open(img_path)
    img = img.resize((200, 100), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

# Function to load and display the first image
def load_and_display_img1():
    global img1_path
    img, img1_path = load_image()
    if img is not None:
        display_images(img1_path, img1_label)

# Function to load and display the second image
def load_and_display_img2():
    global img2_path
    img, img2_path = load_image()
    if img is not None:
        display_images(img2_path, img2_label)

# Initialize GUI
root = tk.Tk()
root.title("Signature Verification")
root.geometry("600x400")
root.configure(bg='lightblue')

frame = Frame(root, bg='lightblue')
frame.pack(pady=20)

img1_label = Label(frame, bg='lightblue')
img1_label.grid(row=0, column=0, padx=10, pady=10)
img2_label = Label(frame, bg='lightblue')
img2_label.grid(row=0, column=1, padx=10, pady=10)

load_img1_button = tk.Button(root, text="Load First Signature", command=load_and_display_img1, font=('Arial', 12, 'bold'), bg='white', fg='blue', padx=20, pady=10)
load_img1_button.pack(pady=10)

load_img2_button = tk.Button(root, text="Load Second Signature", command=load_and_display_img2, font=('Arial', 12, 'bold'), bg='white', fg='blue', padx=20, pady=10)
load_img2_button.pack(pady=10)

compare_button = tk.Button(root, text="Compare Signatures", command=compare_signatures, font=('Arial', 12, 'bold'), bg='white', fg='blue', padx=20, pady=10)
compare_button.pack(pady=20)

result_label = Label(root, text="", font=('Arial', 14), bg='lightblue')
result_label.pack(pady=20)

root.mainloop()
