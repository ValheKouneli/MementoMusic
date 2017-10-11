import pygame
#import time

def getSounds() :
    pygame.mixer.pre_init(48000, -16, 2, 2048)
    pygame.init()

    notes = ['c_', 'cs', 'd_', 'ds', 'e_', 'f_', 'fs', 'g_', 'gs', 'a_', 'as', 'b_']
    sounds = []

    #from 4 to 5, other are too low/high
    for i in range(1) :
        for note in notes :
            filename = "beeps/" + note + str(i+4) + ".wav"

            sound = pygame.mixer.Sound(filename)
            sounds.append(sound)

            #channel = sound.play()
            #while channel.get_busy() :
                #pygame.time.delay(100)
            #time.sleep(3)
    
    return sounds
