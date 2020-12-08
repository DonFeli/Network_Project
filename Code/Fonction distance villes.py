#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
Source pour le calcul:
https://geodesie.ign.fr/contenu/fichiers/Distance_longitude_latitude.pdf
"""
 
from math import sin, cos, acos, pi
 
#############################################################################
def deg2rad(dd):
    """Convertit un angle "degrés décimaux" en "radians"
    """
    return dd/180*pi
 #############################################################################
def distanceGPS(latA, longA, latB, longB):
    """Retourne la distance en mètres entre les 2 points A et B connus grâce à
       leurs coordonnées GPS (en radians).
    """
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378137
    # angle en radians entre les 2 points
    S = acos(sin(latA)*sin(latB) + cos(latA)*cos(latB)*cos(abs(longB-longA)))
    # distance entre les 2 points, comptée sur un arc de grand cercle
    return S*RT
 
#############################################################################
if __name__ == "__main__":
 
    # cooordonnées GPS en radians du 1er point (ici, mairie de Tours)
    latA = deg2rad(47.390668) # Nord
    longA = deg2rad(0.689319) # Est
 
    # cooordonnées GPS en radians du 2ème point (ici, mairie de Limoges)
    latB = deg2rad(45.826516) # Nord
    longB = deg2rad(1.260290) # Est
 
    dist = distanceGPS(latA, longA, latB, longB)
    print(int(dist))