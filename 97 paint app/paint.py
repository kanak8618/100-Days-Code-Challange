import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Paint App")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.color = "black"
        self.brush_size = 5
        self.setup_ui()

        self.image = Image.new("RGB", (800, 500), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.undo_stack = []

    def setup_ui(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        color_button = tk.Button(top_frame, text="Choose Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=10)
        clear_button = tk.Button(top_frame, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=10)
        save_button = tk.Button(top_frame, text="Save", command=self.save_image)
        save_button.pack(side=tk.LEFT, padx=10)
        eraser_button = tk.Button(top_frame, text="Eraser", command=self.use_eraser)
        eraser_button.pack(side=tk.LEFT, padx=10)
        brush_shape_menu = tk.Menubutton(top_frame, text="Brush Shape", relief=tk.RAISED)
        brush_shape_menu.menu = tk.Menu(brush_shape_menu, tearoff=0)
        brush_shape_menu["menu"] = brush_shape_menu.menu
        self.brush_shape = tk.StringVar()
        self.brush_shape.set("Round")
        brush_shape_menu.menu.add_radiobutton(label="Round", variable=self.brush_shape, value="Round")
        brush_shape_menu.menu.add_radiobutton(label="Square", variable=self.brush_shape, value="Square")
        brush_shape_menu.pack(side=tk.LEFT, padx=10)
        undo_button = tk.Button(top_frame, text="Undo", command=self.undo)
        undo_button.pack(side=tk.LEFT, padx=10)

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (800, 500), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.undo_stack = []

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.image.save(file_path)

    def use_eraser(self):
        self.color = "white"

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        if self.brush_shape.get() == "Round":
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
            self.draw.ellipse([x1, y1, x2, y2], fill=self.color)
        elif self.brush_shape.get() == "Square":
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline=self.color)
            self.draw.rectangle([x1, y1, x2, y2], fill=self.color)
        self.undo_stack.append(self.image.copy())

    def undo(self):
        if self.undo_stack:
            self.image = self.undo_stack.pop()
            self.draw = ImageDraw.Draw(self.image)
            self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()