import pygame
from pygame.sprite import Sprite

class Tiro(Sprite):
    """Classe para gerenciar os projéteis disparados da nave"""

    def __init__(self, ai_jogo):
        """Cria um objeto 'tiro' na posição atual da nave"""
        super().__init__()
        self.tela = ai_jogo.tela
        self.configuracoes = ai_jogo.configuracoes
        self.cor = self.configuracoes.cor_tiro

        # Cria um tiro retangular em (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, self.configuracoes.largura_tiro,
                               self.configuracoes.altura_tiro)
        self.rect.midtop = ai_jogo.nave.rect.midtop

        # Armazena a posição do projétil como um float para movimento suave
        self.y = float(self.rect.y)

    def update(self):
        """Move o projétil para cima na tela"""
        self.y -= self.configuracoes.velocidade_tiro
        self.rect.y = self.y

        # Remove o tiro quando sair da tela (topo)
        if self.rect.bottom < 0:
            self.kill()

    def desenhar_tiro(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.tela, self.cor, self.rect)
