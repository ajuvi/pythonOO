import pygame
from random import randrange
from models.Avatar import Avatar
from models.Poma import Poma
from Globals import Globals

#estat del joc
estat="init"

#puntuació del joc
punts=0

# Inicialitzar Pygame
pygame.init()
fpsClock = pygame.time.Clock()

# Crear la finestra (screen) i la zona per a pintar (tauler)
screen = pygame.display.set_mode((Globals.screen_width, Globals.screen_height))
tauler = pygame.Surface((Globals.screen_width, Globals.screen_height))

# Text de la finestra
pygame.display.set_caption("El joc de la serp")

# Configurar la repetición de teclas
pygame.key.set_repeat(1, 50)

#Imatges dels elements
serp_img = pygame.image.load("./imatges/cap.png")
serp_img = pygame.transform.scale(serp_img, (Globals.tile_width, Globals.tile_height))
poma_img = pygame.image.load("./imatges/poma.png")
poma_img = pygame.transform.scale(poma_img, (Globals.tile_width, Globals.tile_height)) 
cua_img = pygame.image.load("./imatges/cua.png")
cua_img = pygame.transform.scale(cua_img, (Globals.tile_width, Globals.tile_height)) 

# Propietats de la sep
serp_x = Globals.grid_rows//3
serp_y = Globals.grid_columns//2
serp_direccio = [1,0]

# Propietats de la cua
serp_cua = [] 

# Propietats de la poma
poma_x=randrange(Globals.grid_rows)
poma_y=randrange(Globals.grid_columns)

# Pantalla inicial del joc
font = pygame.font.SysFont(None, 36)
txtTitol = font.render('Press key to starting', True, (255, 255, 255))
rect = txtTitol.get_rect(center=screen.get_rect().center)
screen.fill((0, 0, 0)) 
screen.blit(txtTitol, rect)
while estat=="init":
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()        
        elif evento.type == pygame.KEYDOWN:
            estat="playing"
    pygame.display.flip()

            
# Bucle principal del joc
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
        #modificar la posció de la poma
        poma_x=randrange(Globals.grid_rows)
        poma_y=randrange(Globals.grid_columns)
        #afegir un tros de cua a la serp
        serp_cua.append([0,0])
        #en col·lissionar amb la poma incrementar el punts i incrementar la velocitat del joc
        punts=punts+1
        Globals.FPS=Globals.FPS+Globals.incrFPS

    # moure el cap
    pos_x = serp_x
    pos_y = serp_y
    serp_x=serp_x+serp_direccio[0]
    serp_y=serp_y+serp_direccio[1]

    # moure la cua
    for num in range(len(serp_cua)-1,-1,-1):
        if num>0:
            serp_cua[num][0]=serp_cua[num-1][0]
            serp_cua[num][1]=serp_cua[num-1][1]
        else:
            serp_cua[0][0]=pos_x
            serp_cua[0][1]=pos_y

    # final de joc    
    if serp_x<0 or serp_x>=Globals.grid_rows or serp_y<0 or serp_y>=Globals.grid_columns:
        estat="end"

    ##########
    # render #
    ##########

    #pintar el fons de blanc
    tauler.fill((255, 255, 255)) 

    #pintar la poma
    tauler.blit(poma_img, (poma_x*Globals.tile_width, poma_y*Globals.tile_height)) 

    #pintar el cap de la serp
    tauler.blit(serp_img, (serp_x*Globals.tile_width, serp_y*Globals.tile_height)) 

    #pintar la cua
    for cua in serp_cua:
        tauler.blit(cua_img, (cua[0]*Globals.tile_width, cua[1]*Globals.tile_height))
        print(cua)

    # Aplicar el doble buffering        
    screen.blit(tauler, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(Globals.FPS)

# Pantalla final del joc
font = pygame.font.SysFont(None, 36)
txtTitol = font.render(f'Has aconseguit {punts} pomes.', True, (255, 255, 255))
rect = txtTitol.get_rect(center=screen.get_rect().center)
screen.fill((0, 0, 0)) 
screen.blit(txtTitol, rect)
while estat=="end":
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()        
        elif evento.type == pygame.KEYDOWN:
            estat="exit"
    pygame.display.flip()