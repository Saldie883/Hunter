import pygame
from argbuilder import args
from model import Model
from view import View

pygame.init()
screen = pygame.display.set_mode(args.res)
model = Model(
    args.wsize,
    hares=args.hares,
    wolves=args.wolves,
    deer_families=args.deerflocks)

v = View(screen, model, args.camscale)
v.start()
