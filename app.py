import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk
from keras._tf_keras.keras.models import load_model

MODEL_PATH = "tumor10EpCat.h5"
IMG_SIZE = 64
DISPLAY_SIZE = (300, 300)  # Width, height - UI display

class TumorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tumor Detection (YES/NO)")

        # proba zaladowania modelu
        try:
            self.model = load_model(MODEL_PATH)
        except Exception as e:
            messagebox.showerror("Model Error", f"Failed to load model:\n{e}")
            self.root.destroy()
            return

        self.loaded_image = None  # PIL image

        
        self.image_label = tk.Label(self.root, text="No image loaded", bg="gray")
        self.image_label.pack(padx=10, pady=10)

        
        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=5)

        
        self.classify_button = tk.Button(self.root, text="Classify", command=self.classify_image, state=tk.DISABLED)
        self.classify_button.pack(pady=5)

        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"))
        self.result_label.pack(pady=10)

    def load_image(self):
        
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Images", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff"), ("All files", "*.*")]
        )
        if not file_path:
            return  # Cancelled

        
        img_cv = cv2.imread(file_path)
        if img_cv is None:
            messagebox.showerror("Error", "Unable to load the image.")
            return

        # Convert BGR -> RGB
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        self.loaded_image = Image.fromarray(img_cv) 

        
        display_image = self.loaded_image.resize(DISPLAY_SIZE, Image.Resampling.LANCZOS)
        imgtk = ImageTk.PhotoImage(display_image)

        # update label
        self.image_label.configure(image=imgtk, text="")
        self.image_label.image = imgtk 

        #  classify button
        self.classify_button.config(state=tk.NORMAL)
        self.result_label.config(text="")

    def classify_image(self):
        
        if self.loaded_image is None:
            messagebox.showerror("No image", "Please load an image first.")
            return

        #resize to 64x64 for the model
        img_for_model = self.loaded_image.resize((IMG_SIZE, IMG_SIZE), Image.Resampling.LANCZOS)
        img_arr = np.array(img_for_model, dtype='float32') / 255.0
        input_arr = np.expand_dims(img_arr, axis=0)  # (1, 64, 64, 3)

        # prediction
        result = self.model.predict(input_arr)
        class_idx = np.argmax(result, axis=1)[0]

        if class_idx == 0:
            text = "Classification: NO (no tumor)"
            color = "green"
        else:
            text = "Classification: YES (tumor detected)"
            color = "red"

        self.result_label.config(text=text, fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = TumorApp(root)
    root.mainloop()
