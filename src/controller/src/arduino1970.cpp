#include <ros/ros.h>
#include <custommsg/ppmchnls.h>


ros::Publisher *pubptr;

void callback(const custommsg::ppmchnls::ConstPtr& msg)
{
	//msg->header.stamp = ros::Time::now();
	custommsg::ppmchnls msgOut;
	msgOut.header.stamp = ros::Time::now();
	msgOut.chn1 = msg->chn1;
	msgOut.chn2 = msg->chn2;
	msgOut.chn3 = msg->chn3;
	msgOut.chn4 = msg->chn4;
	msgOut.chn5 = msg->chn5;
	msgOut.chn6 = msg->chn6;
	msgOut.chn7 = msg->chn7;
	msgOut.chn8 = msg->chn8;

	pubptr->publish(msgOut);
}



int main(int argc, char** argv)
{
	ros::init(argc, argv, "Arduino_1970");
	ros::NodeHandle nh;
	ros::Subscriber sub = nh.subscribe<custommsg::ppmchnls>("channel_values", 1, callback);

	pubptr = new ros::Publisher(nh.advertise<custommsg::ppmchnls>("channel_values_time", 1000));


	ros::spin();
	delete pubptr;
}
