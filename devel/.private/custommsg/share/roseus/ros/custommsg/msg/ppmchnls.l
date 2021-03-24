;; Auto-generated. Do not edit!


(when (boundp 'custommsg::ppmchnls)
  (if (not (find-package "CUSTOMMSG"))
    (make-package "CUSTOMMSG"))
  (shadow 'ppmchnls (find-package "CUSTOMMSG")))
(unless (find-package "CUSTOMMSG::PPMCHNLS")
  (make-package "CUSTOMMSG::PPMCHNLS"))

(in-package "ROS")
;;//! \htmlinclude ppmchnls.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass custommsg::ppmchnls
  :super ros::object
  :slots (_header _chn1 _chn2 _chn3 _chn4 _chn5 _chn6 _chn7 _chn8 ))

(defmethod custommsg::ppmchnls
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:chn1 __chn1) 0)
    ((:chn2 __chn2) 0)
    ((:chn3 __chn3) 0)
    ((:chn4 __chn4) 0)
    ((:chn5 __chn5) 0)
    ((:chn6 __chn6) 0)
    ((:chn7 __chn7) 0)
    ((:chn8 __chn8) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _chn1 (round __chn1))
   (setq _chn2 (round __chn2))
   (setq _chn3 (round __chn3))
   (setq _chn4 (round __chn4))
   (setq _chn5 (round __chn5))
   (setq _chn6 (round __chn6))
   (setq _chn7 (round __chn7))
   (setq _chn8 (round __chn8))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:chn1
   (&optional __chn1)
   (if __chn1 (setq _chn1 __chn1)) _chn1)
  (:chn2
   (&optional __chn2)
   (if __chn2 (setq _chn2 __chn2)) _chn2)
  (:chn3
   (&optional __chn3)
   (if __chn3 (setq _chn3 __chn3)) _chn3)
  (:chn4
   (&optional __chn4)
   (if __chn4 (setq _chn4 __chn4)) _chn4)
  (:chn5
   (&optional __chn5)
   (if __chn5 (setq _chn5 __chn5)) _chn5)
  (:chn6
   (&optional __chn6)
   (if __chn6 (setq _chn6 __chn6)) _chn6)
  (:chn7
   (&optional __chn7)
   (if __chn7 (setq _chn7 __chn7)) _chn7)
  (:chn8
   (&optional __chn8)
   (if __chn8 (setq _chn8 __chn8)) _chn8)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint16 _chn1
    2
    ;; uint16 _chn2
    2
    ;; uint16 _chn3
    2
    ;; uint16 _chn4
    2
    ;; uint16 _chn5
    2
    ;; uint16 _chn6
    2
    ;; uint16 _chn7
    2
    ;; uint16 _chn8
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint16 _chn1
       (write-word _chn1 s)
     ;; uint16 _chn2
       (write-word _chn2 s)
     ;; uint16 _chn3
       (write-word _chn3 s)
     ;; uint16 _chn4
       (write-word _chn4 s)
     ;; uint16 _chn5
       (write-word _chn5 s)
     ;; uint16 _chn6
       (write-word _chn6 s)
     ;; uint16 _chn7
       (write-word _chn7 s)
     ;; uint16 _chn8
       (write-word _chn8 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint16 _chn1
     (setq _chn1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _chn2
     (setq _chn2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _chn3
     (setq _chn3 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _chn4
     (setq _chn4 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _chn5
     (setq _chn5 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _chn6
     (setq _chn6 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _chn7
     (setq _chn7 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _chn8
     (setq _chn8 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get custommsg::ppmchnls :md5sum-) "4976e6ed228d03b8df848315fce63edb")
(setf (get custommsg::ppmchnls :datatype-) "custommsg/ppmchnls")
(setf (get custommsg::ppmchnls :definition-)
      "Header header
uint16 chn1
uint16 chn2
uint16 chn3
uint16 chn4
uint16 chn5
uint16 chn6
uint16 chn7
uint16 chn8

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :custommsg/ppmchnls "4976e6ed228d03b8df848315fce63edb")


