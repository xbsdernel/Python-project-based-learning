import pygame as pg
import numpy as np

pg.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60
CELL_SIZE = 22
TOWER_SIZE = 60
COST_TOWER = 50
ENEMY_SPAWN_DELAY = 1000

player_currency = 300
player_health = 10
current_wave = 0
enemy_group = pg.sprite.Group()
tower_group = pg.sprite.Group()
dragging_tower = None
enemy_spawn_multiplier = 1
killed_enemies = 0

clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")

map_image = pg.image.load('map.png').convert_alpha()
tower_image = pg.image.load('zxc.png').convert_alpha()
enemy_image = pg.image.load('allien 3.png').convert_alpha()
new_enemy_image = pg.image.load('allien 4.png').convert_alpha()
upgrade_button_image = pg.image.load('Upgrade_tower-removebg-preview.png').convert_alpha()
upgrade_button_image = pg.transform.scale(upgrade_button_image, (233, 107))

original_width, original_height = map_image.get_size()
scale_factor = min(SCREEN_WIDTH / original_width, SCREEN_HEIGHT / original_height)
new_width = int(original_width * scale_factor)
new_height = int(original_height * scale_factor)
map_image = pg.transform.scale(map_image, (new_width, new_height))

x_offset = (SCREEN_WIDTH - new_width) // 2
y_offset = (SCREEN_HEIGHT - new_height) // 2

grid = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
])

provided_path2 = [
    (20, 0), (20, 10.5), (25, 10.5), (26.5, 15), (26.5, 19.5),
    (18, 19.5), (18, 23), (18, 26), (23, 26), (23, 30),
    (23, 43), (17, 43), (17, 45), (17, 47)
]

scaled_path = [(int(y * CELL_SIZE), int(x * CELL_SIZE)) for x, y in provided_path2]

class Tower(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pg.transform.scale(image, (TOWER_SIZE, TOWER_SIZE))
        self.rect = self.image.get_rect(center=(x, y))
        self.range = 150
        self.damage = 10
        self.cooldown = 0

    def attack(self, enemies):
        if self.cooldown > 0:
            self.cooldown -= 1
            return
        for enemy in enemies:
            if pg.Vector2(enemy.rect.center).distance_to(self.rect.center) <= self.range:
                enemy.health -= self.damage
                self.cooldown = 30
                return

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pg.draw.circle(surface, (0, 255, 0), self.rect.center, self.range, 1)

class Enemy(pg.sprite.Sprite):
    def __init__(self, path, image, health, speed):
        super().__init__()
        self.image = pg.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.path = path
        self.current_point = 0
        self.speed = speed
        self.health = health
        self.rect.topleft = self.path[0]

    def update(self):
        global player_currency, killed_enemies
        if self.health <= 0:
            player_currency += 10
            killed_enemies += 1
            self.kill()
            return

        if self.current_point < len(self.path) - 1:
            target = self.path[self.current_point + 1]
            direction = pg.Vector2(target[0] - self.rect.x, target[1] - self.rect.y)
            if direction.length() > self.speed:
                direction = direction.normalize() * self.speed
            self.rect.x += direction.x
            self.rect.y += direction.y
            if abs(self.rect.x - target[0]) < self.speed and abs(self.rect.y - target[1]) < self.speed:
                self.current_point += 1
        else:
            global player_health
            player_health -= 1
            if player_health <= 0:
                pg.quit()
                exit()
            self.kill()

def draw_button():
    button_rect = pg.Rect(10, SCREEN_HEIGHT - 60, 150, 50)
    pg.draw.rect(screen, (0, 128, 0), button_rect)
    button_font = pg.font.Font(None, 36)
    button_text = button_font.render("Add Tower", True, (255, 255, 255))
    screen.blit(button_text, (button_rect.x + 15, button_rect.y + 10))
    return button_rect

def place_tower(x, y):
    global player_currency
    if player_currency >= COST_TOWER:
        tower = Tower(x, y, tower_image)
        tower_group.add(tower)
        player_currency -= COST_TOWER
    else:
        print("Not enough currency!")

def draw_upgrade_button():
    upgrade_button_rect = upgrade_button_image.get_rect(topleft=(170, SCREEN_HEIGHT - 100))
    screen.blit(upgrade_button_image, upgrade_button_rect)
    return upgrade_button_rect

def upgrade_towers():
    global player_currency
    if player_currency >= 500:
        for tower in tower_group:
            tower.damage += 5
        player_currency -= 500
    else:
        print("Not enough currency to upgrade!")

last_spawn_time = pg.time.get_ticks()

def spawn_enemy():
    global last_spawn_time
    now = pg.time.get_ticks()
    if now - last_spawn_time > ENEMY_SPAWN_DELAY:
        for _ in range(enemy_spawn_multiplier):
            enemy = Enemy(scaled_path, enemy_image, health=30, speed=2)
            enemy_group.add(enemy)
        last_spawn_time = now

while True:
    screen.fill((255, 255, 255))

    screen.blit(map_image, (x_offset, y_offset))

    button_rect = draw_button()
    upgrade_button_rect = draw_upgrade_button()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if button_rect.collidepoint(mouse_x, mouse_y):
                    if player_currency >= COST_TOWER:
                        dragging_tower = Tower(mouse_x, mouse_y, tower_image)
                    else:
                        print("Not enough currency!")
                elif dragging_tower:
                    place_tower(mouse_x, mouse_y)
                    dragging_tower = None
                elif upgrade_button_rect.collidepoint(mouse_x, mouse_y):
                    upgrade_towers()

        elif event.type == pg.MOUSEMOTION:
            if dragging_tower:
                dragging_tower.rect.center = event.pos

    if killed_enemies >= 10:
        killed_enemies = 0
        for enemy in enemy_group:
            enemy.health += 20
            enemy.speed += 0.5

    spawn_enemy()

    enemy_group.update()
    for tower in tower_group:
        tower.attack(enemy_group)

    tower_group.draw(screen)
    enemy_group.draw(screen)
    if dragging_tower:
        dragging_tower.draw(screen)

    button_font = pg.font.Font(None, 24)
    currency_text = button_font.render(f"Coins: {player_currency}", True, (0, 50, 0))
    health_text = button_font.render(f"Health: {player_health}", True, (255, 0, 0))
    killed_text = button_font.render(f"Killed: {killed_enemies}", True, (0, 0, 255))

    screen.blit(currency_text, (10, 10))
    screen.blit(health_text, (10, 40))
    screen.blit(killed_text, (10, 70))

    pg.display.flip()
    clock.tick(FPS)
