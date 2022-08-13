import pygame
import random
import images

def pattack(pchealth):
    pchealth += -20 - (random.random() * 10) // 1
    if pchealth <= 0:
        pchealth = 0


def pheal(playerhealth):
    playerhealth += 20 + (random.random() * 10) // 1
    if playerhealth >= 100:
        playerhealth = 100


def pcattack(playerhealth):
    playerhealth += -20 - (random.random() * 10) // 1
    if playerhealth <= 0:
        playerhealth = 0


def pcheal(pchealth):
    pchealth += 20 + (random.random() * 10) // 1
    if pchealth >= 100:
        pchealth = 100

def battle():
