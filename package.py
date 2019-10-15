name = "usd"

version = "19.07"

authors = [
    "Pixar"
]

description = \
    """
    Universal Scene Description (USD) is an efficient, scalable system for authoring, reading, and streaming
    time-sampled scene description for interchange between graphics applications.
    """

requires = [
    "alembic-1.7+",
    "boost-1.61+",
    "cmake-3+",
    "gcc-6+",
    "glew-2+",
    "ilmbase-2.2+<2.4",
    "jinja2-2+",
    "katana-3.0+",
    "maya-2017+",
    "ocio-1.0.9+",
    "openexr-2.2+<2.4",
    "oiio-1.7.14+",
    "opensubdiv-3.3+",
    "ptex-2.1+",
    "pyopengl-3+",
    "pyside2-5.12+",
    "python-2.7+<3",
    "tbb-2017.U6+",
]

variants = [
    ["platform-linux"]
]

tools = [
    "sdfdump",
    "sdffilter",
    "testusdview",
    "usdcat",
    "usdchecker",
    "usddiff",
    "usddumpcrate",
    "usdedit",
    "usdGenSchema",
    "usdrecord",
    "usdresolve",
    "usdstitch",
    "usdstitchclips",
    "usdtree",
    "usdview",
    "usdzip"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "usd-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python")
    env.KATANA_RESOURCES.append("{root}/third_party/katana/plugin")
    env.KATANA_POST_PYTHONPATH.append("{root}/third_party/katana/lib")
    env.MAYA_PLUG_IN_PATH.append("{root}/third_party/maya/plugin")
    env.MAYA_SCRIPT_PATH.append("{root}/third_party/maya/lib/usd/usdMaya/resources")
    env.MAYA_SCRIPT_PATH.append("{root}/third_party/maya/plugin/pxrUsdPreviewSurface/resources")
    env.MAYA_SHELVES_ICONS = "{root}/third_party/maya/lib/usd/usdMaya/resources"
    env.MAYA_SHELF_PATH.append("{root}/third_party/maya/lib/usd/usdMaya/resources")
    env.XBMLANGPATH.append("{root}/third_party/maya/share/usd/plugins/usdMaya/resources")

    # Helper environment variables.
    env.USD_BINARY_PATH.set("{root}/bin")
    env.USD_INCLUDE_PATH.set("{root}/include")
    env.USD_LIBRARY_PATH.set("{root}/lib")
