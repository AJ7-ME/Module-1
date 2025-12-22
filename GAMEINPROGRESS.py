import tkinter as tk
import random
import time
import math

# ================= CONFIG =================
GRID = 25
CELL = 26
FPS = 60
MOVE_TIME = 0.18
XP_PER_LEVEL = 10
WALL_MARGIN = CELL * 0.35
MAX_APPLES = 50
XP_SPEED = 0.05  # How fast the XP bar fills

DIRS = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}

# ================= GAME =================
class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.SW = self.root.winfo_screenwidth()
        self.SH = self.root.winfo_screenheight()

        self.canvas = tk.Canvas(
            self.root,
            width=GRID * CELL,
            height=GRID * CELL + 90,
            bg="#111",
            highlightthickness=0
        )
        self.canvas.place(
            x=(self.SW - GRID * CELL) // 2,
            y=(self.SH - (GRID * CELL + 90)) // 2
        )

        self.state = "menu"
        self.last_logic_time = time.time()
        self.apple_count = 5
        self.show_menu()
        self.loop()
        self.root.mainloop()

    # ================= MENU =================
    def show_menu(self):
        self.clear_keys()
        self.state = "menu"
        self.canvas.delete("all")
        cx = GRID * CELL // 2
        cy = GRID * CELL // 2
        self.canvas.create_text(cx, cy - 100, text="SNAKE",
                                fill="white", font=("Arial", 36, "bold"))
        self.canvas.create_text(cx, cy - 40, text="1 - Solo",
                                fill="white", font=("Arial", 22))
        self.canvas.create_text(cx, cy, text="2 - VS Bot",
                                fill="white", font=("Arial", 22))
        self.canvas.create_text(cx, cy + 40, text="3 - VS Player",
                                fill="white", font=("Arial", 22))
        self.canvas.create_text(cx, cy + 90,
                                text=f"Apples on screen: {self.apple_count} (← / →)",
                                fill="gray", font=("Arial", 14))
        self.root.bind("1", lambda e: self.start_game("solo"))
        self.root.bind("2", lambda e: self.start_game("bot"))
        self.root.bind("3", lambda e: self.start_game("pvp"))
        self.root.bind("<Left>", lambda e: self.adjust_apples(-1))
        self.root.bind("<Right>", lambda e: self.adjust_apples(1))

    def adjust_apples(self, d):
        self.apple_count = max(1, min(MAX_APPLES, self.apple_count + d))
        self.show_menu()

    # ================= START =================
    def start_game(self, mode):
        self.clear_keys()
        self.state = "game"
        self.mode = mode

        self.snake1 = [(12, 12), (11, 12), (10, 12)]
        self.dir1 = (1, 0)
        self.can_turn1 = True
        self.snake2 = [(12, 14), (13, 14), (14, 14)] if mode != "solo" else []
        self.dir2 = (-1, 0)
        self.can_turn2 = True

        self.progress = 1.0
        self.head1 = [self.snake1[0][0]*CELL, self.snake1[0][1]*CELL]
        self.start1 = self.head1[:]
        self.end1 = self.head1[:]
        if mode != "solo":
            self.head2 = [self.snake2[0][0]*CELL, self.snake2[0][1]*CELL]
            self.start2 = self.head2[:]
            self.end2 = self.head2[:]

        self.foods = [self.spawn_food() for _ in range(self.apple_count)]

        self.apples1 = self.apples2 = 0
        self.xp1 = self.xp2 = 0
        self.xp_display1 = 0.0
        self.xp_display2 = 0.0

        self.paused = False
        self.game_over = False
        self.winner_text = ""
        self.last_logic_time = time.time()

        self.bind_controls()

    # ================= INPUT =================
    def bind_controls(self):
        self.root.bind("<space>", lambda e: self.toggle_pause())
        self.root.bind("<Return>", lambda e: self.show_menu())
        self.root.bind("w", lambda e: self.turn(1, "Up"))
        self.root.bind("s", lambda e: self.turn(1, "Down"))
        self.root.bind("a", lambda e: self.turn(1, "Left"))
        self.root.bind("d", lambda e: self.turn(1, "Right"))
        if self.mode == "pvp":
            self.root.bind("<Up>", lambda e: self.turn(2, "Up"))
            self.root.bind("<Down>", lambda e: self.turn(2, "Down"))
            self.root.bind("<Left>", lambda e: self.turn(2, "Left"))
            self.root.bind("<Right>", lambda e: self.turn(2, "Right"))

    def clear_keys(self):
        self.root.unbind_all("<Key>")
        self.root.unbind_all("<Return>")

    def turn(self, p, d):
        dx, dy = DIRS[d]
        if p == 1 and self.can_turn1 and (-dx, -dy) != self.dir1:
            self.dir1 = (dx, dy)
            self.can_turn1 = False
        if p == 2 and self.can_turn2 and (-dx, -dy) != self.dir2:
            self.dir2 = (dx, dy)
            self.can_turn2 = False

    def toggle_pause(self):
        self.paused = not self.paused

    # ================= LOOP =================
    def loop(self):
        now = time.time()
        if self.state == "game":
            if not self.paused and not self.game_over:
                if now - self.last_logic_time >= MOVE_TIME:
                    self.last_logic_time = now
                    self.logic_step()
                self.interpolate()
            self.animate_xp()
            self.draw()
        self.root.after(int(1000/FPS), self.loop)

    # ================= LOGIC =================
def logic_step(self):
    self.move_snake(1)
    if self.mode == "bot":
        self.bot_move()
        self.move_snake(2)
    elif self.mode == "pvp":
        self.move_snake(2)
    self.check_collisions()
    self.progress = 0.0
    self.can_turn1 = True
    self.can_turn2 = True

def move_snake(self, p):
    snake = self.snake1 if p==1 else self.snake2
    direction = self.dir1 if p==1 else self.dir2
    hx, hy = snake[0]
    nx, ny = hx+direction[0], hy+direction[1]
    snake.insert(0, (nx, ny))

    if (nx, ny) in self.foods:
        self.foods.remove((nx, ny))
        self.foods.append(self.spawn_food())
        if p==1:
            self.apples1 += 1
            if self.apples1 >= XP_PER_LEVEL:
                self.apples1 = 0
                self.xp1 += 1
        else:
            self.apples2 += 1
            if self.apples2 >= XP_PER_LEVEL:
                self.apples2 = 0
                self.xp2 += 1
    else:
        snake.pop()

    start = self.start1 if p==1 else self.start2
    end = self.end1 if p==1 else self.end2
    start[:] = [hx*CELL, hy*CELL]
    end[:] = [nx*CELL, ny*CELL]

def bot_move(self):
    hx, hy = self.snake2[0]
    fx, fy = min(self.foods, key=lambda f: abs(f[0]-hx)+abs(f[1]-hy))
    best = self.dir2
    best_dist = 9999
    for dx, dy in DIRS.values():
        nx, ny = hx+dx, hy+dy
        if 0<=nx<GRID and 0<=ny<GRID:
            if (nx, ny) not in self.snake1 and (nx, ny) not in self.snake2:
                d = abs(nx-fx)+abs(ny-fy)
                if d<best_dist:
                    best_dist = d
                    best = (dx, dy)
    self.dir2 = best

def check_collisions(self):
    # ----- PLAYER 1 -----
    if not self.pixel_in_bounds(self.head1):
        self.game_over = True
        if self.mode != "solo":
            self.winner_text = "Player 2 Wins!"
        return

    if self.snake1[0] in self.snake1[1:]:
        self.game_over = True
        if self.mode != "solo":
            self.winner_text = "Player 2 Wins!"
        return

    # ----- PLAYER 2 (VS MODES) -----
    if self.mode != "solo":
        if not self.pixel_in_bounds(self.head2):
            self.game_over = True
            self.winner_text = "Player 1 Wins!"
            return

        if self.snake2[0] in self.snake2[1:]:
            self.game_over = True
            self.winner_text = "Player 1 Wins!"
            return

        # ----- HEAD-TO-HEAD (DRAW) -----
        if self.snake1[0] == self.snake2[0]:
            self.game_over = True
            self.winner_text = "Draw!"
            return

        # ----- HEAD INTO BODY (CORRECT LOGIC) -----
        if self.snake1[0] in self.snake2[1:]:
            self.game_over = True
            self.winner_text = "Player 2 Wins!"
            return

        if self.snake2[0] in self.snake1[1:]:
            self.game_over = True
            self.winner_text = "Player 1 Wins!"
            return

def pixel_in_bounds(self, head):
    x, y = head
    return (-WALL_MARGIN < x < GRID*CELL-CELL+WALL_MARGIN) and (-WALL_MARGIN < y < GRID*CELL-CELL+WALL_MARGIN)

    # ================= INTERPOLATION =================
    def interpolate(self):
        if self.progress<1:
            self.progress += 1/(FPS*MOVE_TIME)
            t = min(self.progress,1)
            self.head1[0] = self.start1[0] + (self.end1[0]-self.start1[0])*t
            self.head1[1] = self.start1[1] + (self.end1[1]-self.start1[1])*t
            if self.mode!="solo":
                self.head2[0] = self.start2[0] + (self.end2[0]-self.start2[0])*t
                self.head2[1] = self.start2[1] + (self.end2[1]-self.start2[1])*t

    # ================= XP ANIMATION =================
    def animate_xp(self):
        if self.xp_display1 < self.apples1:
            self.xp_display1 = min(self.apples1, self.xp_display1 + XP_SPEED)
        if self.mode!="solo" and self.xp_display2 < self.apples2:
            self.xp_display2 = min(self.apples2, self.xp_display2 + XP_SPEED)

    # ================= DRAW =================
    def draw(self):
        self.canvas.delete("all")
        self.draw_snake(self.snake1,self.head1,self.dir1,"#00cc66")
        if self.mode!="solo":
            self.draw_snake(self.snake2,self.head2,self.dir2,"#0066cc")
        for fx, fy in self.foods:
            self.draw_apple(fx*CELL, fy*CELL)
        self.draw_xp()
        if self.paused:
            self.canvas.create_text(GRID*CELL//2, GRID*CELL//2,text="PAUSED", fill="white", font=("Arial",36))
        if self.game_over:
            msg = "GAME OVER"
            if self.mode!="solo":
                msg = self.winner_text or "GAME OVER"
            self.canvas.create_text(GRID*CELL//2, GRID*CELL//2,text=msg+"\nENTER - Menu",
                                    fill="white", font=("Arial",28), justify="center")

    def draw_snake(self, snake, head, direction, color):
        pts = [head[0]+CELL//2, head[1]+CELL//2]
        for x,y in snake[1:]:
            pts += [x*CELL+CELL//2, y*CELL+CELL//2]
        self.canvas.create_line(*pts, width=CELL-6, capstyle=tk.ROUND, joinstyle=tk.ROUND, fill=color)
        hx, hy = head
        self.canvas.create_oval(hx+4, hy+4, hx+CELL-4, hy+CELL-4, fill=color, outline="")
        ox, oy = direction
        ex = hx+CELL//2 + ox*4
        ey = hy+CELL//2 + oy*4
        self.canvas.create_oval(ex-6,ey-6,ex-2,ey-2,fill="black")
        self.canvas.create_oval(ex+2,ey-6,ex+6,ey-2,fill="black")

    def draw_xp(self):
        y = GRID*CELL + 30
        w = (GRID*CELL//2)-60
        self.canvas.create_rectangle(20,y,20+w,y+12, outline="#555")
        self.canvas.create_rectangle(20,y, 20 + (self.xp_display1/XP_PER_LEVEL)*w,y+12, fill="#33ff33", outline="")
        self.canvas.create_text(20, y-8, text=f"P1 XP: {self.xp1}", fill="white", anchor="w")
        if self.mode!="solo":
            x2 = GRID*CELL - 20 - w
            self.canvas.create_rectangle(x2,y,x2+w,y+12,outline="#555")
            self.canvas.create_rectangle(x2,y,x2 + (self.xp_display2/XP_PER_LEVEL)*w, y+12, fill="#33ff33", outline="")
            self.canvas.create_text(x2+w,y-8,text=f"P2 XP: {self.xp2}", fill="white", anchor="e")

    def draw_apple(self, x, y):
        cx, cy = x+CELL//2, y+CELL//2
        r = CELL//2-3
        self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="#e60000", outline="")
        self.canvas.create_oval(cx-r+4, cy-r+4, cx+r-4, cy+r-4, fill="#ff3333", outline="")
        self.canvas.create_line(cx, cy-r, cx, cy-r-6, fill="#5a3a1a", width=3)
        self.canvas.create_oval(cx+2, cy-r-8, cx+10, cy-r-2, fill="#2ecc71", outline="")
        self.canvas.create_oval(cx-5, cy-6, cx-2, cy-3, fill="white", outline="")

    def spawn_food(self):
        while True:
            p = (random.randint(0, GRID-1), random.randint(0, GRID-1))
            if p not in self.snake1 and p not in self.snake2:
                return p

SnakeGame()
