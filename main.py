import pygame, sys
from button import Button

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

# colors
white = (255, 255, 255)
black = (0, 0, 0)
grey = (192, 192, 192)
bg_color = (195, 248, 255)

# button images
start_img = pygame.image.load("Images/Button_start1.png")  
start_img_hover = pygame.image.load("Images/Button_start2.png")
start_img_click = pygame.image.load("Images/Button_start3.png")
settings_img = pygame.image.load("Images/Button_settings1.png")
settings_img_hover = pygame.image.load("Images/Button_settings2.png")
settings_img_click = pygame.image.load("Images/Button_settings3.png")


start_button = Button(100, 100, start_img, start_img_hover, start_img_click, 1)
settings_button = Button(100, 200, settings_img, settings_img_hover, settings_img_click, 1)
    


running = True

while running:
    screen.fill(bg_color)
    start_button.draw(screen)
    settings_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit

    pygame.display.flip()
    
clock.tick(60)

pygame.quit()
