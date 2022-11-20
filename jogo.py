import os 
import pygame 
import sys
from pygame.locals import *

os.system ("cls")
print("Jogando Breackout")

def gerador_de_blocos():
	for fileira in range(fileiras):
		for coluna in range(colunas):
			x = ((bastao_esquerda * coluna) + bastao_esquerda) + (largura_dos_blocos * coluna)
			y = ((topo_bastao * fileira) + topo_bastao) + (altura_dos_blocos * fileira)
			blocos = pygame.Rect(x,y,largura_dos_blocos,altura_dos_blocos)
			listaDeBlocos.append(blocos)

def desenhoDosBlocos(blocos):
	for blocos in blocos:
		pygame.draw.rect(tela, cor, blocos)

def animacaoDaBola():
	global posicao_y_bola, posicao_x_bola, tempo_perdido, pontuacao
	bola.x += posicao_x_bola
	bola.y += posicao_y_bola

	if bola.left <= 0 or bola.right >= largura:
		posicao_x_bola = - posicao_x_bola

	if bola.top <= 0:
		posicao_y_bola = - posicao_y_bola

	if bola.bottom >= altura:
		tempo_perdido = pygame.time.get_ticks()

	if bola.colliderect(bastao):
		posicao_y_bola = - posicao_y_bola

	for blocos in listaDeBlocos: #hitbox do jogo
		if bola.colliderect(blocos):
			posicao_y_bola = - posicao_y_bola
			listaDeBlocos.remove(blocos)
			pontuacao += 1

def redefinir():
	global posicao_x_bola, posicao_y_bola, tempo_perdido, pontuacao
	bola.x = largura//2-10
	bola.y = altura-40
	bastao.x = largura//2-150//2
	bastao.y = altura-20
	listaDeBlocos.clear()
	gerador_de_blocos()
	pontuacao = 0
	

	tempo_atual = pygame.time.get_ticks()

	if tempo_atual - tempo_perdido < 1000:
		num_three = fonte_conometro.render("3", True, cor)
		num_three_rect = num_three.get_rect(center=(largura//2, altura//2+10))
		tela.blit(num_three, num_three_rect)

	elif 1000 < tempo_atual - tempo_perdido < 2000:
		num_two = fonte_conometro.render("2", True, cor)
		num_two_rect = num_two.get_rect(center=(largura//2, altura//2+10))
		tela.blit(num_two, num_two_rect)

	elif 2000 <tempo_atual - tempo_perdido < 3000:
		num_one = fonte_conometro.render("1", True, cor)
		num_one_rect = num_one.get_rect(center=(largura//2, altura//2+10))
		tela.blit(num_one, num_one_rect)

	if tempo_atual - tempo_perdido >= 3000:
		posicao_x_bola = - posicao_x_bola
		posicao_y_bola = - posicao_y_bola
		tempo_perdido = None

def escritaPontuacao():
	pontuacao_text = fonte_pontuacao.render(f"{pontuacao}",True,cor)
	pontuacao_rect = pontuacao_text.get_rect(center= (20,altura-20))
	tela.blit(pontuacao_text, pontuacao_rect)

def win():
	if len(listaDeBlocos) == 0:
		tela.fill(cor_do_fundo)
		posicao_y_bola, posicao_x_bola = 0,0
		won_text = fonte_conometro.render("You won !!",True,cor)
		won_rect = won_text.get_rect(center = (largura//2, altura//2))
		tela.blit(won_text, won_rect)

pygame.init()
largura = 800 #tupla
altura = 650 #tupla
tela = pygame.display.set_mode((largura, altura)) #tupla
pygame.display.set_caption("2D Breakout")
tempo = pygame.time.Clock()

cor_do_fundo = pygame.Color("#2b2b2b")
cor = pygame.Color("#ff7259")
pontuacao = 0

bastao = pygame.Rect(largura//2-150//2, altura-20, 150, 10)
direcao_x_bastao = 0

bola = pygame.Rect(largura//2-10,altura-40,20,20)
posicao_x_bola = 5
posicao_y_bola = -5

fileiras = 4
colunas = 5
bastao_esquerda = 10
topo_bastao = 10
largura_dos_blocos = 147
altura_dos_blocos = 40
listaDeBlocos = []
gerador_de_blocos()

tempo_perdido = None #escritas do jogo
fonte_conometro = pygame.font.SysFont("monospace", 70)
fonte_pontuacao = pygame.font.SysFont("monospace", 35)

while True:
	tempo.tick(100)
	for event in pygame.event.get():
		if event.type == QUIT:
			print(pontuacao)
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:#mover o bastao
			if event.key == K_LEFT:
				direcao_x_bastao = -5

			if event.key == K_RIGHT:
				direcao_x_bastao = 5

		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				direcao_x_bastao = 0 
