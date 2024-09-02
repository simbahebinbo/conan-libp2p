import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.scm import Git
from conan.tools.files import copy

class PackageConan(ConanFile):
    name = "p2p"
    version = "1.0.0"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/simbahebinbo/conan-cpp-libp2p.git"
    requires = (
        "boost/1.85.0",
        "fmt/10.1.1",
        "qtils/0.0.4",
        "zlib/1.2.11",
        "c-ares/1.18.1",
        "sqlite3/3.36.0",
        "gtest/1.14.0",
        "yaml-cpp/0.6.3"
    )
#
# openssl/1.1.1l
# protobuf/3.11.3
# tsl-hat-trie/0.6.0
# ms-gsl/2.0.0

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def source(self):
        git = Git(self)
        if not os.path.exists(os.path.join(self.source_folder, ".git")):
            git.clone("https://github.com/simbahebinbo/cpp-libp2p.git", target=".")
        else:
            self.run("git pull")

        branch_name = "develop"
        git.checkout(branch_name)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

        # 头文件路径
        include_folder = os.path.join(self.source_folder, "include")
        # 库文件路径
        lib_folder = os.path.join(self.build_folder, "src")

        # 使用 conan.tools.files.copy 替代 self.copy
        copy(self, "*.h", dst=os.path.join(self.package_folder, "include"), src=include_folder)
        copy(self, "*.hpp", dst=os.path.join(self.package_folder, "include"), src=include_folder)
        copy(self, "*.a", dst=os.path.join(self.package_folder, "lib"), src=lib_folder)

    def package_info(self):
        self.cpp_info.libs = ["p2p"]
