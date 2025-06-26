import pygame.font 

class Botao:
    """"Classe para criar botões para o jogo"""
    def __init__(self, ai_jogo, texto):
        """Inicializa os atributos do botão"""
        self.tela = ai_jogo.tela
        self.tela_rect = self.tela.get_rect()

        # Define as dimensões e propriedades do botão
        self.largura = 200
        self.altura = 50
        self.cor = (0, 255, 0)
        self.texto = texto
        self.texto_cor = (255, 255, 255)    
        self.fonte = pygame.font.SysFont(None, 48)

        #  Cria o retângulo do botão e centraliza na tela
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.center = self.tela_rect.center

        # A mensagem do botão 
        self._preparar_texto(texto)

    def _preparar_texto(self, texto):
        """Transforma o texto em uma imagem renderizada e centraliza no botão"""
        self.texto_imagem = self.fonte.render(texto, True, self.texto_cor, self.cor)
        self.texto_rect = self.texto_imagem.get_rect()
        self.texto_rect.center = self.rect.center   


    def desenhar(self):
        """Desenha o botão na tela"""
        self.tela.fill(self.cor, self.rect) 
        self.tela.blit(self.texto_imagem, self.texto_rect)
