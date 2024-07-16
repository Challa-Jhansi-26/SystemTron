import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.center_x = 200
        self.center_y = 200
        self.radius = 150
        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                self.center_x + self.radius, self.center_y + self.radius)
        for i in range(12):
            angle = math.pi/6 * i
            x = self.center_x + self.radius * 0.85 * math.sin(angle)
            y = self.center_y - self.radius * 0.85 * math.cos(angle)
            self.canvas.create_text(x, y, text=str(i+1), font=('Arial', 16))

    def update_clock(self):
        self.canvas.delete("hands")
        now = time.localtime()
        self.draw_hand(now.tm_hour % 12 * 30 + now.tm_min / 2, self.radius * 0.5, 'black', 6)
        self.draw_hand(now.tm_min * 6, self.radius * 0.8, 'blue', 4)
        self.draw_hand(now.tm_sec * 6, self.radius * 0.9, 'red', 2)
        self.root.after(1000, self.update_clock)

    def draw_hand(self, angle, length, color, width):
        angle = math.radians(angle - 90)
        x = self.center_x + length * math.cos(angle)
        y = self.center_y + length * math.sin(angle)
        self.canvas.create_line(self.center_x, self.center_y, x, y, fill=color, width=width, tags="hands")

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
