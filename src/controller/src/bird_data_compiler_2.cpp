#include <ros/ros.h>
#include <message_filters/subscriber.h>
#include <message_filters/time_synchronizer.h>
#include <message_filters/sync_policies/approximate_time.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/TwistStamped.h>
#include <geometry_msgs/AccelStamped.h>
#include <custommsg/ppmchnls.h>
#include <fstream>
#include <string>

using namespace std;
using namespace message_filters;

// Function Declarations
void callback(const geometry_msgs::PoseStamped::ConstPtr&, const geometry_msgs::TwistStamped::ConstPtr&, const geometry_msgs::AccelStamped::ConstPtr&, const custommsg::ppmchnls::ConstPtr&);
void initialise_file();

// make csv file
string filename = "bird_data.csv";
int linesCount = 0;


ros::Time startTime;

void initialise_file(){
	fstream outputFile;
	// open file
	outputFile.open(filename, ios::out);
	// write the csv file headers
	outputFile << "x" << "," << "y" << "," << "z" << "," 
<< "qx" << "," << "qy" << "," << "qz" << "," << "qw" << "," 
<< "u" << "," << "v" << "," << "w" << "," 
<< "theta_dot" << "," << "phi_dot" << ","  "psi_dot" << ","  
<< "u_dot" << "," << "v_dot" << "," << "w_dot" << "," 
<< "theta_ddot" << "," << "phi_ddot" << ","  "psi_ddot" 
<< ","  "chn1" << "," << "chn2" << "," << "chn3" << "," << "chn4" << "," << "chn5" << "," << "chn6" << "," << "chn7" << "," << "chn8" << "," << "time" << endl;
	// close the csv file
	outputFile.close();	
	linesCount++;
}


void callback(const geometry_msgs::PoseStamped::ConstPtr& msg, const geometry_msgs::TwistStamped::ConstPtr& msg2, const geometry_msgs::AccelStamped::ConstPtr& msg3, const custommsg::ppmchnls::ConstPtr& ppm_vals)
{
	fstream outputFile;
	outputFile.open(filename, ios::out | (linesCount ? ios::app : ios::trunc));
	// write the csv file data row
	outputFile << msg->pose.position.x << "," << msg->pose.position.y << "," << msg->pose.position.z << "," 

<< msg->pose.orientation.x << "," 
	<< msg->pose.orientation.y << "," << msg->pose.orientation.z << "," << msg->pose.orientation.w << "," 

<< msg2->twist.linear.x << "," << msg2->twist.linear.y << "," << msg2->twist.linear.z << "," 

<< msg2->twist.angular.x << "," << msg2->twist.angular.y << ","<< msg2->twist.angular.z << ","

<< msg3->accel.linear.x << "," << msg3->accel.linear.y << "," << msg3->accel.linear.z << "," 

<< msg3->accel.angular.x << "," << msg3->accel.angular.y << ","<< msg3->accel.angular.z << "," 

<< ppm_vals->chn1 << "," << ppm_vals -> chn2 << "," << ppm_vals -> chn3 << "," << ppm_vals -> chn4 << "," << ppm_vals -> chn5 << "," << ppm_vals -> chn6 << "," << ppm_vals -> chn7 << "," << ppm_vals -> chn8 << "," << ros::Time::now() - startTime << endl;
	// close the csv file
	outputFile.close();
	linesCount++;

}

int main(int argc, char** argv)
{
	ros::init(argc, argv, "bird_data_compiler_node");
	ros::NodeHandle nh;

	message_filters::Subscriber<geometry_msgs::PoseStamped> sub_vicon_pose(nh, "/mavros/vision_pose/pose", 10000);
	message_filters::Subscriber<geometry_msgs::TwistStamped> sub_vicon_twist(nh, "/vrpn_client_node/flapusp/twist", 10000);
	message_filters::Subscriber<geometry_msgs::AccelStamped> sub_vicon_accel(nh, "/vrpn_client_node/flapusp/accel", 10000);
	message_filters::Subscriber<custommsg::ppmchnls> sub_arduino(nh, "channel_values_time", 10000);

	typedef sync_policies::ApproximateTime<geometry_msgs::PoseStamped, geometry_msgs::TwistStamped, geometry_msgs::AccelStamped, custommsg::ppmchnls> MySyncPolicy;

	Synchronizer<MySyncPolicy> sync(MySyncPolicy(10), sub_vicon_pose, sub_vicon_twist, sub_vicon_accel, sub_arduino);
	sync.registerCallback(boost::bind(&callback, _1, _2, _3, _4));

	initialise_file();

	startTime = ros::Time::now();	
	
	ros::spin();
	
	return 0;
}
