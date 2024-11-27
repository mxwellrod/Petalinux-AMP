#
# This file is the freeRTOS-OCM recipe.
#

SUMMARY = "Simple freeRTOS-OCM application"
SECTION = "PETALINUX/apps"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://OCM_demo.elf \
	"

S = "${WORKDIR}"
INSANE_SKIP_${PN} = "arch"

do_install() {
	     install -d ${D}/lib/firmware
	     install -m 0644 ${S}/OCM_demo.elf ${D}/lib/firmware/OCM_demo.elf
}
FILES:${PN} = "/lib/firmware/OCM_demo.elf"