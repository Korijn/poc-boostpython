#include <iostream>
#include "simple_example.h"
#include <boost/python.hpp>
 
using namespace boost::python;
// Declare our Boost Python Module
// enable_pickling is optional, but I find it useful to
// have persistent storage of simple data types in Python.
BOOST_PYTHON_MODULE(simpleExample)
{
	class_<SimpleExample>("simpleExample",init<>())
		.def("SayHello", &SimpleExample::SayHello)
		.enable_pickling()
		;
}
 
void SimpleExample::SayHello() 
{
	std::cout<<"Hello World!";
}