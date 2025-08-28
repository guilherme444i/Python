import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = IMAGEM_CANO
        self.CANO_BASE = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_base = self.altura - self.CANO_TOPO.get_height()
        self.pos_topo = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        mask_passaro = passaro.get_mask()
        mask_topo = pygame.mask.from_surface(self.CANO_TOPO)
        mask_base = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        ponto_topo = mask_passaro.overlap(mask_topo, distancia_topo)
        ponto_base = mask_passaro.overlap(mask_base, distancia_base)

        if ponto_base or ponto_topo:
            return True
        return False

class Passaro:
    IMAGENS = IMAGEM_PASSARO
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMAGENS[0]

    def pular(self):
        self.velocidade = -8.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # Calcula o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # Ajusta o ângulo do pássaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # Escolhe qual imagem do pássaro mostrar
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMAGENS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMAGENS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMAGENS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMAGENS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMAGENS[0]
            self.contagem_imagem = 0

        # Se o pássaro estiver caindo, fixa a imagem para não bater as asas
        if self.angulo <= -80:
            self.imagem = self.IMAGENS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * 2

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        centro = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=centro)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))

#funções do sistema
def desenhar_tela(tela, passaros, canos, chao, pontos):
    #Desenhando o fundo da tela
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    #desenhando os pássaros
    for passaro in passaros:
        passaro.desenhar(tela)
    #desenhando os canos
    for cano in canos:
        cano.desenhar(tela)
    #desenhando o texto de pontuação
    texto = FONTE_PONTOS.render(f'Pontuação:{pontos}', 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    #desenhando o chão
    chao.desenhar(tela)
    #atualizando a tela
    pygame.display.update()

def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos= [Cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    #loop do jogo

    rodando = True
    while rodando:
        relogio.tick(29)
        #interação com o usúario
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()
                if evento.type == pygame.K_UP:
                    for passaro in passaros:
                        passaro.pular()
                

        #Mover coisas
        for passaro in passaros:
            passaro.mover()
            chao.mover()

            adicionar_cano = False
            remover_canos = []
            for cano in canos:
                for i, passaro in enumerate(passaros):
                    if cano.colidir(passaro):
                        passaro.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
                cano.mover()
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)

            if adicionar_cano:
                pontos += 1
                canos.append(Cano(600))

            for cano in remover_canos:
                canos.remove(cano)

            for i, passaro in enumerate(passaros):
                if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                    passaro.pop(i)

            desenhar_tela(tela, passaros, canos, chao, pontos)
if __name__ == "__main__":
    main()
