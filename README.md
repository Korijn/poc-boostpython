# Proof of Concept Boost Python

This repository demonstrates how to build a package with a Boost.Python module in it, 
and how to distribute it as a wheel. The wheel also includes the Boost.Python library,
so that users will not need to install Boost on their systems separately.

## Current Status

Tested on Windows 10 x64 CPython 3.6.4.

## Windows requirements

Install VS2017 build tools.

## Acquire Boost sources

Download and unpack into repo root a source distribution of boost http://www.boost.org/. 
At the time writing, v1.66.0 is latest.

## Virtualenv setup

```
> pipenv install --dev
```

## Build Boost.Python

Run the following command at least once:

```
> pipenv run python build_boost.py --init
```

## Development setup

First install boost into your virtualenv (so that DLLs etc. will be on their expected paths):

```
> pipenv run python build_boost.py install
```

Then use `setup.py develop` as usual:

```
> pipenv run python setup.py develop
> pipenv run python -c "from hwpkg import HelloWorldSayer; HelloWorldSayer().SayHello()"
Hello World!
```

Re-run the `setup.py develop` command to re-compile when you change your sources. Configure 
your IDE to run this command on-save of your source files for a pleasant  development cycle.

## Building a wheel

```
> pipenv run python build_boost.py
> pipenv run python setup.py bdist_wheel
```

Go to a new folder and create a blank venv. Install the built wheel into it and call the
module to test your wheel:

```
> cd ..
> mkdir tmp
> pipenv install
> pipenv run pip install ..\poc-boostpython\dist\hwpkg-0.0.0-cp36-cp36m-win_amd64.whl
> pipenv run python -c "from hwpkg import HelloWorldSayer; HelloWorldSayer().SayHello()"
Hello World!
```
