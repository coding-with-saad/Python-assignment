import tkinter as tk

# Settings
cell_size = 20  # Size of each grid cell
eraser_size = 50  # Size of the eraser

# Create the main window
root = tk.Tk()
root.title("Canvas Eraser")

# Create the canvas
canvas_width = 600
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="lightgray")
canvas.pack()

# Draw the initial grid of blue cells
cells = []
for row in range(0, canvas_height, cell_size):
    row_cells = []
    for col in range(0, canvas_width, cell_size):
        cell = canvas.create_rectangle(col, row, col + cell_size, row + cell_size, fill="blue", outline="lightgray")
        row_cells.append(cell)
    cells.append(row_cells)

# Eraser properties
eraser_rect = None  # Placeholder for the eraser rectangle
eraser_x, eraser_y = 0, 0  # Initial eraser position
is_dragging = False  # Flag to track if the eraser is being dragged

# Function to update the eraser and erase overlapping cells
def update_eraser(x, y):
    global eraser_rect
    eraser_x, eraser_y = x, y

    # If eraser rectangle exists, delete it
    if eraser_rect:
        canvas.delete(eraser_rect)

    # Draw the new eraser rectangle
    eraser_rect = canvas.create_rectangle(eraser_x, eraser_y,
                                          eraser_x + eraser_size,
                                          eraser_y + eraser_size,
                                          fill="red", outline="black")

    # Erase the cells that the eraser overlaps
    for row_cells in cells:
        for cell in row_cells:
            cell_coords = canvas.coords(cell)
            cell_x1, cell_y1, cell_x2, cell_y2 = cell_coords

            if (eraser_x < cell_x2 and eraser_x + eraser_size > cell_x1 and
                    eraser_y < cell_y2 and eraser_y + eraser_size > cell_y1):
                # Change cell color to white
                canvas.itemconfig(cell, fill="white")

# Mouse event handlers for eraser dragging
def on_mouse_down(event):
    global is_dragging
    is_dragging = True
    update_eraser(event.x - eraser_size / 2, event.y - eraser_size / 2)

def on_mouse_move(event):
    if is_dragging:
        update_eraser(event.x - eraser_size / 2, event.y - eraser_size / 2)

def on_mouse_up(event):
    global is_dragging
    is_dragging = False

# Bind the mouse events
canvas.bind("<ButtonPress-1>", on_mouse_down)
canvas.bind("<B1-Motion>", on_mouse_move)
canvas.bind("<ButtonRelease-1>", on_mouse_up)

# Start the main event loop
root.mainloop()
