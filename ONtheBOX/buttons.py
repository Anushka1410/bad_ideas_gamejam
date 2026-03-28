import pygame
import sys

print("Starting pygame")
pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu Flow")

background = pygame.image.load("background.jpg.jpeg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

font = pygame.font.SysFont(None, 40)

menu_state = "main"
game_paused = False
game_over = False
running = True

class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.image = font.render(text, True, WHITE)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect.inflate(20, 10))
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


play_btn = Button("Play", 400, 200)
options_btn = Button("Options", 400, 260)
quit_btn = Button("Quit", 400, 320)

options_audio_btn = Button("Audio Settings", 400, 200)
options_back_btn = Button("Back", 400, 260)

resume_btn = Button("Resume", 400, 200)
restart_btn = Button("Restart", 400, 260)
home_btn = Button("Home", 400, 320)

end_restart_btn = Button("Restart", 400, 250)
main_menu_btn = Button("Main Menu", 400, 320)

clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if menu_state == "main":
                if play_btn.is_clicked(mouse_pos):
                    menu_state = "game"
                elif options_btn.is_clicked(mouse_pos):
                    menu_state = "options"
                elif quit_btn.is_clicked(mouse_pos):
                    running = False

            elif menu_state == "options":
                if options_audio_btn.is_clicked(mouse_pos):
                    menu_state = "audio"
                elif options_back_btn.is_clicked(mouse_pos):
                    menu_state = "main"

            elif menu_state == "audio":
                if options_back_btn.is_clicked(mouse_pos):
                    menu_state = "main"

            elif menu_state == "pause":
                if resume_btn.is_clicked(mouse_pos):
                    menu_state = "game"
                elif restart_btn.is_clicked(mouse_pos):
                    menu_state = "game"
                elif home_btn.is_clicked(mouse_pos):
                    menu_state = "main"

            elif menu_state == "end":
                if end_restart_btn.is_clicked(mouse_pos):
                    menu_state = "game"
                elif main_menu_btn.is_clicked(mouse_pos):
                    menu_state = "main"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and menu_state == "game":
                menu_state = "pause"

            if event.key == pygame.K_e and menu_state == "game":
                menu_state = "end"  


    if menu_state == "main":
        play_btn.draw()
        options_btn.draw()
        quit_btn.draw()

    elif menu_state == "game":
        text = font.render("GAME RUNNING (Press P to Pause, E to End)", True, WHITE)
        screen.blit(text, (100, 250))

    elif menu_state == "options":
        options_audio_btn.draw()
        options_back_btn.draw()

    elif menu_state == "audio":
        text = font.render("Audio Settings (not implemented)", True, WHITE)
        screen.blit(text, (150, 200))
        options_back_btn.draw()

    elif menu_state == "pause":
        resume_btn.draw()
        restart_btn.draw()
        home_btn.draw()

    elif menu_state == "end":
        end_restart_btn.draw()
        main_menu_btn.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()         
