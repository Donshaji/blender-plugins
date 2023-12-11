import bpy

selected_object = bpy.context.active_object

voxel_modifier = selected_object.modifiers.new(name="VoxelRemesh", type='VOXEL')
voxel_modifier.voxel_size = 0.1

bpy.ops.object.modifier_apply({"object": selected_object}, modifier="VoxelRemesh")

bpy.context.view_layer.update()

print("Voxelization complete!")