class Programa: 
    def __init__(self, nome, ano):
        self.ano = ano
        self._nome = nome.title()
        self._likes = 0
        
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1 

    @property
    def nome(self):
        return self._nome
    
    @nome.setter 
    def nome(self, nome):
        self._nome = nome 

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'Nome: {self.nome }- {self.duracao} min de duração - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

class  Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    def __getitem__(self, item):
        return self._programas[item]

    @property 
    def listagem(self):
        return self._programas
    
Game_of_Thrones = Serie('Game of Thrones', 2011, 8)
O_culpado = Filme('O culpado', 2021, 91)
Breaking_bad = Serie('Breaking bad', 2013, 5)
Por_Lugares_incriveis = Filme('Por Lugares incriveis', 2020, 108)


Game_of_Thrones.dar_likes()
Game_of_Thrones.dar_likes()
Game_of_Thrones.dar_likes()
Game_of_Thrones.dar_likes()
Game_of_Thrones.dar_likes()
Game_of_Thrones.dar_likes()
Game_of_Thrones.dar_likes()
Game_of_Thrones.dar_likes()
O_culpado.dar_likes()
O_culpado.dar_likes()
O_culpado.dar_likes()
Breaking_bad.dar_likes()
Breaking_bad.dar_likes()
Breaking_bad.dar_likes()
Breaking_bad.dar_likes()
Breaking_bad.dar_likes()
Breaking_bad.dar_likes()
Por_Lugares_incriveis.dar_likes()





listinha = [Game_of_Thrones, O_culpado, Breaking_bad, Por_Lugares_incriveis]
Minha_playlist = Playlist('Minha Playlist: ', listinha)
print('_'*60)
print('Playlist Rodrigo')
print('*'*60)
for Programa in Minha_playlist:
    print(Programa)
print('*'*60)
print('Tamanho da playlist: ', len(listinha))
print('_'*60)



# https://www.youtube.com/watch?v=Opi5HH3sZz4