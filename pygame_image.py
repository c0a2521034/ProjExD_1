import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    bgR_img = pg.transform.flip(bg_img, True, False)
    k3_image =pg.image.load("fig/3.png")#工科トン画像
    k3_image = pg.transform.flip(k3_image, True,False)
    k3_rct = k3_image.get_rect() #練習10.1　工科トンのrectの取得
    k3_rct.center = 300, 200 # 練習10.2　工科トンの初期座標の指定

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #練習10.3全キーの押下状態の取得
        if key_lst[pg.K_UP]:#練習10上下左右の移動
            k3_rct.move_ip(0,-1)
        if key_lst[pg.K_DOWN]:
            k3_rct.move_ip(0,+1)
        if key_lst[pg.K_LEFT]:
            k3_rct.move_ip(-1,0)
        if key_lst[pg.K_RIGHT]:
            k3_rct.move_ip(+2,0)


        k3_rct.move_ip(-1,0)
        x = tmr%3200 #練習5 練習9
        screen.blit(bg_img, [-x, 0]) #練習2
        screen.blit(bgR_img, [-x + 1600, 0])
        screen.blit(bgR_img,[-x + 3200,0])#練習9
        screen.blit(k3_image, k3_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()