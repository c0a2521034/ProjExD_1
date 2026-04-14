import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    bgR_img=pg.transform.flip(bg_img, True, False)
    k3_image =pg.image.load("fig/3.png")#工科トン画像
    k3_image=pg.transform.flip(k3_image, True,False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        x = tmr%3200 #練習5
        screen.blit(bg_img, [-x, 0]) #練習2
        screen.blit(bgR_img, [-x + 1600, 0])
        screen.blit(bgR_img,[-x + 3200,0])
        screen.blit(k3_image, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()