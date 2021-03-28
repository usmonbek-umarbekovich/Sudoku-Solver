import tkinter as tk
from . import style
from . import helpers
from time import sleep


class Sudoku:
  def __init__(self):
    self.window = tk.Tk()
    self.window.title("Sudoku Solver")
    self.window.protocol("WM_DELETE_WINDOW", self.kill_window)
    self.window.geometry("550x610")

    self.canvas = tk.Canvas(self.window, **style.canvas)
    self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

    frame = tk.Frame(self.window, bg="#f4f4f4")
    frame.pack(side=tk.TOP, expand=tk.YES)
    
    self.run_button = tk.Button(frame, text="Solve", command=self.solve, **style.run_button)
    self.run_button.grid(ipadx=15, row=0, column=0)
    self.run_button.bind("<Enter>", self.on_enter)
    self.run_button.bind("<Leave>", self.on_leave)
    # self.run_button.bind("<Return>", self.solve)

    label = tk.Label(frame, text="Runtime:", font=("Arial", 13))
    label.grid(padx=5, row=0, column=1)

    self.runtime = tk.Label(frame, text='n', font=("Arial", 13))
    self.runtime.grid(row=0, column=2)
    
    self.text_ids = [[0]*9 for _ in range(9)]
    
    self.canvas.update()
    width = self.canvas.winfo_width()
    height = self.canvas.winfo_height()
    step_x, step_y = width/9, height/9
    self.draw_lines(width, height, step_x, step_y)
    self.write_given_numbers(width, height, step_x, step_y)
    
    self.window.mainloop()

  def kill_window(self):
    self.window.destroy()
    
  def on_enter(self, event):
    self.run_button['background'] = '#333333'

  def on_leave(self, event):
    self.run_button['background'] = '#444444'
    
  def draw_lines(self, width, height, step_x, step_y):    
    # draw x lines
    y = step_y
    while y <= height:
      x = 0
      thic = (round(y/step_y) % 3 == 0) and 3 or 1
      while x <= width:
        self.canvas.create_line(x, y, x+3.5, y, width=thic)
        self.canvas.update()
        x += 3.5
      y += step_y
    
    # draw y lines
    x = step_x
    while x <= width:
      y = 0
      thic = (round(x/step_x) % 3 == 0) and 3 or 1
      while y <= height:
        self.canvas.create_line(x, y, x, y+3.5, width=thic)
        self.canvas.update()
        y += 3.5
      x += step_x
  
  def write_given_numbers(self, width, height, step_x, step_y):
    y = step_y/2
    while y < height:
      x = step_x/2
      while x < width:
        r, c = round((y-step_y/2)/step_y), round((x-step_x/2)/step_x)
        number = helpers.board[r][c] or ''
        self.text_ids[r][c] = self.canvas.create_text(x, y,
                                                      text=str(number),
                                                      anchor=tk.CENTER,
                                                      font="Arial 16")
        sleep(0.05)
        self.canvas.update()
        x += step_x
      y += step_y
    
  def solve(self):
    pos = helpers.find_empty(helpers.board)
    if not pos:
      return True
    else:
      row, col = pos
    
    for num in range(1, 10):
      if helpers.is_valid(helpers.board, num, pos):
        helpers.board[row][col] = num
        self.canvas.itemconfigure(self.text_ids[row][col], text=str(num))
        sleep(0.09)
        self.canvas.update()

        if self.solve():
          return True
        
        helpers.board[row][col] = 0
        self.canvas.itemconfigure(self.text_ids[row][col], text='')
        sleep(0.09)
        self.canvas.update()
    return False