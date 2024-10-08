from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
import os

class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires(self.tested_reference_str)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        multiaddress_path = os.path.join(self.build_folder, "multiaddress")
        self.run(multiaddress_path, env="conanrun")
