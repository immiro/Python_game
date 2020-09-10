
import pygame
from pygame.locals import *
import random
import math

width, height = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake by Miro")

#player variables
player_radius = 20.0
player_animation = player_radius
player_x = random.uniform(0+player_radius, 800-player_radius)
player_y = random.uniform(0+player_radius, 600-player_radius)
vel = 0.1

#food variables
foodx = random.uniform(50, 500)
foody = random.uniform(50, 500)
food_rad = 5.0

#other variables
points = 0
pygame.font.init()

def main():
    global player_radius, player_x, player_y, player_area, points, foody, foodx, vel, font, player_animation, acc
    pygame.init()
    pygame.time.delay(100)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y += vel
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= vel

        #check if player hits borders
        if player_x - player_radius <= 0:
            run = False
        if player_x + player_radius >= width:
            run = False

        if player_y - player_radius <= 0:
            run = False
        if player_y + player_radius >= height:
            run = False

        #check if player eats food
        y = player_y - foody
        x = player_x - foodx

        dis = math.sqrt(y**2 + x**2)
        if dis <= player_radius + food_rad:
            foodx = random.uniform(50, 500)
            foody = random.uniform(50, 500)
            player_radius += 0.5
            points += 1
            vel += 0.05
            print(points)

        pygame.font.init()
        font = pygame.font.SysFont('AGENCYR.TFF', 32)
        points_text = font.render('Points {0}'.format(points), False, (255, 255, 255))

        if player_animation < player_radius:
            player_animation += 0.04
        else:
            player_animation = player_radius

        screen.fill((0, 0, 0))

        #draw player
        pygame.draw.circle(screen, (255, 255, 255), (int(player_x),
                                                     int(player_y)), int(player_animation))
        #draw food
        pygame.draw.circle(screen, (255, 255, 0),
                           (int(foodx), int(foody)), int(food_rad))

        screen.blit(points_text, (30, 30))

        pygame.display.update()


if __name__ == '__main__':
    main()
