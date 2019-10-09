# Based and improved from https://github.com/UTS-AnimalLogicAcademy/open-source-rez-packages/tree/master/usd_katana

set(PXR_INSTALL_SUBDIR "third_party/katana")

if (NOT ${PXR_BUILD_USD_CORE})
    # If we are not building the USD core libraries and binaries, we make sure that the headers of some necessary
    # libraries are correctly exposed to CMake.
    include_directories(${Boost_INCLUDE_DIRS} ${TBB_INCLUDE_DIRS} ${GLEW_INCLUDE_DIR})
endif()

# Transform the KATANA_API versions into defines to be used by this code
add_definitions(
    -DPX_KATANA_ASSET_API_VER=${KATANA_API_ASSET_API_VERSION}
    -DPX_KATANA_AMP_API_VER=${KATANA_API_AMP_API_VERSION}
    -DPX_KATANA_SGG_API_VER=${KATANA_API_SGG_API_VERSION}
    -DPX_KATANA_RENDER_API_VER=${KATANA_API_RENDER_API_VERSION}
    -DPX_KATANA_VMP_API_VER=${KATANA_API_VMP_API_VERSION}
    -DPX_KATANA_OP_API_VER=${KATANA_API_OP_API_VERSION}
    -DPX_KATANA_ATTRFNC_API_VER=${KATANA_API_ATTRFNC_API_VERSION}
    )

add_subdirectory(lib)
add_subdirectory(plugin)
add_subdirectory(python)