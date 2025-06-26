import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe que representa uma única nave da frota"""

    def __init__(self, ai_jogo):
        """Inicializa a nave alien e define sua posição inicial"""
        super().__init__()
        self.tela = ai_jogo.tela
        self.configuracoes = ai_jogo.configuracoes

        # Carrega a imagem da nave e define seu atributo rect
        self.image = pygame.image.load('imagens/saucer.png')
        self.rect = self.image.get_rect()

        # Inicia cada alien novo perto do canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do alien
        self.x = float(self.rect.x)


    def update(self):
        """Move o alien para a direita ou esquerda""" 
        self.x += self.configuracoes.velocidade_alien * self.configuracoes.direcao_frota
        self.rect.x = self.x


    def verifique_bordas(self):
        """Verifica se o alien está na borda da tela"""
        tela_rect = self.tela.get_rect()
        if self.rect.right >= tela_rect.right or self.rect.left <= 0:
            return True
        return False
