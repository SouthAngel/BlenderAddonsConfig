import bpy
from bpy.types import Menu

# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)


class VIEW3D_PIE_select_mode(Menu):
    bl_idname = "pie.select"
    # label is displayed at the center of the pie menu.
    bl_label = "Select Mode"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator_enum("mesh.select_mode", "type")
        prop = pie.operator("wm.context_set_value",
                        text="Vertex & Edge & Face Select",
                        icon='SNAP_VOLUME')
        prop.value = "(True, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"


addon_keymaps = []


def register():
    bpy.utils.register_class(VIEW3D_PIE_select_mode)
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'C', 'PRESS')
        kmi.properties.name = VIEW3D_PIE_select_mode.bl_idname
        addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_class(VIEW3D_PIE_select_mode)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()
