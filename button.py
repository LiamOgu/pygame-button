import pygame
from sound import Sound

class Button:
    def __init__(self, x, y, image, hover_image, click_image, scale):

        width = image.get_width()
        height = image.get_height()        
        self.click_image = pygame.transform.scale(click_image, (int(width*scale), int(height*scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(width*scale), int(height*scale)))
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.fake_rect = self.image.get_rect()
        self.fake_rect.topleft = (x, y)
        self.scale = scale
        self.clicked = False
        self.main_music = Sound()



    def draw(self, surface):

        index = 0  # index to parcouring the differents images (main image, hover image, click image)
        imgs = [self.image, self.hover_image, self.click_image] 
        pos = pygame.mouse.get_pos()
        if index == 0:
            surface.blit(imgs[index], (self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos):

            index = 1
            surface.blit(imgs[index], (self.rect.x, self.rect.y))

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            
                index = 2
                surface.blit(imgs[index], (self.rect.x, self.rect.y))

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        