bl_info = {
    "name": "Add Camera Rigs",
    "author": "Wayne Dixon, Brian Raschko, Kris Wittig",
    "version": (1, 4),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Camera > Dolly or Crane Rig",
    "description": "Adds a Camera Rig with UI",
    "tracker_url": "https://github.com/waylow/add_camera_rigs/issues",
    "category": "Camera",
}

import bpy
import os

from . import build_rigs
from . import operators
from . import ui_panels
from . import prefs
from . import composition_guides_menu

# =========================================================================
# Registration:
# =========================================================================

def register():
    build_rigs.register()
    operators.register()
    ui_panels.register()
    prefs.register()
    composition_guides_menu.register()


def unregister():
    build_rigs.unregister()
    operators.unregister()
    ui_panels.unregister()
    prefs.unregister()
    composition_guides_menu.unregister()


if __name__ == "__main__":
    register()
