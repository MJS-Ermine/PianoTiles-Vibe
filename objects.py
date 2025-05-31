import pygame
import random

SCREEN = WIDTH, HEIGHT = 288, 512
TILE_WIDTH = WIDTH // 4
TILE_HEIGHT = 130

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
BLUE2 = (2, 239, 239)
PURPLE = (191, 64, 191)

class Tile(pygame.sprite.Sprite):
	def __init__(self, x, y, win, tile_type: str = "normal"):
		super(Tile, self).__init__()

		self.win = win
		self.x, self.y = x, y
		self.tile_type = tile_type
		self.color = self.get_color()
		self.alive = True

		self.surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT), pygame.SRCALPHA)
		self.rect = self.surface.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.center = TILE_WIDTH//2, TILE_HEIGHT//2 + 15
		self.line_start = self.center[0], self.center[1]-18
		self.line_end = self.center[0], 20

	def get_color(self):
		if self.tile_type == "life":
			return (0, 200, 0)
		elif self.tile_type == "time":
			return (0, 128, 255)
		else:
			return BLACK

	def update(self, speed):
		self.rect.y += speed
		if self.rect.y >= HEIGHT:
			self.kill()

		if self.alive:
			pygame.draw.rect(self.surface, self.color, (0,0, TILE_WIDTH, TILE_HEIGHT))
			pygame.draw.rect(self.surface, PURPLE, (0,0, TILE_WIDTH, TILE_HEIGHT), 4)
			pygame.draw.rect(self.surface, BLUE2, (0,0, TILE_WIDTH, TILE_HEIGHT), 2)
			pygame.draw.line(self.surface, BLUE, self.line_start, self.line_end, 3)
			pygame.draw.circle(self.surface, BLUE, self.center, 15, 3)
			if self.tile_type == "life":
				pygame.draw.circle(self.surface, (255,0,0), self.center, 10)
			elif self.tile_type == "time":
				pygame.draw.circle(self.surface, (255,255,0), self.center, 10)
		else:
			pygame.draw.rect(self.surface, (0,0,0, 90), (0,0, TILE_WIDTH, TILE_HEIGHT))
		self.win.blit(self.surface, self.rect)

class Text(pygame.sprite.Sprite):
	def __init__(self, text, font, pos, win):
		super(Text, self).__init__()
		self.win = win

		self.x,self.y = pos
		self.initial = self.y
		self.image = font.render(text, True, (255, 255, 255))

	def update(self, speed):
		self.y += speed
		if self.y - self.initial >= 100:
			self.kill()

		self.win.blit(self.image, (self.x, self.y))

class Counter(pygame.sprite.Sprite):
	def __init__(self, win, font, start_count: int = 60) -> None:
		"""計時賽倒數計時器。

		Args:
			win: pygame 視窗物件
			font: pygame 字型物件
			start_count (int): 倒數秒數，預設 60 秒
		"""
		super().__init__()
		self.win = win
		self.font = font
		self.start_count = start_count
		self.count = start_count
		self.index = 1
		self.active = False

	def start(self) -> None:
		"""啟動計時器。"""
		self.active = True
		self.index = 1
		self.count = self.start_count

	def reset(self) -> None:
		"""重設計時器。"""
		self.count = self.start_count
		self.index = 1
		self.active = True

	def update(self) -> None:
		"""每幀呼叫，更新倒數。"""
		if self.active and self.count > 0:
			if self.index % 30 == 0:
				self.count -= 1
			self.index += 1

	def is_time_up(self) -> bool:
		"""判斷時間是否到。"""
		return self.count <= 0

	def draw(self) -> None:
		"""在畫面上顯示剩餘時間。"""
		if self.active and self.count >= 0:
			timer_img = self.font.render(f'Time: {self.count}', True, (255, 0, 0))
			self.win.blit(timer_img, (10, 10))

class Square(pygame.sprite.Sprite):
	def __init__(self, win):
		super(Square, self).__init__()

		self.win = win
		self.color = (255, 255, 255)
		self.speed = 3
		self.angle = 0

		self.side = random.randint(15, 40)
		x = random.randint(self.side, WIDTH-self.side)
		y = 0

		self.surface = pygame.Surface((self.side, self.side), pygame.SRCALPHA)
		self.rect = self.surface.get_rect(center=(x, y))

	def update(self):
		center = self.rect.center
		self.angle = (self.angle + self.speed) % 360
		image = pygame.transform.rotate(self.surface , self.angle)
		self.rect = image.get_rect()
		self.rect.center = center

		self.rect.y += 1.5

		if self.rect.top >= HEIGHT:
			self.kill()

		pygame.draw.rect(self.surface, self.color, (0,0, self.side, self.side), 4)
		pygame.draw.rect(self.surface, (30, 144, 255, 128), (2,2, self.side-4, self.side-4), 2)
		self.win.blit(image, self.rect)

class Button(pygame.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(Button, self).__init__()
		
		self.scale = scale
		self.image = pygame.transform.scale(img, self.scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def update_image(self, img):
		self.image = pygame.transform.scale(img, self.scale)

	def draw(self, win):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True

			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False

		win.blit(self.image, self.rect)
		return action