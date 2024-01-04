import pygame

class Tank:
	def __init__(self, screen):
		"""Задание характеристик объекта-танка"""
		# задание экрана для вывода объекта
		self.screen = screen
		# загрузка изображения объекта и задание его размеров
		self.image = pygame.image.load('tank.png')
		# задание иконки окна с помощью изображения объекта
		pygame.display.set_icon(self.image)
		# задание размеров изображения объекта-танка
		self.w, self.h = (70, 67)
		self.image = pygame.transform.scale(self.image,(self.w, self.h))
		# преобразование изображения объекта-танка
		self.image = self.image.convert_alpha()
		# задание начальной позиции отображения объекта-танка
		self.pos = (screen.get_width()/2, screen.get_height()/2)
		# задание начального угла поворота объекта
		self.angle = 0
		# задание скорости перемещения объекта по осям Х, У
		self.speed = 5
		# получение прямоугольника изображения объекта-танка
		self.screen_rect = screen.get_rect()
		
		# задание флагов перемещения объекта по осям Х и У
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		# задание флагов вращения объекта против/по часовой стрелке
		self.anti_clockwise = False
		self.clockwise = False
	
	
	def update(self):
		"""Обновление позиции объекта-танка"""
		# изменение позиции при перемещении вправо и достижения границы экрана
		if self.moving_right and self.rotated_image_rect.right < self.screen.get_size()[0]:
			self.rotated_image_rect.centerx += self.speed
			# обновление позиции объекта-танка
			self.pos = (self.rotated_image_rect.centerx, self.rotated_image_rect.centery)
		# изменение позиции при перемещении влево и достижения границы экрана
		elif self.moving_left and self.rotated_image_rect.left > 0:
			self.rotated_image_rect.centerx -= self.speed
			# обновление позиции объекта-танка
			self.pos = (self.rotated_image_rect.centerx, self.rotated_image_rect.centery)
		# изменение позиции при перемещении вверх и достижения границы экрана
		elif self.moving_up and self.rotated_image_rect.top > 2:
			self.rotated_image_rect.centery -= self.speed
			# обновление позиции объекта-танка
			self.pos = (self.rotated_image_rect.centerx, self.rotated_image_rect.centery)
		# изменение позиции при перемещении вниз и достижения границы экрана
		elif self.moving_down and self.rotated_image_rect.bottom < self.screen.get_size()[1]:
			self.rotated_image_rect.centery += self.speed
			# обновление позиции объекта-танка
			self.pos = (self.rotated_image_rect.centerx, self.rotated_image_rect.centery)
		# изменение позиции при перемещении против часовой стрелки
		elif self.anti_clockwise:
			self.angle += 1
		# изменение позиции при перемещении по часовой стрелке
		elif self.clockwise:
			self.angle -= 1
			 
	def blitRotate(self):
		"""Отрисовка объекта-танка при изменении его положения"""
		# смещение от точки вращения к центру
		self.image_rect = self.image.get_rect(topleft = (self.pos[0] - self.w/2, self.pos[1]-self.h/2))
		self.offset_center_to_pivot = pygame.math.Vector2(self.pos) - self.image_rect.center
		# повернутое смещение от точки вращения к центру
		self.rotated_offset = self.offset_center_to_pivot.rotate(-self.angle)
		# поворот изображения относительно его центра
		self.rotated_image_center = (self.pos[0] - self.rotated_offset.x, self.pos[1] - self.rotated_offset.y)
		# получение прямоугольника перевёрнутого изображения
		self.rotated_image = pygame.transform.rotate(self.image, self.angle)
		self.rotated_image_rect = self.rotated_image.get_rect(center = self.rotated_image_center)
		# отрисовка объекта-танка на фоне
		self.screen.blit(self.rotated_image, self.rotated_image_rect)
		# отрисовка прямоугольника объекта
		pygame.draw.rect(self.screen, (255, 0, 0), (*self.rotated_image_rect.topleft, *self.rotated_image.get_size()),2)
		
		
	

