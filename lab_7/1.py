import pygame
import sys
from datetime import datetime

pygame.init()

# Размер окна
WINDOW_SIZE = 500
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Mickey Clock")

# Загружаем фоновые часы
clock_image = pygame.image.load("/Users/alia/Desktop/kbtu/PP2/lab_7/image/clock.png")
clock_image = pygame.transform.scale(clock_image, (WINDOW_SIZE, WINDOW_SIZE))

# Загружаем изображения рук (стрелок)
right_hand = pygame.image.load("/Users/alia/Desktop/kbtu/PP2/lab_7/image/right_hand.png")  # Минутная стрелка
left_hand = pygame.image.load("/Users/alia/Desktop/kbtu/PP2/lab_7/image/left_hand.png")  # Секундная стрелка

# Центр часов (точка вращения)
clock_center = (WINDOW_SIZE // 2, WINDOW_SIZE // 2)

# Функция для поворота изображения вокруг его центра
def blit_rotate_center(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, new_rect.topleft)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время
    now = datetime.now()
    minute = now.minute
    second = now.second

    # Угол поворота (6 градусов на каждую единицу)
    minute_angle = - (minute * 6)  # Минутная стрелка
    second_angle = - (second * 6)  # Секундная стрелка

    # Отображаем фон (неповорачиваемый)
    screen.fill((255, 255, 255))
    screen.blit(clock_image, (0, 0))

    # Вращаем и отображаем стрелки
    blit_rotate_center(screen, right_hand, clock_center, minute_angle)  # Минутная рука
    blit_rotate_center(screen, left_hand, clock_center, second_angle)  # Секундная рука

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()