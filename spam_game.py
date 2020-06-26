import pygame
import sys
import time
import random
from pygame.locals import *

# set setting variable
window_width = 960
window_higth = 720

# create spam class


class Spam(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/spam3.png")
        self.image_size = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.Rect((self.pos_x, self.pos_y), self.image_size.size)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, new_x, new_y):
        self.rect = pygame.Rect((new_x, new_y), self.image_size.size)


def main():
    # initialize pygame
    pygame.init()
    # set window size
    screen = pygame.display.set_mode((window_width, window_higth))
    # set window title
    title = "Do you like SPAM?"
    pygame.display.set_caption(title)

    #  setup fps
    fps_controll = pygame.time.Clock()

    # load background image
    background = pygame.image.load("./image/Sketch_Spam.jpg")
    # adjust background image size to screen size
    background = pygame.transform.scale(
        background, (window_width, window_higth))
    background_size = background.get_rect()

    # set title
    title_font = pygame.font.SysFont(None, 100)
    title_text = title_font.render(
        title, True, (255, 0, 0))

    # set score board
    score = 0

    # setup text font
    text_font = pygame.font.SysFont(None, 80)

    # setup score board
    score_board_text = text_font.render(
        "Score : " + str(score), True, (0, 0, 0))

    # set hight score board
    hight_score = 0

    # setup high score board
    higth_score_board_text = text_font.render(
        "High Score : " + str(hight_score), True, (0, 0, 0))

    # setup restart board
    restart_text = text_font.render(
        "", True, (0, 0, 0))

    # setup update record board
    update_record_text = text_font.render("", True, (0, 0, 0))

    # setup timeup

    # outside position
    outside_screen_posx_xy = 1500

    # craete main spam
    main_spam_init_x = 540
    main_spam_init_y = 240
    main_spam = Spam(main_spam_init_x, main_spam_init_y)

    # playing spam
    playing_spam_pos_init_x = random.randrange(960 - 100)
    playing_spam_pos_init_y = random.randrange(720 - 100)
    playing_spam = Spam(outside_screen_posx_xy, outside_screen_posx_xy)

    # load bgm
    bgm = pygame.mixer.Sound("./sound/liberty_bell.mp3")
    spam_voice_1 = pygame.mixer.Sound("./sound/spam1.mp3")
    spam_voice_2 = pygame.mixer.Sound("./sound/spam2.mp3")

    # setup game state
    game_start = False
    game_end = False

    # main sprocess
    while True:
        # set up fps
        fps_controll.tick(30)

        # 背景画像描画
        screen.fill((255, 255, 255))
        screen.blit(background, background_size)

        # title load
        screen.blit(title_text, (200, 100))

        # score board load
        screen.blit(score_board_text, (70, 15))

        # high socre board load
        screen.blit(higth_score_board_text, (440, 15))

        # restart comment load
        screen.blit(restart_text, (50, 600))

        # update_record load
        screen.blit(update_record_text, (50, 150))

        # main start spam load
        main_spam.draw(screen)
        # play spam load
        playing_spam.draw(screen)
        # 終了判定
        checkForQuit()

        # 描画更新
        pygame.display.update()

        # 各イベント定義
        for event in pygame.event.get():
            # クリック時判定
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                # 開始判定 初期表示スパムクリックで開始　bgm再生　タイトル消去、スコア表示
                if not game_start and main_spam.rect.collidepoint(event.pos):
                    # play bgm
                    bgm.play()
                    # overwrite title ,
                    title_text = title_font.render("", True, (255, 0, 0))
                    screen.blit(title_text, (0, 0))
                    # init score
                    score = 0
                    score_board_text = text_font.render(
                        "Score : " + str(score), True, (0, 0, 0))

                    # move main spam to out side of screen
                    main_spam.update(outside_screen_posx_xy,
                                     outside_screen_posx_xy)
                    game_start = True
                    playing_spam.update(
                        playing_spam_pos_init_x, playing_spam_pos_init_y)

                    # delete unnecessary text while playing
                    restart_text = text_font.render("", True, (0, 0, 0))
                    screen.blit(restart_text, (0, 0))
                    update_record_text = text_font.render(
                        "", True, (0, 0, 0))
                    screen.blit(update_record_text, (0, 0))

                    # start timer
                    game_timer = pygame.time.get_ticks()

                # ゲーム開始中
                elif game_start and playing_spam.rect.collidepoint(event.pos) and pygame.time.get_ticks() - game_timer < 30000:
                    playing_spam_pos_x = random.randrange(window_width - 100)
                    playing_spam_pos_y = random.randrange(window_higth - 100)
                    playing_spam.update(playing_spam_pos_x,
                                        playing_spam_pos_y)
                    score += 1
                    score_board_text = text_font.render(
                        "Score : " + str(score), True, (0, 0, 0))
                    screen.blit(score_board_text, (0, 0))
                    if score % 5 == 0:
                        spam_voice_2.play()
                    else:
                        spam_voice_1.play()
                elif game_start and pygame.time.get_ticks() - game_timer > 30000:
                    # ゲーム停止状態に遷移
                    game_start = False
                    # ゲーム終了表示、3秒待つ
                    pygame.time.delay(2000)
                    # ハイスコア表示、 ゲームリスタート用に元画像表示
                    if hight_score < score:
                        hight_score = score
                        higth_score_board_text = text_font.render(
                            "High Score : " + str(hight_score), True, (0, 0, 0))
                        screen.blit(higth_score_board_text, (0, 0))
                        update_record_text = text_font.render(
                            "You got the highest score!!!", True, (255, 0, 0))
                        screen.blit(update_record_text, (0, 0))

                    # リプレイ表示描写
                    playing_spam.update(
                        outside_screen_posx_xy, outside_screen_posx_xy)
                    main_spam.update(main_spam_init_x, main_spam_init_y)
                    restart_text = text_font.render(
                        "More SPAM? Click SPAM Again!!", True, (255, 0, 0))
                    screen.blit(restart_text, (0, 0))


# 終了判定メソッド
def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
