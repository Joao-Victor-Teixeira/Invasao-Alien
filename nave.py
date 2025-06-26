import pygame
from pygame.sprite import Sprite

class Nave(Sprite):  # Herda de Sprite!
    """Classe para cuidar da nave"""

    def __init__(self, ai_jogo):
        """Inicializa a nave e define sua posição inicial"""
        super().__init__()
        
        self.tela = ai_jogo.tela
        self.configuracoes = ai_jogo.configuracoes
        self.image = pygame.image.load('imagens/rocket.png')
        self.rect = self.image.get_rect()
        self.tela_rect = self.tela.get_rect()

        # Começa cada nova nave na parte inferior central da tela
        self.rect.midbottom = self.tela_rect.midbottom
        self.x = float(self.rect.x)

        # Flags de movimento
        self.movendo_direita = False
        self.movendo_esquerda = False

    def atualize_movimento(self):
        """Atualiza a posição da nave com base na flag de movimento"""
        if self.movendo_direita and self.rect.right < self.tela_rect.right:
            self.x += self.configuracoes.velocidade_nave
        if self.movendo_esquerda and self.rect.left > 0:
            self.x -= self.configuracoes.velocidade_nave
        self.rect.x = self.x

    def blitme(self):
        """Desenha a nave na sua localização"""
        self.tela.blit(self.image, self.rect)

    def centralizar_nave(self):
        """Centraliza a nave na parte inferior da tela"""
        self.rect.midbottom = self.tela_rect.midbottom
        self.x = float(self.rect.x)