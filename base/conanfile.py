from conans import ConanFile
from base_recipe import BaseConanFile


class CommonADASConanRecipes(ConanFile):
    name = 'base_recipe'
    description = 'Base recipe'
    exports = 'base_recipe.py'
    version = '0.1.0'
