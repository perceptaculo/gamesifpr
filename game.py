import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das cores (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Definição das dimensões da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de MRU")

# Parâmetros do MRU
velocidade = 10  # Velocidade constante em pixels por frame
posicao_x = 50  # Posição inicial no eixo X
posicao_y = HEIGHT // 2  # Posição constante no eixo Y (meio da tela)

# Loop principal do programa
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualização da posição do objeto
    posicao_x += velocidade

    # Redesenhar o fundo e o objeto
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (posicao_x, posicao_y), 20)

    # Verificação se o objeto saiu da tela (reinicia o movimento)
    if posicao_x > WIDTH:
        posicao_x = 0

    # Atualização da tela
    pygame.display.flip()

    # Controle da velocidade de atualização (frames por segundo)
    clock.tick(240)
