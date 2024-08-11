import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das cores (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Definição das dimensões da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de MRU com Controle e Aceleração")

# Função para desenhar o texto na tela
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Função para o menu principal
def main_menu():
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(WHITE)
        draw_text('Menu Principal', font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
        draw_text('Pressione ENTER para começar', small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()

# Função principal do jogo
def game_loop():
    posicao_x = WIDTH // 2
    posicao_y = HEIGHT // 2
    velocidade = 5
    aceleracao = 5  # Valor da aceleração ao pressionar Shift
    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Controle do movimento com as setas do teclado
        keys = pygame.key.get_pressed()
        atual_velocidade = velocidade

        # Aplicar aceleração se o Shift for pressionado
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            atual_velocidade += aceleracao

        if keys[pygame.K_LEFT]:
            posicao_x -= atual_velocidade
        if keys[pygame.K_RIGHT]:
            posicao_x += atual_velocidade
        if keys[pygame.K_UP]:
            posicao_y -= atual_velocidade
        if keys[pygame.K_DOWN]:
            posicao_y += atual_velocidade

        # Limite para que o objeto não saia da tela
        if posicao_x < 0:
            posicao_x = 0
        if posicao_x > WIDTH:
            posicao_x = WIDTH
        if posicao_y < 0:
            posicao_y = 0
        if posicao_y > HEIGHT:
            posicao_y = HEIGHT

        # Redesenhar o fundo e o objeto
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (posicao_x, posicao_y), 20)
        
        pygame.display.flip()

        clock.tick(60)

# Inicialização do menu principal
main_menu()
