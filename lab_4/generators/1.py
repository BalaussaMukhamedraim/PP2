# Create a generator that generates the squares of numbers up to some number N.

def generate_squares(N):
    for i in range(N):
        yield i * i  # Генерируем значение, а не возвращаем список

N = 10
for square in generate_squares(N):
    print(square)

# or

class SquareIterator:
    def __init__(self, N):
        self.N = N
        self.i = 0  # Начинаем с нуля

    def __iter__(self):
        return self  # Итератор должен возвращать сам себя

    def __next__(self):
        if self.i < self.N:
            result = self.i * self.i
            self.i += 1
            return result
        else:
            raise StopIteration  # Останавливаем итерацию

# Используем наш итератор
N = 10
for square in SquareIterator(N):
    print(square)