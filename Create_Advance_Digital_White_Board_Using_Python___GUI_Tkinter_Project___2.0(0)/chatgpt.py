import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.images = []
        self.selected_image = None

        self.width_scale = tk.Scale(root, from_=10, to=300, orient=tk.HORIZONTAL, command=self.update_width)
        self.width_scale.set(100)
        self.width_scale.pack()

        self.height_scale = tk.Scale(root, from_=10, to=300, orient=tk.HORIZONTAL, command=self.update_height)
        self.height_scale.set(100)
        self.height_scale.pack()

        self.canvas.bind("<Button-1>", self.select_image)
        self.canvas.bind("<B1-Motion>", self.move_image)

    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            self.images.append(photo)
            image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.tag_bind(image_id, "<Button-1>", lambda event, image_id=image_id: self.select_image(event, image_id))

    def select_image(self, event, image_id=None):
        if image_id:
            self.selected_image = image_id
            self.canvas.tag_raise(self.selected_image)
            bbox = self.canvas.bbox(self.selected_image)
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            self.width_scale.set(width)
            self.height_scale.set(height)
            self.canvas.itemconfigure(self.selected_image, outline="red", width=2)
        else:
            self.selected_image = None
            self.canvas.itemconfigure("selected", outline="", width=0)

    def move_image(self, event):
        if self.selected_image:
            self.canvas.coords(self.selected_image, event.x, event.y)

    def update_width(self, value):
        if self.selected_image:
            bbox = self.canvas.bbox(self.selected_image)
            current_width = bbox[2] - bbox[0]
            scale_factor = float(value) / current_width
            self.canvas.scale(self.selected_image, bbox[0], bbox[1], scale_factor, 1)

    def update_height(self, value):
        if self.selected_image:
            bbox = self.canvas.bbox(self.selected_image)
            current_height = bbox[3] - bbox[1]
            scale_factor = float(value) / current_height
            self.canvas.scale(self.selected_image, bbox[0], bbox[1], 1, scale_factor)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditor(root)

    add_button = tk.Button(root, text="Add Image", command=app.add_image)
    add_button.pack()

    root.mainloop()
