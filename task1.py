import pygame
import PIL
import cv2
import moviepy.editor as mp
import pydub
import tkinter as tk 
from importlib.metadata import version
import pkg_resources

def check_installation():
    try:
        pygame.init()
        print("✅ Pygame version:", pygame.__version__)
        print("✅ Pillow version:", PIL.__version__)
        print("✅ OpenCV version:", cv2.__version__)
        print("✅ MoviePy version:", version("moviepy"))
        print("✅ Pydub version:", pkg_resources.get_distribution("pydub").version)
        print("✅ Tkinter is installed and working!")
    except Exception as e:
        print("❌ Error:", e)

check_installation()
