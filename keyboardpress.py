import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((320, 240))

def getKey(keyName):
    answer = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        answer = True
    pygame.display.update()
    return answer

def main():
    print(getKey("a"))

if __name__ == '__main__':
    init()
    while True:
        main()

