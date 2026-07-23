import pygame
pygame.init()

width = 800
height = 600
color_1 = (20, 20, 30)
color_2 = (30, 30, 30)
color_mtn = (170, 0, 255)
c_m2 = (245, 245, 245)
title_font = pygame.font.SysFont("arial", 60)
title = title_font.render("PHANTOM CHALLENGE", True, color_mtn)
title_rect = title.get_rect(center=(400, 50))
button_font = pygame.font.SysFont("arial", 35)
start_text = button_font.render("START", True, c_m2)
exit_text = button_font.render("EXIT", True, c_m2)
easy_text = button_font.render("easy", True, c_m2)
hard_text = button_font.render("hard", True, c_m2)
normal_text = button_font.render("normal", True, c_m2)
back_text = button_font.render("back", True, c_m2)
footer_font = pygame.font.SysFont("consolas", 18)
footer_text = footer_font.render("Phantom Challenge v0.1 Alpha * MILAD 2026", True, (245, 245, 245))
footer_rect = footer_text.get_rect(center=(400, 580))
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Phantom Challenge")
#================================================button=================================================================
start_button = pygame.Rect(200, 150, 150, 40)
exit_button = pygame.Rect(500, 150, 150, 40)
start_txt_rect = start_text.get_rect(center=start_button.center)
exit_txt_rect = exit_text.get_rect(center=exit_button.center)
easy_rect = easy_text.get_rect(center=(400, 180))
hard_rect = hard_text.get_rect(center=(400, 260))
normal_rect = normal_text.get_rect(center=(400, 340))
back_rect = back_text.get_rect(center=(400, 500))
easy_button = pygame.Rect(250, 150, 300, 60)
hard_button = pygame.Rect(250, 230, 300, 60)
normal_button = pygame.Rect(250, 310, 300, 60)
back_button = pygame.Rect(250, 470, 300, 60)
#===========================================================DEF=========================================================
def draw_buttons(mouse_pos) :

    if start_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (0,220,255), start_button, border_radius=15)

    else:
        pygame.draw.rect(screen, (0,170,255), start_button, border_radius=15)
    screen.blit(start_text, start_txt_rect)
    if exit_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (255,80,80), exit_button, border_radius=15)

    else:
        pygame.draw.rect(screen, (220,60,60), exit_button, border_radius=15)
    screen.blit(exit_text, exit_txt_rect)

def draw_difficulty(mouse_pos):
    if easy_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (0,220,255), easy_button, border_radius=15)

    else:
        pygame.draw.rect(screen, (0,170,255), easy_button, border_radius=15)
    screen.blit(easy_text, easy_rect)
    if hard_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (0,220,255), hard_button, border_radius=15)

    else:
        pygame.draw.rect(screen, (0,170,255), hard_button, border_radius=15)
    screen.blit(hard_text, hard_rect)
    if normal_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (0,220,255), normal_button, border_radius=15)

    else:
        pygame.draw.rect(screen, (0,170,255), normal_button, border_radius=15)
    screen.blit(normal_text, normal_rect)
    if back_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (0,220,255), back_button, border_radius=15)

    else:
        pygame.draw.rect(screen, (0,170,255), back_button, border_radius=15)
    screen.blit(back_text, back_rect)
    text = title_font.render("Choose Difficulty... ", True, (170, 0, 255))
    rect = text.get_rect(center=(400, 50))




    screen.blit(text, rect)
    screen.blit(easy_text , easy_rect)
    screen.blit(hard_text, hard_rect)
    screen.blit(normal_text, normal_rect)
    screen.blit(back_text, back_rect)




def draw_title():
    screen.blit(title, title_rect)
def draw_footer():
    screen.blit(footer_text, footer_rect)
def draw_game ():
    screen.fill(color_2)
    game_text = title_font.render("GAME", True, (170, 0, 255))
    game_rect = game_text.get_rect(center=(400, 50))
    screen.blit(game_text, game_rect)


game_state = "menu"
difficulty = None

running = True
while running:
    screen.fill(color_1)
    if game_state == "menu":
        draw_title()
        draw_footer()
        mouse_pos = pygame.mouse.get_pos()
        draw_buttons(mouse_pos)
    elif game_state == "game":
        draw_game()
    elif game_state == "difficulty":
        mouse_pos = pygame.mouse.get_pos()
        draw_difficulty(mouse_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "menu":
                if exit_button.collidepoint(event.pos):
                    running = False
                elif start_button.collidepoint(event.pos):
                    game_state = "difficulty"
            elif game_state == "difficulty":
                if easy_button.collidepoint(event.pos):
                    difficulty = "easy"
                    game_state = "game"
                elif normal_button.collidepoint(event.pos):
                    difficulty = "normal"
                    game_state = "game"
                elif hard_button.collidepoint(event.pos):
                    difficulty = "hard"
                    game_state = "game"
                elif back_button.collidepoint(event.pos):
                    game_state = "menu"
    pygame.display.update()
pygame.quit()


























