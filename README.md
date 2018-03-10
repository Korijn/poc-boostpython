# Proof of Concept Boost Python

This repository demonstrates how to build a package with a Boost.Python module in it, 
and how to distribute it as a wheel. The wheel also includes the Boost.Python library,
so that users will not need to install Boost on their systems separately.

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

Make sure to append `--init` on your first call to initialize Boost.Build.

Append `install` if you are looking for a development setup. Boost will be installed into
your virtualenv.

## Development setup

```
> pipenv run python build_boost.py install
> pipenv run python setup.py develop
> pipenv run python -c "from hwpkg import HelloWorldSayer; HelloWorldSayer().SayHello()"
Hello World!
```

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
