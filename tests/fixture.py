"""Fixture available to test methods"""

from os import chdir
import pygame


def fixture():
    chdir('..')
    pygame.init()
    pygame.display.set_mode()
