#
# This file is the webserver recipe.
#

SUMMARY = "Simple webserver application with NGINX"
SECTION = "PETALINUX/apps"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://index.html"
SRC_URI += "file://50x.html"
SRC_URI += "file://info.php"
SRC_URI += "file://open_db.php"
SRC_URI += "file://open_test.db"
SRC_URI += "file://phpliteadmin.config.php"
SRC_URI += "file://phpliteadmin.php"
SRC_URI += "file://sqlite_test.php"

SRC_URI += "file://db/db1.db"
SRC_URI += "file://db/test.db"

FILES:${PN} += "/srv/www"

S = "${WORKDIR}"

do_install() {
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/index.html ${D}/srv/www/index.html
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/50x.html ${D}/srv/www/50x.html
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/info.php ${D}/srv/www/info.php
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/open_db.php ${D}/srv/www/open_db.php
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/open_test.db ${D}/srv/www/open_test.db
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/phpliteadmin.config.php ${D}/srv/www/phpliteadmin.config.php
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/phpliteadmin.php ${D}/srv/www/phpliteadmin.php
	     install -d ${D}/srv/www
	     install -m 0644 ${S}/sqlite_test.php ${D}/srv/www/sqlite_test.php
	     install -d ${D}/srv/www/db
	     install -m 0644 ${S}/db/db1.db ${D}/srv/www/db/db1.db
	     install -d ${D}/srv/www/db
	     install -m 0644 ${S}/db/test.db ${D}/srv/www/db/test.db
}
