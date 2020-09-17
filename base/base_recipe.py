from conans import ConanFile, tools


class BaseConanFile(ConanFile):
    license = 'MIT'
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake', 'cmake_find_package'

    def build_id(self):
        self.output.info('Running build_id.')

    def source(self):
        self.output.info('Running source.')

    def system_requirements(self):
        self.output.info('Running system_requirements.')
        installer = tools.SystemPackageTool()
        installer.install('qt5-default')
