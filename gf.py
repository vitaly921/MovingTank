import pygame
import sys


def check_keydown_events(event, tank):
	"""Обработка нажатий клавиш"""
	# завершение игры при нажатии ESC
	if event.key == pygame.K_ESCAPE:
		sys.exit()
	# изменение значений флагов при нажатии клавиш изменения положения
	elif event.key == pygame.K_RIGHT:
		tank.moving_right = True
	elif event.key == pygame.K_LEFT:
		tank.moving_left = True
	elif event.key == pygame.K_UP:
		tank.moving_up = True
	elif event.key == pygame.K_DOWN:
		tank.moving_down = True
	elif event.key == pygame.K_a:
		tank.anti_clockwise = True
	elif event.key == pygame.K_d:
		tank.clockwise = True


def check_keyup_events(event, tank):
	"""Обработока отжатий клавиш"""
	# изменение значений флагов при отжатии клавиш изменения положения
	if event.key == pygame.K_RIGHT:
		tank.moving_right = False
	elif event.key == pygame.K_LEFT:
		tank.moving_left = False
	elif event.key == pygame.K_UP:
		tank.moving_up = False
	elif event.key == pygame.K_DOWN:
		tank.moving_down = False
	elif event.key == pygame.K_a:
		tank.anti_clockwise = False
	elif event.key == pygame.K_d:
		tank.clockwise = False


def check_events(tank):
	"""Обработка событий в игре"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# действия при нажатии клавиш
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, tank)
		# действия при отжатии клавиш
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, tank)
