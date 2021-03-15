#include <ros/ros.h>
#include <message_filters/subscriber.h>
#include <message_filters/time_synchronizer.h>
#include <message_filters/sync_policies/approximate_time.h>
#include <geometry_msgs/PoseStamped.h>
#include <custommsg/ppmchnls.h>
#include <fstream>
#include <string>

using namespace std;
using namespace message_filters;

// Function Declarations
void callback(const geometry_msgs::PoseStamped::ConstPtr&, const custommsg::ppmchnls::ConstPtr&);
void initialise_file();

// make csv file
string filename = "bird_data.csv";
int linesCount = 0;

void initialise_file(){
	fstream outputFile;
	// open file
	outputFile.open(filename, ios::out);
	// write the csv file headers
	outputFile << "x" << "," << "y" << "," << "z" << "," << "qx" << "," << "qy" << "," << "qz" << "," << "qw" << "," << "chn1" << "," << "chn2" << "," << "chn3" << "," << "chn4" << "," << "chn5" << "," << "chn6" << "," << "chn7" << "," << "chn8" << endl;
	// close the csv file
	outputFile.close();	
	linesCount++;
}


void callback(const geometry_msgs::PoseStamped::ConstPtr& msg, const custommsg::ppmchnls::ConstPtr& ppm_vals)
{
	fstream outputFile;
	outputFile.open(filename, ios::out | (linesCount ? ios::app : ios::trunc));
	// write the csv file data row
	outputFile << msg->pose.position.x << "," << msg->pose.position.y << "," << msg->pose.position.z << "," << msg->pose.orientation.x << "," 
	<< msg->pose.orientation.y << "," << msg->pose.orientation.z << "," << msg->pose.orientation.w << "," << ppm_vals->chn1 << "," << ppm_vals -> chn2 << "," << ppm_vals -> chn3 << "," << ppm_vals -> chn4 << "," << ppm_vals -> chn5 << "," << ppm_vals -> chn6 << "," << ppm_vals -> chn7 << "," << ppm_vals -> chn8 << endl;
	// close the csv file
	outputFile.close();
	linesCount++;
}

int main(int argc, char** argv)
{
	ros::init(argc, argv, "bird_data_compiler_node");
	ros::NodeHandle nh;

	message_filters::Subscriber<geometry_msgs::PoseStamped> sub_vicon(nh, "/mavros/vision_pose/pose", 1);
	message_filters::Subscriber<custommsg::ppmchnls> sub_arduino(nh, "channel_values", 1);

	typedef sync_policies::ApproximateTime<geometry_msgs::PoseStamped, custommsg::ppmchnls> MySyncPolicy;

	Synchronizer<MySyncPolicy> sync(MySyncPolicy(10), sub_vicon, sub_arduino);
	sync.registerCallback(boost::bind(&callback, _1, _2));

	initialise_file();
	ros::spin();
	
	return 0;
}
