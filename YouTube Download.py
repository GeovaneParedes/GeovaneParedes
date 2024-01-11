'''Este pequeno projeto, baixar videos do youtube'''
from pytube import YouTube 
from time import sleep
link = input('Qual o link do video? ')
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download() '''Aqui ele ja esta processando o video'''
print('Começando download....')
sleep(2)#Aqui e dada uma pausa
print('Acabou...aproveite o video!')
