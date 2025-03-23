import pygame
from color_palette import *
import random
import time

pygame.init()

# Размеры экрана и ячейки
WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Игровая сетка
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (j * CELL, i * CELL, CELL, CELL), 1)

# Класс точки
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс змеи
class Snake:
    def __init__(self):
        self.body = [Point(5, 5)]
        self.dx = 1
        self.dy = 0
        self.alive = True

    def move(self):
        # Перемещаем сегменты тела
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Двигаем голову
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # Проверка на выход за границы
        if (self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or
            self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL):
            self.alive = False

        # Проверка на столкновение с собой
        for segment in self.body[1:]:
            if self.body[0].x == segment.x and self.body[0].y == segment.y:
                self.alive = False

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            return True
        return False

# Класс еды
class Food:
    def __init__(self, snake):
        self.snake = snake
        self.pos = Point(0, 0)
        self.generate_random_pos()

    def generate_random_pos(self):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            # Проверяем, не находится ли еда на змее
            overlap = False
            for segment in self.snake.body:
                if segment.x == x and segment.y == y:
                    overlap = True
                    break
            if not overlap:
                self.pos.x = x
                self.pos.y = y
                break

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

# Настройки игры
FPS = 5
clock = pygame.time.Clock()

snake = Snake()
food = Food(snake)

# Очки и уровень
score = 0
level = 1
foods_to_next_level = 3  # Количество ед для повышения уровня

# Шрифт
font = pygame.font.SysFont("Verdana", 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Управление
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

    # Если змейка жива — игра продолжается
    if snake.alive:
        screen.fill(colorBLACK)
        draw_grid()

        snake.move()
        if snake.check_collision(food):
            score += 1
            food.generate_random_pos()

            # Переход на следующий уровень
            if score % foods_to_next_level == 0:
                level += 1
                FPS += 2  # Увеличиваем скорость

        snake.draw()
        food.draw()

        # Отображаем очки и уровень
        score_text = font.render(f"Score: {score}", True, colorWHITE)
        level_text = font.render(f"Level: {level}", True, colorWHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

    else:
        # Если проиграли — красный экран и сообщение
        screen.fill(colorRED)
        game_over = font.render("Game Over!", True, colorBLACK)
        screen.blit(game_over, (WIDTH // 2 - 60, HEIGHT // 2))
        pygame.display.flip()
        time.sleep(2)
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()