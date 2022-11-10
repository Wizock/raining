from __future__ import annotations

import random

import pygame

height, width = 1920, 1080
screen = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()
running = True

gravity = 0.1


class Rain:
    def __init__(self, screen):
        self.vel = 2 * random.uniform(0, 3.665)
        self.screen = screen
        self.rain_instances = [
            pygame.Rect(
                float(random.randint(0, height)),
                random.uniform(-1000, 1000),
                random.uniform(1.2, 1.5),
                random.randint(3, 4),
            )
            for _ in range(width * 10)
        ]

    def draw(self):
        for rain in self.rain_instances:
            pygame.draw.rect(
                self.screen,
                random.choices(
                    (
                        (93, 63, 211),
                        (48, 25, 52),
                        (195, 177, 225),
                        (127, 0, 255),
                        (25, 25, 25),
                        (200, 200, 200),
                    )
                )[0],
                rain,
            )

    def update(self):
        for rain in self.rain_instances:
            rain.y += self.vel * random.uniform(1, 2)
            if rain.y > height:
                rain.y = 0


rain = Rain(screen)

while running:
    for event in pygame.event.get():
        if (
            event.type != pygame.QUIT
            and event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
            or event.type == pygame.QUIT
        ):
            running = False

    pygame.display.update()

    screen.fill((10, 10, 10))
    rain.draw()
    rain.update()

    pygame.display.flip()
    pygame.event.pump()
