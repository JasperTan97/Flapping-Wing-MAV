#include <ros.h>
#include <PPMReader.h>
#include <InterruptHandler.h>
#include <custommsg/ppmchnls.h>

int interruptPin = 3;
int channelAmount = 8;
PPMReader ppm(interruptPin, channelAmount);
ros::NodeHandle nh;

custommsg::ppmchnls chnl_vals;
ros::Publisher pubchnl("channel_values", &chnl_vals);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  nh.initNode();
  nh.advertise(pubchnl);
}

void loop() {
  // put your main code here, to run repeatedly:
  /*
  for (int channel = 1; channel <= channelAmount; ++channel) {
    unsigned long value = ppm.latestValidChannelValue(channel, 0);
    Serial.print(String(value) + " ");
  }
  Serial.println();
  */
  chnl_vals.chn1 = ppm.latestValidChannelValue(1, 0);
  chnl_vals.chn2 = ppm.latestValidChannelValue(2, 0);
  chnl_vals.chn3 = ppm.latestValidChannelValue(3, 0);
  chnl_vals.chn4 = ppm.latestValidChannelValue(4, 0);
  chnl_vals.chn5 = ppm.latestValidChannelValue(5, 0);
  chnl_vals.chn6 = ppm.latestValidChannelValue(6, 0);
  chnl_vals.chn7 = ppm.latestValidChannelValue(7, 0);
  chnl_vals.chn8 = ppm.latestValidChannelValue(8, 0);

  pubchnl.publish(&chnl_vals);
  nh.spinOnce();
  delay(10);
}
