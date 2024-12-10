#
# This file is the web-busybox recipe.
#

SUMMARY = "Simple web-busybox application"
SECTION = "PETALINUX/apps"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://index.html"
SRC_URI += "file://zybo.png"
SRC_URI += "file://cgi-bin/index.cgi"

FILES:${PN} += "/srv/www"

S = "${WORKDIR}"

do_install() {
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/index.html ${D}/srv/www/index_original.html # name changed to avoid webserver to upload it, and uplod cgi instead
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/zybo.png ${D}/srv/www
	     install -d ${D}/srv/www/cgi-bin
       	 install -m 0755 ${S}/cgi-bin/index.cgi ${D}/srv/www/cgi-bin
}
