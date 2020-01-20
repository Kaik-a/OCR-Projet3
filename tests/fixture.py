"""Fixture available to test methods"""

from os import chdir
import pygame


def fixture():
    """Set up environment to test"""
    chdir('..')
    pygame.init()
    pygame.display.set_mode()
