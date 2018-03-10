# Proof of Concept Boost Python

First download and unpack into repo root a source distribution of boost http://www.boost.org/

Then open a console:

```
> "C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" amd64
> cd boost_1_66_0
> bootstrap
> b2 toolset=msvc link=shared --with-python -j4
> cd ..
> python setup.py build
```

Had to manually copy over the boost_python lib and dll files into the build dir for it to work.

If you are getting warnings about Boost.config and your compiler version, append `define="BOOST_CONFIG_SUPPRESS_OUTDATED_MESSAGE=1"` to the command.

If something fails, clean up before trying again with `b2 --clean`.
