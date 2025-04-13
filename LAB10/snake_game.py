import pygame
import random
import psycopg2
from config import load_config
from datetime import datetime

# === DB functions ===
def get_user(conn, username):
    with conn.cursor() as cur:
        cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        return cur.fetchone()

def create_user(conn, username):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
        return cur.fetchone()

def save_score(conn, user_id, score, level):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
            (user_id, score, level)
        )
        conn.commit()

# === Game Setup ===
pygame.init()
cell_size = 40
cell_number = 20
clock = pygame.time.Clock()
done = False
score = 0
level = 1
length = 2
fps = 5
snake_lst = []
direction = "UP"

# Colors
color_red = (255, 0, 0)
color_purple = (128, 0, 128)
color_orange = (255, 68, 51)
color_green = (0,255,0)
color_white = (255,255,255)

fruit_types = [(color_red, 1), (color_purple, 2), (color_orange, 3)]
fruit_spawn_time = 5000
last_fruit_time = pygame.time.get_ticks()

# Setup screen
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
font = pygame.font.Font("PP2/LAB10/font/Pixeltype.ttf", 50)

# Get player name
username = input("Введите ваше имя: ").strip()

# === Connect to database ===
config = load_config()
conn = psycopg2.connect(**config)
user = get_user(conn, username)
if user:
    user_id = user[0]
    print(f"🔁 Добро пожаловать, {username}!")
else:
    user_id = create_user(conn, username)[0]
    print(f"🆕 Новый игрок создан: {username}")

# Starting position
x_ch = (cell_number // 2) * cell_size
y_ch = (cell_number // 2) * cell_size
snake_lst = [[x_ch, y_ch]]
x_pos = y_pos = 0

def game_over(x, y):
    return x < 0 or x >= cell_number * cell_size or y < 0 or y >= cell_number * cell_size

def fruit():
    while True:
        x = random.randint(0, cell_number - 1) * cell_size
        y = random.randint(0, cell_number - 1) * cell_size
        if [x, y] not in snake_lst:
            return (x, y, random.choice(fruit_types) if level >= 3 else (color_red, 1))

x_f, y_f, fruit_info = fruit()

def draw_snake():
    for block in snake_lst:
        pygame.draw.rect(screen, color_green, (*block, cell_size, cell_size))

# === Main game loop ===
while not done:
    screen.fill(color_white)
    pygame.display.set_caption(f"Score: {score} Level: {level}")

    if score > 5:
        score = 0
        level += 1
        fps += 3

    current_time = pygame.time.get_ticks()
    if current_time - last_fruit_time >= fruit_spawn_time:
        x_f, y_f, fruit_info = fruit()
        last_fruit_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN": direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP": direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT": direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT": direction = "RIGHT"

    # Movement
    if direction == "UP": x_pos, y_pos = 0, -cell_size
    elif direction == "DOWN": x_pos, y_pos = 0, cell_size
    elif direction == "LEFT": x_pos, y_pos = -cell_size, 0
    elif direction == "RIGHT": x_pos, y_pos = cell_size, 0

    x_ch += x_pos
    y_ch += y_pos

    if game_over(x_ch, y_ch) or [x_ch, y_ch] in snake_lst:
        print("💾 Сохраняем результат...")
        save_score(conn, user_id, score, level)
        print("Результат сохранён! До встречи 😉")
        break

    snake_lst.append([x_ch, y_ch])
    if len(snake_lst) > length:
        del snake_lst[0]

    if x_ch == x_f and y_ch == y_f:
        score += fruit_info[1]
        length += fruit_info[1]
        x_f, y_f, fruit_info = fruit()
        last_fruit_time = current_time

    pygame.draw.rect(screen, fruit_info[0], (x_f, y_f, cell_size, cell_size))
    draw_snake()

    clock.tick(fps)
    pygame.display.flip()

conn.close()
pygame.quit()