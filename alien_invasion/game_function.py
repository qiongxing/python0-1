import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
import json

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sb.write_score()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets,sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y,sb)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y,sb):
    "在玩家单机Play时开始新游戏"
    button_clicked= play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active =True
        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #清空外星人列表子弹列表
        aliens.empty()
        bullets.empty()
        #创建新的外星人,并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def check_keydown_events(event,ai_settings,screen,ship,bullets,sb):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        #飞船右移
        ship.moving_right =True
    elif event.key == pygame.K_LEFT:
        #飞船左移
        ship.moving_left =True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sb.write_score()
        sys.exit()

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        #飞船右移停止
        ship.moving_right =False
    elif event.key == pygame.K_LEFT:
        #飞船左移停止
        ship.moving_left =False

def update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb):
    """更新屏幕的图像，并切换新屏幕"""
    #每次循环时重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    sb.show_score()
    #让最近绘制屏幕可见
    pygame.display.flip()

def fire_bullet(ai_settings,screen,ship,bullets):
    """没有达到限制就发射一颗子弹"""
    #创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet =Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def update_bullets(ai_settings,screen,ship,bullets,aliens,stats,sb):
    """更新子弹位置,并删除一消失的子弹"""
    #编组调用update时，会自动调用内部每个精灵的update方法
    bullets.update()    
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb):
    """响应子弹和外星人的碰撞"""
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for alines in collisions.values():
            stats.score += ai_settings.alien_points*len(alines)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        #删除现有的子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)


def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人并计算可容纳多少个外星人，这个外星人不加入编组中
    alien =Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(ai_settings,alien_width):
    """计算每行最多容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少汗外星人"""
    available_space_y =(ai_settings.screen_height - (3 * alien_height)- ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """"创建一个外星人并将其放在当前行"""
    alien =Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x =alien_width +2*alien_width*alien_number
    alien.rect.x =alien.x
    alien.rect.y = alien.rect.height +2*alien.rect.height*row_number
    aliens.add(alien)

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """更新外星人位置监测飞船碰撞"""
    check_fleet_edge(ai_settings,aliens)
    aliens.update()
    #监测外星人与飞船碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    "响应外星人撞到飞船"
    if stats.ships_left > 0:
        #将ships_left减一
        stats.ships_left -=1
        #更新记分牌
        sb.prep_ships()
        #清空外星人列表，子弹列表
        aliens.empty()
        bullets.empty()

        #创建新的外星人，并将飞船放到屏幕中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
    "检查是否有外星人到达了屏幕底端"
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
            break

def check_fleet_edge(ai_settings,aliens):
    """"有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将外星人下移，并改变方向"""
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *=-1

def check_high_score(stats,sb):
    "检查是否诞生最高得分"
    if stats.score >stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()