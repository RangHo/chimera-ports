pkgname = "sdbus-c++"
pkgver = "2.3.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "elogind-devel",
    "libexpat-devel",
]
pkgdesc = "High-level C++ D-Bus library"
license = "LGPL-2.1-only"
url = "https://github.com/Kistler-Group/sdbus-cpp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3a289eded586c26d06c1387de72c7bf7c809527a70d51ba6401fe61059b19626"


@subpackage("sdbus-c++-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
