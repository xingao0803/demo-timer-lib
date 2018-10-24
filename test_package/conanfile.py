import os

from conans import ConanFile, tools


class TimerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "compiler_args"
    requires = "Timer/1.0@jfrog/stable"

    def build(self):
        self.run("g++ ../../example.cpp @conanbuildinfo.args -o example")

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')
        self.copy('*.a', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run("..%sexample" % os.sep)
