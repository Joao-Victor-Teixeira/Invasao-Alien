import pygame.font
from pygame.sprite import Group
from nave import Nave

class Placar:
    """Class to represent a pontuação do jogo."""

    def __init__(self, ai_jogo):
        """Inicializa os atributos de pontuação."""
        self.ai_jogo = ai_jogo
        # Referências para a tela e configurações do jogo
        self.tela = ai_jogo.tela
        self.tela_rect = self.tela.get_rect()
        self.configuracoes = ai_jogo.configuracoes  
        self.estatisticas = ai_jogo.estatisticas

        #cofigurações da fonte
        self.cor_texto = (30, 30, 30)
        self.fonte = pygame.font.SysFont(None, 48)

        # Prepara a imagem da pontuação inicial
        self.preparar_pontuacao()
        self.preparar_pontuacao_maxima()
        self.preparar_nivel()


    def preparar_pontuacao(self):
        """Transforma a pontuação em uma imagem renderizada."""
        pontuacao_str = str(self.estatisticas.pontuacao)
        self.imagem_pontuacao = self.fonte.render(pontuacao_str, True, self.cor_texto, self.configuracoes.bg_color)
        
        # Centraliza a pontuação na parte superior da tela
        self.rect_pontuacao = self.imagem_pontuacao.get_rect()
        self.rect_pontuacao.right = self.tela_rect.right - 20
        self.rect_pontuacao.top = 20


    def preparar_pontuacao_maxima(self):
        """Transforma a pontuação máxima em uma imagem renderizada."""
        pontuacao_max_str = f"Recorde: {self.estatisticas.pontuacao_maxima}"
        self.imagem_pontuacao_maxima = self.fonte.render(pontuacao_max_str, True, self.cor_texto, self.configuracoes.bg_color)
        
        # Posiciona a pontuação máxima abaixo da pontuação atual
        self.rect_pontuacao_maxima = self.imagem_pontuacao_maxima.get_rect()
        self.rect_pontuacao_maxima.right = self.tela_rect.right - 20
        self.rect_pontuacao_maxima.top = self.rect_pontuacao.bottom + 10


    def preparar_nivel(self):
        """Transforma o nível atual em uma imagem renderizada."""
        nivel_str = f"Nível: {self.estatisticas.nivel}"
        self.imagem_nivel = self.fonte.render(nivel_str, True, self.cor_texto, self.configuracoes.bg_color)
        
        # Posiciona o nível abaixo da pontuação máxima
        self.rect_nivel = self.imagem_nivel.get_rect()
        self.rect_nivel.right = self.tela_rect.right - 20
        self.rect_nivel.top = self.rect_pontuacao_maxima.bottom + 10


    def mostrar_placar(self):
        """Desenha a pontuação e a pontuação máxima na tela."""
        self.tela.blit(self.imagem_pontuacao, self.rect_pontuacao)
        self.tela.blit(self.imagem_pontuacao_maxima, self.rect_pontuacao_maxima)

    def mostrar_naves(self):
        """Mostra as naves restantes na tela."""
        self.naves = pygame.sprite.Group()
        for numero_nave in range(self.estatisticas.naves_restantes):
            nave = Nave(self.ai_jogo)
            nave.rect.x = 10 + numero_nave * nave.rect.width
            nave.rect.y = 10
            self.naves.add(nave)
        self.naves.draw(self.tela)


    def atualizar_placar(self):
        """Atualiza a pontuação e a pontuação máxima na tela."""
        self.preparar_pontuacao()
        self.preparar_pontuacao_maxima()
        self.mostrar_placar()
        self.mostrar_naves()

    def mostrar_nivel(self):
        """Desenha o nível atual na tela."""
        self.tela.blit(self.imagem_nivel, self.rect_nivel)