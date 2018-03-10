from setuptools import setup, Extension


setup(
    name='hwpkg',
    packages=['hwpkg'],
    ext_modules=[
        Extension('hwpkg.hello_world', ['hwpkg/hello_world.cpp'],
                  include_dirs=['boost_1_66_0']),
    ],
)
