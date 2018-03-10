from setuptools import setup, Extension


setup(
    name='mypkg',
    packages=['mypkg'],
    ext_modules=[
        Extension('mypkg.simpleExample',
                  ['mypkg/simple_example.cpp'],
                  include_dirs=['mypkg', '../boost_1_66_0'],
                  library_dirs=['../boost_1_66_0/stage/lib'],
                  )
    ],
)
