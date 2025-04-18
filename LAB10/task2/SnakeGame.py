import pygame, psycopg2, random, sys
from ConfigSnakeGame import host, user, password, db_name

pygame.init()
WIN_W, WIN_H = 800, 600
win = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Snek!")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

WHITE, GREEN, RED, BLACK = (255,255,255), (0,255,0), (255,0,0), (0,0,0)

def db_connect():
    return psycopg2.connect(host=host, user=user, password=password, dbname=db_name)

def load_or_register_player(name):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT id, score, level FROM users WHERE name=%s", (name,))
    result = cur.fetchone()
    if result:
        player_id, score, lvl = result
    else:
        cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id", (name,))
        player_id = cur.fetchone()[0]
        score, lvl = 0, 1
        conn.commit()
    conn.close()
    return player_id, score, lvl

def save_progress(pid, score, lvl):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("UPDATE users SET score=%s, level=%s WHERE id=%s", (score, lvl, pid))
    conn.commit()
    conn.close()

def spawn_food(snake):
    while True:
        food = [random.randint(0, (WIN_W - 10) // 10) * 10,
                random.randint(0, (WIN_H - 10) // 10) * 10]
        if food not in snake:
            return food

name = input("Введите имя: ")
player_id, score, level = load_or_register_player(name)
speed = 15 + (level - 1) * 3
next_lvl = 3

head = [100, 50]
body = [[100, 50], [90, 50], [80, 50]]
dir = "RIGHT"
next_dir = dir
food = spawn_food(body)
food_on = True
game_active = True

while game_active:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_active = False
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dir != "DOWN":
                next_dir = "UP"
            elif e.key == pygame.K_DOWN and dir != "UP":
                next_dir = "DOWN"
            elif e.key == pygame.K_LEFT and dir != "RIGHT":
                next_dir = "LEFT"
            elif e.key == pygame.K_RIGHT and dir != "LEFT":
                next_dir = "RIGHT"
            elif e.key == pygame.K_s:
                save_progress(player_id, score, level)
            elif e.key == pygame.K_p:
                paused = True
                msg = font.render("ПАУЗА — нажми P, чтобы продолжить", True, WHITE)
                win.blit(msg, (WIN_W//2 - 120, WIN_H//2))
                pygame.display.update()
                while paused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_p:
                            paused = False

    dir = next_dir
    if dir == "UP":
        head[1] -= 10
    elif dir == "DOWN":
        head[1] += 10
    elif dir == "LEFT":
        head[0] -= 10
    elif dir == "RIGHT":
        head[0] += 10

    body.insert(0, list(head))
    if head == food:
        food_on = False
        score += 1
    else:
        body.pop()

    if not food_on:
        food = spawn_food(body)
    food_on = True

    if head[0] < 0 or head[0] >= WIN_W or head[1] < 0 or head[1] >= WIN_H:
        break
    if head in body[1:]:
        break

    if score % next_lvl == 0 and score != 0:
        level = score // next_lvl + 1
        speed = 15 + (level - 1) * 3

    win.fill(BLACK)
    for seg in body:
        pygame.draw.rect(win, GREEN, pygame.Rect(seg[0], seg[1], 10, 10))
    pygame.draw.rect(win, RED, pygame.Rect(food[0], food[1], 10, 10))
    win.blit(font.render(f"Очки: {score}", True, WHITE), (10, 10))
    win.blit(font.render(f"Уровень: {level}", True, WHITE), (10, 40))
    pygame.display.update()
    clock.tick(speed)

save_progress(player_id, score, level)
win.fill(BLACK)
game_over = font.render("ИГРА ОКОНЧЕНА", True, WHITE)
win.blit(game_over, game_over.get_rect(center=(WIN_W//2, WIN_H//2)))
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()