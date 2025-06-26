class Configuracoes:
    """Classe para armazenar as configurações do jogo"""

    def __init__(self):
        """Inicializa as configurções do jogo"""
        #Configurações da tela
        self.largura_tela = 1200
        self.altua_tela = 800
        self.bg_color = (230, 230, 230)
        
        #Configurações da nave
        self.velocidade_nave = 1.0   
        self.limite_nave = 3
        #Configurações dos projéteis
        self.velocidade_tiro = 2.0
        self.largura_tiro = 3
        self.altura_tiro = 15
        self.cor_tiro = (60, 60, 60)
        self.limite_tiros = 30
        #Configurações dos aliens
        self.velocidade_alien = 1.0
        self.vel_queda_frota = 10
        # direção da frota de 1 representa direita e -1 esquerda
        self.direcao_frota = 1

        # Aumenta a velocidade do jogo
        self.fator_aumento_velocidade = 1.1  # Fator de aceleração

        self.iniciar_configuracoes_dinamicas()


    def iniciar_configuracoes_dinamicas(self):
        """Inicializa as configurações que mudam durante o jogo"""
        self.velocidade_nave = 1.5
        self.velocidade_alien = 1.0
        self.vel_queda_frota = 10
        self.velocidade_tiro = 2.0
        self.limite_tiros = 30
        self.direcao_frota = 1.0

        # Direção da frota de 1 representa direita e -1 esquerda
        self.direcao_frota = 1    

        #Configurações de pontuação
        self.pontos_por_alien = 50

    def aumentar_velocidade(self):
        """Aumenta as velocidades do jogo."""
        self.velocidade_nave *= self.fator_aumento_velocidade
        self.velocidade_tiro *= self.fator_aumento_velocidade
        self.velocidade_alien *= self.fator_aumento_velocidade