import sys
import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi juego")

background_image = pygame.image.load(r'./fondos/fondo.jpg').convert()
background_image2 = pygame.image.load(r'./fondos/fondo2.jpg').convert()
background_image3 = pygame.image.load(r'./fondos/fondo3.jpg').convert()
viajero = pygame.image.load(r'./fondos/viajero.png').convert()
font_name = 'Segoe UI'
font_size = 30
font = pygame.font.SysFont(font_name, font_size)

def text(text):
    message_text = text

    text_surface = font.render(message_text, True, (255, 255, 255)) 
    text_rect = text_surface.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    return text_surface, text_rect

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

button_hovered = False
button_pressed = False
x = 0

# Función para dibujar un botón
def draw_button(texto, surface, rect, text, font, text_color, button_color, hover_color, pressed_color):
    global button_hovered, button_pressed, x

    mouse_pos = pygame.mouse.get_pos()

    button_hovered = rect.collidepoint(mouse_pos)
    if button_hovered:
        if pygame.mouse.get_pressed()[0] == 1:
            button_pressed = True
            return button_pressed
        else:
            if button_pressed:
                #button_click_action(texto)
                x = 1
            return False

    pygame.draw.rect(surface, button_color, rect, 2)

    font_surface = font.render(text, True, text_color)
    font_rect = font_surface.get_rect(center=rect.center)
    surface.blit(font_surface, font_rect)

def button_click_action(texto):
    screen.fill((0, 0, 0)) # Limpia la pantalla
    screen.blit(background_image, (0, 0))
    text_surface, text_rect = text(texto)
    screen.blit(text_surface, text_rect)

def create_btn1(font, texto):

    button_rect = pygame.Rect(40, 50, 200, 60)
    draw_button(texto, screen, button_rect, "Continuar... ", font, WHITE, WHITE, DARK_GRAY, BLACK)


def render_wrapped_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    text_surfaces = [font.render(line, True, BLACK) for line in lines]
    return text_surfaces

def render_text(texto):
    text_surfaces = render_wrapped_text(texto, font, screen_width)

    text_rects = [text_surface.get_rect(center=(screen_width // 2, (i + 1) * text_surface.get_height())) for i, text_surface in enumerate(text_surfaces)]

    return text_surfaces, text_rects

h = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    screen.blit(background_image, (0, 0))
    text_surface, text_rect = text('Hola guerrero intergalactico! ')
    screen.blit(text_surface, text_rect)
    texto1 = 'Vamos a salvar la galaxia, unos terribles zumborg están atacando planetas y destruyendo la vida'
    create_btn1(font, texto1)
    if x == 1:
        
        screen.fill((0, 0, 0))
        screen.blit(background_image2, (-100, -100))
        screen.blit(viajero, (600, 300))
        text_surfaces, text_rects = render_text(texto1)
        texto2 = 'Vamos al combate, Salvemos la galaxia.'
        for text_surface, text_rect in zip(text_surfaces, text_rects):
            screen.blit(text_surface, text_rect)

    pygame.display.flip() 

pygame.quit()
sys.exit()

