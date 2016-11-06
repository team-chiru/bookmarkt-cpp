from conans import ConanFile, CMake

class BookmarktConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   # requires = "Poco/1.7.3@lasote/stable" # comma separated list of requirements

   generators = "cmake", "gcc", "txt"
   # default_options = "Poco:shared=True", "OpenSSL:shared=True"

   def imports(self):
      self.copy("*.dll", dst="bin", src="bin") # From bin to bin
      self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin

   def build(self):
      cmake = CMake(self.settings)
      self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
      self.run('cmake --build . %s' % cmake.build_config)
