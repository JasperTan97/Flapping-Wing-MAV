// Generated by gencpp from file rosserial_mbed/TestResponse.msg
// DO NOT EDIT!


#ifndef ROSSERIAL_MBED_MESSAGE_TESTRESPONSE_H
#define ROSSERIAL_MBED_MESSAGE_TESTRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rosserial_mbed
{
template <class ContainerAllocator>
struct TestResponse_
{
  typedef TestResponse_<ContainerAllocator> Type;

  TestResponse_()
    : output()  {
    }
  TestResponse_(const ContainerAllocator& _alloc)
    : output(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _output_type;
  _output_type output;





  typedef boost::shared_ptr< ::rosserial_mbed::TestResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rosserial_mbed::TestResponse_<ContainerAllocator> const> ConstPtr;

}; // struct TestResponse_

typedef ::rosserial_mbed::TestResponse_<std::allocator<void> > TestResponse;

typedef boost::shared_ptr< ::rosserial_mbed::TestResponse > TestResponsePtr;
typedef boost::shared_ptr< ::rosserial_mbed::TestResponse const> TestResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rosserial_mbed::TestResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rosserial_mbed::TestResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rosserial_mbed::TestResponse_<ContainerAllocator1> & lhs, const ::rosserial_mbed::TestResponse_<ContainerAllocator2> & rhs)
{
  return lhs.output == rhs.output;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rosserial_mbed::TestResponse_<ContainerAllocator1> & lhs, const ::rosserial_mbed::TestResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rosserial_mbed

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::rosserial_mbed::TestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rosserial_mbed::TestResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosserial_mbed::TestResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosserial_mbed::TestResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosserial_mbed::TestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosserial_mbed::TestResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rosserial_mbed::TestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0825d95fdfa2c8f4bbb4e9c74bccd3fd";
  }

  static const char* value(const ::rosserial_mbed::TestResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0825d95fdfa2c8f4ULL;
  static const uint64_t static_value2 = 0xbbb4e9c74bccd3fdULL;
};

template<class ContainerAllocator>
struct DataType< ::rosserial_mbed::TestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rosserial_mbed/TestResponse";
  }

  static const char* value(const ::rosserial_mbed::TestResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rosserial_mbed::TestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string output\n"
"\n"
;
  }

  static const char* value(const ::rosserial_mbed::TestResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rosserial_mbed::TestResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.output);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TestResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rosserial_mbed::TestResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rosserial_mbed::TestResponse_<ContainerAllocator>& v)
  {
    s << indent << "output: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.output);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROSSERIAL_MBED_MESSAGE_TESTRESPONSE_H
