pkgname = "noctalia"
pkgver = "5.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--buildtype=release",
    "-Dcpp_std=c++23",
    "-Db_lto=true",
]
hostmakedepends = [
    "bash",
    "git",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "curl-devel",
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "jemalloc-devel",
    "libepoxy-devel",
    "libqalculate-devel",
    "librsvg-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "mesa-devel",
    "pango-devel",
    "pipewire-devel",
    "polkit-devel",
    "sdbus-c++-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = [
    "elogind",
    "tzdb",
]
pkgdesc = "Lightweight Wayland shell built directly on Wayland and OpenGL ES"
license = "MIT"
url = "https://github.com/noctalia-dev/noctalia"
source = f"{url}/archive/refs/heads/main.tar.gz"
sha256 = "SKIP"
# not yet
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
