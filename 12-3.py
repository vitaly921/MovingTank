import pygame
import sys
import gf
from tank import Tank


def run_game():
	# инициализация pygame
	pygame.init()
	# задание размеров окна
	length, width = 1200, 800
	# получение объекта-экрана с установленными размерами
	screen = pygame.display.set_mode((length, width))
	# задание названия окна
	pygame.display.set_caption('Moving and rotating the tank')
	
	# получение объекта для управления временными показателями 
	clock = pygame.time.Clock()
	
	# получение изображения фона и задание его размера по размеру окна
	image_background = pygame.image.load('images/background.jpg')
	image_background = pygame.transform.scale(image_background,
		(length, width))

	# получение объекта-танка
	tank = Tank(screen)

	# основной цикл игры
	while True:
		# установка максимального количества кадров в секунду
		clock.tick(60)
		# обработка событий
		gf.check_events(tank)
		# обновление позиции танка       
		tank.update()
		# отрисовка фона на экране
		screen.blit(image_background, (0,0))
		# отрисовка танка на экране и обновление его положения
		tank.blitRotate()
		# обновление экрана 
		pygame.display.flip()

# запуск игры
run_game()
