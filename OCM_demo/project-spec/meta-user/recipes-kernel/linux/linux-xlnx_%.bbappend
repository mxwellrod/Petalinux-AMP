FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " file://bsp.cfg"
KERNEL_FEATURES:append = " bsp.cfg"
SRC_URI += "file://user_2024-11-27-00-19-00.cfg \
            file://user_2024-12-02-09-13-00.cfg \
            "

