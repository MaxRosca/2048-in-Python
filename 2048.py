import random

import pygame

blackColor = (0, 0, 0)
whiteColor = (255, 255, 255)
screenSize = (600, 600)

pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('2048')
screen.fill(blackColor)
clock = pygame.time.Clock()
pygame.font.init()

gridSize = 3
exitGame = False
gameOver = False
moved = False
positions = []

def initGrid(gridSize):
    gridColumn = []
    grid = []
    for i in range(gridSize):
        for j in range(gridSize):
            gridColumn.append(0)
        grid.append(gridColumn)
        gridColumn = []
    for i in range(2):
        randomStart1 = random.randrange(gridSize)
        randomStart2 = random.randrange(gridSize)
        grid[randomStart1][randomStart2] = 2
    return grid

def drawGrid(gridLen, screen, color):
    screenWidth = screenSize[0]
    screenHeight = screenSize[1]
    boxWidth = screenWidth/gridLen - 6.5
    boxHeight = screenHeight/gridLen - 6.5
    global positions
    x = 5
    y = 5
    for i in range(gridLen):
        for j in range(gridLen):
            pygame.draw.rect(screen, color, [x, y, boxWidth, boxHeight])
            positions.append((x + boxWidth/2 - 10, y + boxHeight/2 - 10))
            x += boxWidth + 5
        y += boxHeight + 5 
        x = 5

def addElement(grid):
    options = []
    zeroInGrid = False
    if grid != None:
        for i in range(len(grid)):
            if 0 in grid[i]:
                zeroInGrid = True
                for j in range(len(grid)):
                    if grid[i][j] == 0:
                        options.append((i, j))
        if zeroInGrid:
            addNumberPos = random.randrange(len(options))
            addedNumber = random.randrange(2,4,2)
            option = options[addNumberPos]
            grid[option[0]][option[1]] = addedNumber
        
        return grid

def drawNumbers(grid, positions):
    font = pygame.font.SysFont('Comic Sans MS', round(screenSize[0]/12))
    k = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            number = font.render(str(grid[i][j]), False, (0, 0, 0))
            if grid[i][j] != 0:
                screen.blit(number, positions[k])
            k = k + 1

def move(grid, key):
    move.moved = 0
    for i in range(len(grid)):
        w = len(grid) - 1
        j = 0
        if key == "R":
            while j != len(grid) - 1:
                if j != len(grid):
                    if grid[i][j + 1] == 0 and grid[i][j] != 0:
                        grid[i][j + 1] = grid[i][j]
                        grid[i][j] = 0
                        move.moved += 1
                        j = 0
                    elif grid[i][j+1] == grid[i][j] and grid[i][j] != 0:
                        grid[i][j+1] += grid[i][j]
                        grid[i][j] = 0
                    else:
                        j += 1
                    

        if key == "L":
            while w != 0:
                if w != 0:
                    if grid[i][w - 1] == 0 and grid[i][w] != 0:
                        grid[i][w - 1] = grid[i][w]
                        grid[i][w] = 0
                        w = len(grid) - 1
                        move.moved += 1
                    elif grid[i][w - 1] == grid[i][w] and grid[i][w] != 0:
                        grid[i][w - 1] += grid[i][w]
                        grid[i][w] = 0
                    else:
                        w = w - 1
        
        if key == "D":
            while j != len(grid) - 1:
                if j != len(grid):
                    if grid[j + 1][i] == 0 and grid[j][i] != 0:
                        grid[j + 1][i] = grid[j][i]
                        grid[j][i] = 0
                        j = 0
                        move.moved += 1
                    elif grid[j+1][i] == grid[j][i] and grid[j][i] != 0:
                        grid[j+1][i] += grid[j][i]
                        grid[j][i] = 0
                    else:
                        j += 1
        
        if key == "U":
            while w != 0:
                if w != 0:
                    if grid[w - 1][i] == 0 and grid[w][i] != 0:
                        grid[w - 1][i] = grid[w][i]
                        grid[w][i] = 0
                        w = len(grid) - 1
                        move.moved += 1
                    elif grid[w - 1][i] == grid[w][i] and grid[w][i] != 0:
                        grid[w - 1][i] += grid[w][i]
                        grid[w][i] = 0
                    else:
                        w = w - 1
    for col in grid:
        print(col)
    print('\n')

grid = initGrid(gridSize)
drawGrid(gridSize, screen, whiteColor)
drawNumbers(grid, positions)

while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move(grid, "R")
                moved = True
            if event.key == pygame.K_LEFT:
                move(grid, "L")
                moved = True
            if event.key == pygame.K_DOWN:
                move(grid, "D")
                moved = True
            if event.key == pygame.K_UP:
                move(grid, "U")
                moved = True
            screen.fill(blackColor)
            drawGrid(gridSize, screen, whiteColor)
            drawNumbers(grid, positions)

    if grid != None:
        if moved and move.moved != 0:
            grid = addElement(grid)
            moved = False
            screen.fill(blackColor)
            drawGrid(gridSize, screen, whiteColor)
            drawNumbers(grid, positions)

    pygame.display.update()

pygame.quit()
exit
