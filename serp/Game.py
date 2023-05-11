import pygame
from random import randrange

######################
# Paràmetres del joc #
######################
FPS = 4
fpsClock = pygame.time.Clock()
estat="playing"
punts=0

#dimensions de la finestra
window_width=800
window_height=600

#nombre de files i de columnes
num_rows=40
num_columns=30

#dimensions de cada tile
tile_width = window_width/num_rows
tile_height = window_height/num_columns

# Inicialitzar Pygame
pygame.init()

# Crear la finestra
windows = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("El joc de la serp")

# Configurar la repetición de teclas
pygame.key.set_repeat(1, 50)

# Propietats de la serp
serp_x = num_rows//3
serp_y = num_columns//2
serp_direccio = [1,0]
serp_cua = [] 

# Propietats de la poma
poma_x=randrange(num_rows)
poma_y=randrange(num_columns)

#Imatges dels elements
serp_img = pygame.image.load("./imatges/cap.png")
serp_img = pygame.transform.scale(serp_img, (tile_width, tile_height))
poma_img = pygame.image.load("./imatges/poma.png")
poma_img = pygame.transform.scale(poma_img, (tile_width, tile_height)) 
cua_img = pygame.image.load("./imatges/cua.png")
cua_img = pygame.transform.scale(cua_img, (tile_width, tile_height)) 

# Bucle principal
while estat=="playing":

    ###################
    # Event de teclat #
    ###################
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                if serp_direccio[0]!=1:
                    serp_direccio=[-1,0]
            elif evento.key == pygame.K_RIGHT:
                if serp_direccio[0]!=-1:
                    serp_direccio=[1,0]
            elif evento.key == pygame.K_UP:
                if serp_direccio[1]!=1:
                    serp_direccio=[0,-1]
            elif evento.key == pygame.K_DOWN:
                if serp_direccio[1]!=-1:
                    serp_direccio=[0,1]

    ##########
    # logica #
    ##########

    # colissió amb la poma
    if poma_x==serp_x and poma_y==serp_y:
        poma_x=randrange(num_rows)
        poma_y=randrange(num_columns)
        serp_cua.append([0,0])
        punts=punts+1
        FPS=FPS+0.25

    # moure serp
    pos_x = serp_x
    pos_y = serp_y

    # moure el cap
    serp_x=serp_x+serp_direccio[0]
    serp_y=serp_y+serp_direccio[1]

    # moure el cos
    for num in range(len(serp_cua)-1,-1,-1):
        if num>0:
            serp_cua[num][0]=serp_cua[num-1][0]
            serp_cua[num][1]=serp_cua[num-1][1]
        else:
            serp_cua[0][0]=pos_x
            serp_cua[0][1]=pos_y

    # final de joc    
    if serp_x<0 or serp_x>=num_rows or serp_y<0 or serp_y>=num_columns:
        estat="end"

    ##########
    # render #
    ##########

    windows.fill((255, 255, 255)) 
    windows.blit(serp_img, (serp_x*tile_width, serp_y*tile_height)) 
    windows.blit(poma_img, (poma_x*tile_width, poma_y*tile_height)) 

    print("CUA")
    for cua in serp_cua:
        windows.blit(cua_img, (cua[0]*tile_width, cua[1]*tile_height))
        print(cua)
        
    pygame.display.update()
    fpsClock.tick(FPS)
