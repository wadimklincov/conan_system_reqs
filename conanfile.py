from conans import ConanFile, CMake, tools


class SystemReqsConan(ConanFile):
    name = "system_reqs_test"
    version = "0.1.0"
    exports_sources = "src/*"

    python_requires = 'base_recipe/0.1.0'
    python_requires_extend = 'base_recipe.BaseConanFile'

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

#    Uncomment for correct behaviour
#    def system_requirements(self):
#        super().system_requirements()
