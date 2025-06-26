class EstatisticasJogo:
   """Armazena dados estatísticos do jogo."""

   def __init__(self, ai_game):
      self.limite_naves = ai_game.configuracoes.limite_nave
      self.naves_restantes = self.limite_naves
      self.pontuacao = 0
      self.pontuacao_maxima = self.carregar_pontuacao_maxima()
      self.nivel = 1  # Adicionado atributo nível

   def iniciar_estatisticas(self):
      """Reinicia as estatísticas do jogo."""
      self.naves_restantes = self.limite_naves
      self.pontuacao = 0
      self.nivel = 1  # Reinicia o nível se desejar

   def carregar_pontuacao_maxima(self):
      """Carrega a pontuação máxima a partir de um arquivo."""
      try:
         with open("pontuacao_maxima.txt", "r") as f:
            return int(f.read())
      except:
         return 0

   def salvar_pontuacao_maxima(self):
      """Salva a pontuação máxima em um arquivo."""
      with open("pontuacao_maxima.txt", "w") as f:
         f.write(str(self.pontuacao_maxima))
