import sys
from time import sleep
import pygame
from config import Configuracoes
from estatisticas_jogo import EstatisticasJogo
from placar import Placar
from botao import Botao
from nave import Nave
from tiro import Tiro
from alien import Alien

class InvasaoAlienigena:
    """Classe para gerenciar ativos e comportamentos do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria seus recursos"""
        pygame.init()
        self.relogio = pygame.time.Clock()
        self.configuracoes = Configuracoes()
        
        # Modo fullscreen
        self.tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.configuracoes.largura_tela = self.tela.get_rect().width
        self.configuracoes.altura_tela = self.tela.get_rect().height
        pygame.display.set_caption("Invasão Alienígena")
        
        # Cria uma instância de EstatisticasJogo para acompanhar o estado do jogo
        self.estatisticas = EstatisticasJogo(self)
        self.placar = Placar(self)
        self.nave = Nave(self)
        self.tiros = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._criar_frota()

        #inicializa a invasão alienígena em um estado inativo
        self.jogo_ativo = False  # Começa inativo
        # cria um botão para iniciar o jogo
        self.botao_jogar = Botao(self, "Jogar")
        self.pausado = False

    def executar_jogo(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._verificar_eventos()
            if self.jogo_ativo and not self.pausado:
                self.nave.atualize_movimento()
                self.tiros.update()
                self._update_aliens()   
                self._atualizar_tiros()
            self._atualizar_tela()
            self.relogio.tick(60)     

    def _criar_frota(self):
        """Cria a frota de aliens"""
        alien = Alien(self)
        largura_alien, altura_alien = alien.rect.size

        atual_x, atual_y = largura_alien, altura_alien 
        while atual_y < (self.configuracoes.altura_tela - 3 * altura_alien):  
            while atual_x < self.configuracoes.largura_tela - 2 * largura_alien:
                self._criar_alien(atual_x, atual_y)
                atual_x += 2 * largura_alien

            # Termina uma fileira; redefine a posição x e aumenta a y
            atual_x = largura_alien
            atual_y += 2 * altura_alien    

    def _criar_alien(self, posicao_x, posicao_y):
        """Cria um alien e o posiciona na fileira"""
        novo_alien = Alien(self)
        novo_alien.x = posicao_x
        novo_alien.rect.x = posicao_x
        novo_alien.rect.y = posicao_y
        self.aliens.add(novo_alien)

    def _verficar_bordas_frota(self):
        """Responde se algum alien atingiu a borda da tela"""
        for alien in self.aliens.sprites():
            if alien.verifique_bordas():
                self._mudar_direcao_frota()
                break

    def _mudar_direcao_frota(self):
        """Faz a frota de aliens descer e mudar de direção"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.configuracoes.vel_queda_frota
        self.configuracoes.direcao_frota *= -1        

    def _verificar_eventos(self):
        """Responde a teclas pressionadas e a eventos de mouse"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                self._verificar_teclas_pressionadas(evento)
            elif evento.type == pygame.KEYUP:
                self._verificar_teclas_soltas(evento)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._checar_botao_jogar(mouse_pos)

    def _checar_botao_jogar(self, mouse_pos):
        """Inicia o jogo ao clicar no botão 'Jogar'"""
        botao_ativo = self.botao_jogar.rect.collidepoint(mouse_pos)
        # Verifica se o botão de jogar foi clicado e se o jogo não está ativo       
        if botao_ativo and not self.jogo_ativo:
            # Redefine as configurações dinâmicas do jogo
            self.configuracoes.iniciar_configuracoes_dinamicas()
            # Reinicia as estatísticas do jogo
            self.estatisticas.iniciar_estatisticas()
            # Muda o estado do jogo para ativo
            self.jogo_ativo = True
            # Redefine o número de naves restantes
            self.estatisticas.naves_restantes = self.estatisticas.limite_naves
           # Redefine as estatísticas do jogo
            self.estatisticas.iniciar_estatisticas()
            self.placar.preparar_pontuacao()
            # Reinicia o jogo
            self.jogo_ativo = True
            self.estatisticas.naves_restantes = self.estatisticas.limite_naves
           # Descarta os tiros e os aliens 
            self.tiros.empty()
            self.aliens.empty()
           # Cria uma nova frota de aliens e centraliza a nave 
            self._criar_frota()
            self.nave.centralizar_nave()
            pygame.mouse.set_visible(False)

    def _verificar_teclas_pressionadas(self, evento):
        """Responde às teclas pressionadas"""
        if evento.key == pygame.K_RIGHT:
            self.nave.movendo_direita = True
        elif evento.key == pygame.K_LEFT:
            self.nave.movendo_esquerda = True  
        elif evento.key == pygame.K_q:
            sys.exit()
        elif evento.key == pygame.K_p:  # Tecla P para pausar/despausar
            self.pausado = not self.pausado
        elif evento.key == pygame.K_SPACE and self.jogo_ativo and not self.pausado:
            self._atirar()

    def _verificar_teclas_soltas(self, evento):
        """Responde às teclas soltas"""
        if evento.key == pygame.K_RIGHT:
            self.nave.movendo_direita = False 
        elif evento.key == pygame.K_LEFT:
            self.nave.movendo_esquerda = False  

    def _atirar(self):
        """Cria um novo projétil e adiciona ao grupo de projéteis""" 
        if len(self.tiros) < self.configuracoes.limite_tiros:
            novo_tiro = Tiro(self)
            self.tiros.add(novo_tiro)   

    def _atualizar_tiros(self):
        """Atualiza a posição dos tiros e elimina os que saíram da tela"""
        # Descarta os projéteis que saíram da tela
        for tiro in self.tiros.copy():
            if tiro.rect.bottom <= 0:
               self.tiros.remove(tiro)
        self._verifar_tiros_em_aliens()       
 
    def _verifar_tiros_em_aliens(self):
        """Verifica se algum tiro atingiu um alien e atualiza a frota"""
        print(len(self.tiros))  # Debug: mostra a quantidade de tiros na tela   
        colisoes = pygame.sprite.groupcollide(self.tiros, self.aliens, True, True)
        if colisoes:
            for tiros, aliens in colisoes.items():
                self.estatisticas.pontuacao += self.configuracoes.pontos_por_alien * len(aliens)
            self.placar.preparar_pontuacao()
        # Só aumenta a velocidade e cria nova frota quando todos os aliens acabarem!
        if not self.aliens:
            self.tiros.empty()
            self._criar_frota()
            self.configuracoes.aumentar_velocidade()

    def _update_aliens(self):
        """Atualiza as posições dos aliens"""
        self._verficar_bordas_frota()
        self.aliens.update()

        #Detecta colisões entre os aliens e a nave
        if pygame.sprite.spritecollideany(self.nave, self.aliens):
            self._naves_atingidas()

    def _naves_atingidas(self):
        """Responde à nave sendo atingida por um alien"""
        self.estatisticas.naves_restantes -= 1
        # Descarta os tiros restantes e reinicia a frota
        self.tiros.empty()
        self.aliens.empty()

        # Cria uma nova frota e centraliza a nave
        self._criar_frota()
        self.nave.centralizar_nave()

        # Se não houver mais naves, encerra o jogo e mostra o cursor
        if self.estatisticas.naves_restantes <= 0:
            self.jogo_ativo = False
            pygame.mouse.set_visible(True)

        # Pausa o jogo por um curto período
        sleep(1.0)

    def _atualizar_tela(self):
        """Atualiza as imagens na tela e muda para a nova tela"""
        self.tela.fill(self.configuracoes.bg_color)
        for tiro in self.tiros.sprites():
            tiro.desenhar_tiro()
        self.nave.blitme()
        self.aliens.draw(self.tela)
        self.placar.mostrar_placar()         # Exibe pontuação e recorde
        self.placar.mostrar_naves()          # Exibe as naves restantes (superior esquerdo)
        self.placar.mostrar_nivel()          # Exibe o nível atual (onde preferir)
        if not self.jogo_ativo:
            self.botao_jogar.desenhar()
            pygame.mouse.set_visible(True)
        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e executa o jogo
    ai = InvasaoAlienigena()
    ai.executar_jogo()
