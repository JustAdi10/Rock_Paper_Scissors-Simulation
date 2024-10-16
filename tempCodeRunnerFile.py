import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rock Paper Scissors Simulation')

rock_img = pygame.image.load('Rock.webp')
paper_img = pygame.image.load('Paper.webp')
scissors_img = pygame.image.load('Scissors.webp')

rock_img = pygame.transform.scale(rock_img, (50, 50))
paper_img = pygame.transform.scale(paper_img, (50, 50))
scissors_img = pygame.transform.scale(scissors_img, (50, 50))

class GameItem:
    def __init__(self, x, y, item_type):
        self.x = x
        self.y = y
        self.item_type = item_type
        self.speed = 3
        self.direction = random.choice([(1, 1), (1, -1), (-1, 1), (-1, -1)])

    def move(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

        if self.x < 0 or self.x > width - 50:
            self.direction = (-self.direction[0], self.direction[1])
            self.x = max(0, min(self.x, width - 50))
        if self.y < 0 or self.y > height - 50:
            self.direction = (self.direction[0], -self.direction[1])
            self.y = max(0, min(self.y, height - 50))

    def draw(self, screen):
        if self.item_type == 'rock':
            screen.blit(rock_img, (self.x, self.y))
        elif self.item_type == 'paper':
            screen.blit(paper_img, (self.x, self.y))
        elif self.item_type == 'scissors':
            screen.blit(scissors_img, (self.x, self.y))

def determine_winner(item1, item2):
    if item1.item_type == item2.item_type:
        return None
    elif (item1.item_type == 'rock' and item2.item_type == 'scissors') or \
         (item1.item_type == 'scissors' and item2.item_type == 'paper') or \
         (item1.item_type == 'paper' and item2.item_type == 'rock'):
        return item1
    else:
        return item2

items = []
num_items = 30

for _ in range(num_items):
    item_type = random.choice(['rock', 'paper', 'scissors'])
    x = random.randint(0, width - 50)
    y = random.randint(0, height - 50)
    items.append(GameItem(x, y, item_type))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for item in items:
        item.move()
        item.draw(screen)

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if (items[i].x < items[j].x + 50 and items[i].x + 50 > items[j].x and
                items[i].y < items[j].y + 50 and items[i].y + 50 > items[j].y):
                winner = determine_winner(items[i], items[j])
                if winner:
                    loser = items[j] if winner == items[i] else items[i]
                    loser.item_type = winner.item_type  # Change loser to winner's type

    pygame.display.flip()
    pygame.time.delay(45)

pygame.quit()
sys.exit()
