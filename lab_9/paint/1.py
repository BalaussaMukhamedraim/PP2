import pygame

pygame.init()

# Размеры окна
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

# Цвета
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

current_color = colorRED

# Настройки
clock = pygame.time.Clock()
THICKNESS = 5
tool = "rectangle"  # по умолчанию рисуем прямоугольник

# Координаты
LMBpressed = False
prevX, prevY = 0, 0
currX, currY = 0, 0

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Мышь нажата
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            print("LMD pressed!")
            prevX = event.pos[0]
            prevY = event.pos[1]

        # Мышь двигается
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed and tool == "eraser":
                pygame.draw.circle(base_layer, colorBLACK, event.pos, THICKNESS)

            elif LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                screen.blit(base_layer, (0, 0))  # очистить временный экран

                if tool == "rectangle":
                    pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif tool == "circle":
                    center = ((prevX + currX) // 2, (prevY + currY) // 2)
                    radius = max(abs(currX - prevX), abs(currY - prevY)) // 2
                    pygame.draw.circle(screen, current_color, center, radius, THICKNESS)
                elif tool == "square":
                    side = min(abs(currX - prevX), abs(currY - prevY))
                    rect = pygame.Rect(prevX, prevY, side, side)
                    pygame.draw.rect(screen, current_color, rect, THICKNESS)  # Рисуем квадрат
                elif tool == "right_triangle":
                    points = [(prevX, prevY), (prevX, currY), (currX, currY)]
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)  # Рисуем прямоугольный треугольник
                elif tool == "equilateral_triangle":
                    side = abs(currX - prevX)
                    height = int((3**0.5 / 2) * side)
                    points = [
                        (prevX, prevY),
                        (prevX + side, prevY),
                        (prevX + side // 2, prevY - height)
                    ]
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)  # Рисуем равносторонний треугольник
                elif tool == "rhombus":
                    dx = abs(currX - prevX) // 2
                    dy = abs(currY - prevY) // 2
                    cx = (prevX + currX) // 2
                    cy = (prevY + currY) // 2
                    points = [
                        (cx, cy - dy),
                        (cx + dx, cy),
                        (cx, cy + dy),
                        (cx - dx, cy)
                    ]
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)  # Рисуем ромб

        # Мышь отпущена
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]

            if tool == "rectangle":
                pygame.draw.rect(base_layer, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif tool == "circle":
                center = ((prevX + currX) // 2, (prevY + currY) // 2)
                radius = max(abs(currX - prevX), abs(currY - prevY)) // 2
                pygame.draw.circle(base_layer, current_color, center, radius, THICKNESS)
            elif tool == "square":
                side = min(abs(currX - prevX), abs(currY - prevY))
                rect = pygame.Rect(prevX, prevY, side, side)
                pygame.draw.rect(base_layer, current_color, rect, THICKNESS)  # Рисуем квадрат
            elif tool == "right_triangle":
                points = [(prevX, prevY), (prevX, currY), (currX, currY)]
                pygame.draw.polygon(base_layer, current_color, points, THICKNESS)  # Рисуем прямоугольный треугольник
            elif tool == "equilateral_triangle":
                side = abs(currX - prevX)
                height = int((3**0.5 / 2) * side)
                points = [
                    (prevX, prevY),
                    (prevX + side, prevY),
                    (prevX + side // 2, prevY - height)
                ]
                pygame.draw.polygon(base_layer, current_color, points, THICKNESS)  # Рисуем равносторонний треугольник
            elif tool == "rhombus":
                dx = abs(currX - prevX) // 2
                dy = abs(currY - prevY) // 2
                cx = (prevX + currX) // 2
                cy = (prevY + currY) // 2
                points = [
                    (cx, cy - dy),
                    (cx + dx, cy),
                    (cx, cy + dy),
                    (cx - dx, cy)
                ]
                pygame.draw.polygon(base_layer, current_color, points, THICKNESS)  # Рисуем ромб

        # Клавиши: смена цвета и инструментов
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = colorRED
            elif event.key == pygame.K_b:
                current_color = colorBLUE
            elif event.key == pygame.K_g:
                current_color = colorGREEN

            elif event.key == pygame.K_1:
                tool = "rectangle"
            elif event.key == pygame.K_2:
                tool = "circle"
            elif event.key == pygame.K_3:
                tool = "eraser"
            elif event.key == pygame.K_4:
                tool = "square"  # Выбор квадрата
            elif event.key == pygame.K_5:
                tool = "right_triangle"  # Выбор прямоугольного треугольника
            elif event.key == pygame.K_6:
                tool = "equilateral_triangle"  # Выбор равностороннего треугольника
            elif event.key == pygame.K_7:
                tool = "rhombus"  # Выбор ромба

            elif event.key == pygame.K_EQUALS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS and THICKNESS > 1:
                THICKNESS -= 1

    screen.blit(base_layer, (0, 0))
    pygame.display.flip()
    clock.tick(60)