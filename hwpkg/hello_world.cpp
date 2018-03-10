#include <iostream>
#include "hello_world.h"
#include <boost/python.hpp>
 
using namespace boost::python;

BOOST_PYTHON_MODULE(hello_world)
{
	class_<HelloWorldSayer>("HelloWorldSayer",init<>())
		.def("SayHello", &HelloWorldSayer::SayHello)
		;
}
 
void HelloWorldSayer::SayHello() 
{
	std::cout<<"Hello World!";
}