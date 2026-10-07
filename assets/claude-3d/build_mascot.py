# build_mascot.py - the Claude mascot as a 3D model, rigged for the 18 named animations.
#
#   /Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python-exit-code 1 --python build_mascot.py
#
# Geometry is the toolkit's canonical 2D mascot (brutalist.art/runtime/remotion/src/scenes/ClaudeMascotScene.tsx):
# torso 96x60, arms 20x20, eyes 11x10, legs 11x26 (pixel units). 1 pixel unit = 1 cm, so the mascot is 0.86 m tall.
# 2D x -> 3D X (right), 2D y (down) -> 3D Z (up), depth is new: torso 48 deep, arms 20, legs 11, eyes 3 (1.5 proud of the face).
# Origin: centre of the underside of the feet (z = 0), centred on the torso. Front faces -Y (Blender's front view).
# One mesh (9 boxes, 108 triangles), one armature (9 bones), two materials. Rigid skinning: every part has weight 1.0 on its bone.
import bpy, bmesh, os, math

HERE = os.path.dirname(os.path.abspath(__file__))
U = 0.01                                    # metres per pixel unit
BODY_HEX, EYE_HEX = "#dd775b", "#000000"    # canonical colours from ClaudeMascotScene.tsx


def srgb(hex_):
    h = hex_.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return (*lin, 1.0)


def px_to_box(x0, x1, ytop, ybot, d0, d1):
    """2D rect (x0..x1, ytop..ybot measured DOWN from the top of the torso, 86 tall total) + depth d0..d1 (-Y front)
    -> world box (xmin, xmax, ymin, ymax, zmin, zmax) in metres. The 2D torso spans x 0..96, so shift by -48 to centre."""
    return ((x0 - 48) * U, (x1 - 48) * U, d0 * U, d1 * U, (86 - ybot) * U, (86 - ytop) * U)


# name, bone, material, 2D rect (x0, x1, ytop, ybot), depth (front -Y first)
PARTS = [
    ("Torso",  "Root",  "body", (0, 96, 0, 60),     (-24, 24)),
    ("ArmL",   "Arm.L", "body", (-20, 0, 20, 40),   (-10, 10)),
    ("ArmR",   "Arm.R", "body", (96, 116, 20, 40),  (-10, 10)),
    ("EyeL",   "Eye.L", "eye",  (11, 22, 10, 20),   (-25.5, -22.5)),
    ("EyeR",   "Eye.R", "eye",  (74, 85, 10, 20),   (-25.5, -22.5)),
    ("Leg1",   "Leg.1", "body", (11, 22, 60, 86),   (-5.5, 5.5)),
    ("Leg2",   "Leg.2", "body", (32, 43, 60, 86),   (-5.5, 5.5)),
    ("Leg3",   "Leg.3", "body", (64, 75, 60, 86),   (-5.5, 5.5)),
    ("Leg4",   "Leg.4", "body", (85, 96, 60, 86),   (-5.5, 5.5)),
]

# bone name -> head (x, y, z) in px-derived metres; every bone points straight up (+Z) 4 cm, so bone-local Y = world Z (up),
# local X = world X (right), local Z = toward the front. Joints sit where each part is anchored in the 2D rig:
#   Root at the feet; legs and eyes at their TOP edge (height changes shrink toward the body / upward-anchored like the 2D rects); arms at their centre.
def bone_heads():
    def top(rect_top, x_centre):
        return (x_centre, 0.0, (86 - rect_top) * U)
    return {
        "Root":  (0.0, 0.0, 0.0),
        "Arm.L": ((-58) * U, 0.0, (86 - 30) * U),
        "Arm.R": ((58) * U, 0.0, (86 - 30) * U),
        "Eye.L": ((16.5 - 48) * U, -24 * U, (86 - 10) * U),
        "Eye.R": ((79.5 - 48) * U, -24 * U, (86 - 10) * U),
        "Leg.1": ((16.5 - 48) * U, 0.0, 26 * U),
        "Leg.2": ((37.5 - 48) * U, 0.0, 26 * U),
        "Leg.3": ((69.5 - 48) * U, 0.0, 26 * U),
        "Leg.4": ((90.5 - 48) * U, 0.0, 26 * U),
    }


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.armatures):
        for b in list(coll):
            coll.remove(b)


def make_material(name, hex_):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = srgb(hex_)
    bsdf.inputs["Roughness"].default_value = 1.0
    m.diffuse_color = srgb(hex_)
    return m


def make_part(name, bone, mat, box):
    bm = bmesh.new()
    x0, x1, y0, y1, z0, z1 = box
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x = x0 + (v.co.x + 0.5) * (x1 - x0)
        v.co.y = y0 + (v.co.y + 0.5) * (y1 - y0)
        v.co.z = z0 + (v.co.z + 0.5) * (z1 - z0)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    o = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(o)
    o.data.materials.append(mat)
    vg = o.vertex_groups.new(name=bone)
    vg.add([v.index for v in me.vertices], 1.0, 'REPLACE')
    return o


def build():
    clear_scene()
    sc = bpy.context.scene
    sc.unit_settings.system = 'METRIC'
    sc.unit_settings.scale_length = 1.0
    mats = {"body": make_material("ClaudeBody", BODY_HEX), "eye": make_material("ClaudeEye", EYE_HEX)}
    parts = [make_part(n, b, mats[m], px_to_box(*rect, *depth)) for n, b, m, rect, depth in PARTS]
    bpy.ops.object.select_all(action='DESELECT')
    for o in parts:
        o.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    bpy.ops.object.join()
    mesh = bpy.context.view_layer.objects.active
    mesh.name = "ClaudeMascot"
    mesh.data.name = "ClaudeMascot"
    for p in mesh.data.polygons:
        p.use_smooth = False

    # armature
    arm_data = bpy.data.armatures.new("ClaudeMascotRig")
    arm = bpy.data.objects.new("ClaudeMascotRig", arm_data)
    sc.collection.objects.link(arm)
    bpy.context.view_layer.objects.active = arm
    arm.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    heads = bone_heads()
    for name, h in heads.items():
        eb = arm_data.edit_bones.new(name)
        eb.head = h
        eb.tail = (h[0], h[1], h[2] + 0.04)
        eb.roll = 0.0
        if name != "Root":
            eb.parent = arm_data.edit_bones["Root"]
    bpy.ops.object.mode_set(mode='OBJECT')
    mesh.parent = arm
    mod = mesh.modifiers.new("Armature", 'ARMATURE')
    mod.object = arm
    arm_data.display_type = 'STICK'
    arm.show_in_front = True
    return mesh, arm


def report(mesh, arm):
    mesh.data.calc_loop_triangles()
    d = mesh.dimensions
    zs = [v.co.z for v in mesh.data.vertices]
    print("Blender %s | metric, 1 unit = 1 m | Z up" % bpy.app.version_string)
    print("ClaudeMascot  %.3f x %.3f x %.3f m | %d triangles | %d parts | materials: %s"
          % (d.x, d.y, d.z, len(mesh.data.loop_triangles), len(PARTS), ", ".join(s.material.name for s in mesh.material_slots)))
    print("origin at world (%.3f, %.3f, %.3f) | lowest z = %.4f m | torso top z = %.4f m"
          % (*mesh.location, min(zs), max(zs)))
    print("vertex groups: %s" % ", ".join(g.name for g in mesh.vertex_groups))
    print("bones: %s" % ", ".join(b.name for b in arm.data.bones))


def export(mesh, arm):
    path = os.path.join(HERE, "claude_mascot.glb")
    bpy.ops.object.select_all(action='DESELECT')
    mesh.select_set(True)
    arm.select_set(True)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', export_yup=True, use_selection=True,
                              export_skins=True, export_animations=False)
    print("exported %s (%d bytes), +Y Up on" % (os.path.basename(path), os.path.getsize(path)))


if __name__ == "__main__":
    mesh, arm = build()
    report(mesh, arm)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "claude_mascot.blend"))
    export(mesh, arm)
