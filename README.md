# Proof of Concept Boost Python

This repository demonstrates how to build a package with a Boost.Python module in it, 
and how to distribute it as a wheel.

## Windows requirements

Install VS2017 build tools.

## Acquire Boost sources

Download and unpack into repo root a source distribution of boost http://www.boost.org/. 
At the time writing, v1.66.0 is latest.

## Install Boost.Python

```
> pipenv install --dev
> pipenv run python build_boost.py
```

## Building the package

```
> pipenv run python setup.py build_ext
```

Add `-i` for an in-place build, giving you a development setup.

## Testing

```
> pipenv run python -c "from hwpkg import HelloWorldSayer; HelloWorldSayer().SayHello()"
Hello World!
```
