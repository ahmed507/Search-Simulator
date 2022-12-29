from queue import Queue
import pygame
import sys
from bfs import BFS

class Main:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (255, 0, 255)
    FPS = 60
    maze = [[' ', ' ', ' ', '#', ' ', ' ', ' ',' ', ' ', ' ', '#', ' ', ' ', ' ','#',' '],
            [' ', '#', ' ', '#', ' ', '#', ' ',' ', ' ', ' ', '#', ' ', ' ', ' ','#',' '],
            [' ', '#', ' ', ' ', ' ', '#', ' ',' ', ' ', ' ', '#', ' ', ' ', ' ','#',' '],
            [' ', '#', '#', '#', '#', '#', ' ',' ', ' ', '#', ' ', ' ', '#', ' ',' ',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', '#', ' ', ' ', ' ','#',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', '#', ' ', ' ', ' ',' ',' '],
            [' ', ' ', '#', ' ', ' ', ' ', ' ',' ', ' ', ' ', '#', ' ', ' ', ' ','#',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ',' ',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ','#',' '],
            [' ', ' ', ' ', '#', ' ', ' ', ' ',' ', ' ', ' ', '#', ' ', ' ', ' ','#',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', '#', ' ', ' ', ' ',' ',' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ']]


    n = len(maze)
    m = len(maze[0])
    SCREEN_WIDTH = 640+n
    SCREEN_HEIGHT = 480+m

    def reset(self):
        self.maze =[[' ' for j in range(self.m)] for i in range(self.n)]

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("BFS Simulator")
        clock = pygame.time.Clock()
        size = 40
        stx, sty = 0,0
        enx,eny = self.n-1,self.m-1
        bfs = BFS(self.maze, (stx, sty), (enx, eny))
        paths,shortest_path = bfs.get_path(self.maze, (stx, sty), (enx, eny))
        distance =len(shortest_path)-1
        # print(paths)
        #make a grid of rectangles to display the maze and the path on the screen
        rectangles = []
        for y in range(self.n):
            rr=[]
            for x in range(self.m):
                rect = pygame.Rect(x * (size+1), y * (size+1), size, size)
                # The grid will be a list of (rect, color) tuples.
                if self.maze[y][x] == '#':
                    rr.append((rect, self.BLACK))
                else:
                    rr.append((rect, self.WHITE))
            rectangles.append(rr)



        myfont = pygame.font.SysFont("Comic Sans MS", 34)
        no_path = myfont.render("NO PATHS FOUND!", 1, self.PURPLE)
        min_dis = myfont.render("MINIMUM DISTANCE : "+str(distance), 1, self.PURPLE)

        while True: 
            clock.tick(self.FPS)
            screen.fill(self.BLACK)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for i in range(len(rectangles)):
                for j in range(len(rectangles[i])):
                    rect, color = rectangles[i][j]
                    pygame.draw.rect(screen, color, rect)
            rect, color = rectangles[stx][sty]
            pygame.draw.rect(screen, self.RED, rect)
            rect, color = rectangles[enx][eny]
            pygame.draw.rect(screen, self.RED, rect)

            # if there are no paths found then display the message on the screen
            if len(paths) ==0:   
                screen.blit(no_path, (150, 300))
            else:
                # display the path on the screen with a delay of 250ms between each step of the path
                # pygame.display.update()
                for i,j in paths:
                    for ii in range(len(rectangles)):
                        for jj in range(len(rectangles[i])):
                            rect, color = rectangles[ii][jj]
                            if i == ii and j == jj and color == self.WHITE:
                                rectangles[ii][jj] = (rect, self.GREEN)
                                pygame.draw.rect(screen, self.GREEN, rect)
                                pygame.display.update()
                                pygame.time.delay(15)
                for i,j in shortest_path:
                    for ii in range(len(rectangles)):
                        for jj in range(len(rectangles[i])):
                            rect, color = rectangles[ii][jj]
                            if i == ii and j == jj and color == self.GREEN:
                                rectangles[ii][jj] = (rect, self.BLUE)
                                pygame.draw.rect(screen, self.BLUE, rect)
                                pygame.display.update()
                                pygame.time.delay(15)
                
                if distance>0:
                    screen.blit(min_dis, (100, 320))
            
            pygame.display.update()

if __name__ == "__main__":
    Main = Main()
    Main.main()