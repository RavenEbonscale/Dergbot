import cv2
from discord.ext import commands
import numpy as np


class image_manuplation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot





def setup(bot):
    bot.add_cog(image_manuplation(bot))