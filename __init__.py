# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_addon_info = {
    "name": "K2-Silverlight Mesh/Clip",
    "author": "Anton Romanov",
    "version": (1, 0),
    "blender": (2, 5, 3),
    "api": 31667,
    "location": "File > Import-Export > K2 model/clip ",
    "description": "Import K2/Silverlight Model/Clip (.model/.clip formats)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}

if "bpy" in locals():
    import imp
    imp.reload(k2_import)
    #imp.reload(export_raw)
else:
    from . import k2_import
    #from . import export_raw


import bpy

def menu_import(self, context):
    self.layout.operator(k2_import.K2Importer.bl_idname, text="K2/Silverlight Model/clip (.model/.clip formats)").filepath = "*.model|*.clip"


#def menu_export(self, context):
#    import os
#    default_path = os.path.splitext(bpy.data.filepath)[0] + ".raw"
#    self.layout.operator(export_raw.RawExporter.bl_idname, text="Raw Faces (.raw)").filepath = default_path


def register():
    bpy.types.INFO_MT_file_import.append(menu_import)
#    bpy.types.INFO_MT_file_export.append(menu_export)

def unregister():
    bpy.types.INFO_MT_file_import.remove(menu_import)
#    bpy.types.INFO_MT_file_export.remove(menu_export)

if __name__ == "__main__":
    register()