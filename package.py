name = "usd"

version = "23.08"

description = """
    Universal Scene Description (USD) is an efficient, scalable system for authoring, reading, and streaming
    time-sampled scene description for interchange between graphics applications.
    """

authors = [
    "Pixar",
]

requires = [
    "boost-1.70+",
    "cmake-3",
    "gcc-6.3+",
    "tbb-2020<2021",
]

variants = [
    [
        "platform-linux",
    ],
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
    "usdzip",
]

build_system = "cmake"


with scope("config") as config:
    config.build_thread_count = "logical_cores"


def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    # env.PYTHONPATH.prepend("{root}/lib/python")
    env.CMAKE_MODULE_PATH.prepend("{root}")

    # Helper environment variables.
    env.USD_BINARY_PATH.set("{root}/bin")
    env.USD_INCLUDE_PATH.set("{root}/include")
    env.USD_LIBRARY_PATH.set("{root}/lib")
