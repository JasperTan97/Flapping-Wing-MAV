#ifndef _ROS_custommsg_ppmchnls_h
#define _ROS_custommsg_ppmchnls_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace custommsg
{

  class ppmchnls : public ros::Msg
  {
    public:
      typedef uint16_t _chn1_type;
      _chn1_type chn1;
      typedef uint16_t _chn2_type;
      _chn2_type chn2;
      typedef uint16_t _chn3_type;
      _chn3_type chn3;
      typedef uint16_t _chn4_type;
      _chn4_type chn4;
      typedef uint16_t _chn5_type;
      _chn5_type chn5;
      typedef uint16_t _chn6_type;
      _chn6_type chn6;
      typedef uint16_t _chn7_type;
      _chn7_type chn7;
      typedef uint16_t _chn8_type;
      _chn8_type chn8;

    ppmchnls():
      chn1(0),
      chn2(0),
      chn3(0),
      chn4(0),
      chn5(0),
      chn6(0),
      chn7(0),
      chn8(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->chn1 >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->chn1 >> (8 * 1)) & 0xFF;
      offset += sizeof(this->chn1);
      *(outbuffer + offset + 0) = (this->chn2 >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->chn2 >> (8 * 1)) & 0xFF;
      offset += sizeof(this->chn2);
      *(outbuffer + offset + 0) = (this->chn3 >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->chn3 >> (8 * 1)) & 0xFF;
      offset += sizeof(this->chn3);
      *(outbuffer + offset + 0) = (this->chn4 >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->chn4 >> (8 * 1)) & 0xFF;
      offset += sizeof(this->chn4);
      *(outbuffer + offset + 0) = (this->chn5 >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->chn5 >> (8 * 1)) & 0xFF;
      offset += sizeof(this->chn5);
      *(outbuffer + offset + 0) = (this->chn6 >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->chn6 >> (8 * 1)) & 0xFF;
      offset += sizeof(this->chn6);
      *(outbuffer + offset + 0) = (this->chn7 >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->chn7 >> (8 * 1)) & 0xFF;
      offset += sizeof(this->chn7);
      *(outbuffer + offset + 0) = (this->chn8 >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->chn8 >> (8 * 1)) & 0xFF;
      offset += sizeof(this->chn8);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      this->chn1 =  ((uint16_t) (*(inbuffer + offset)));
      this->chn1 |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->chn1);
      this->chn2 =  ((uint16_t) (*(inbuffer + offset)));
      this->chn2 |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->chn2);
      this->chn3 =  ((uint16_t) (*(inbuffer + offset)));
      this->chn3 |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->chn3);
      this->chn4 =  ((uint16_t) (*(inbuffer + offset)));
      this->chn4 |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->chn4);
      this->chn5 =  ((uint16_t) (*(inbuffer + offset)));
      this->chn5 |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->chn5);
      this->chn6 =  ((uint16_t) (*(inbuffer + offset)));
      this->chn6 |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->chn6);
      this->chn7 =  ((uint16_t) (*(inbuffer + offset)));
      this->chn7 |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->chn7);
      this->chn8 =  ((uint16_t) (*(inbuffer + offset)));
      this->chn8 |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->chn8);
     return offset;
    }

    virtual const char * getType() override { return "custommsg/ppmchnls"; };
    virtual const char * getMD5() override { return "40ec51ccfeeb5a2284da850069525f99"; };

  };

}
#endif
