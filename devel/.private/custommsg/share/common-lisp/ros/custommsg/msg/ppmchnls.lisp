; Auto-generated. Do not edit!


(cl:in-package custommsg-msg)


;//! \htmlinclude ppmchnls.msg.html

(cl:defclass <ppmchnls> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (chn1
    :reader chn1
    :initarg :chn1
    :type cl:fixnum
    :initform 0)
   (chn2
    :reader chn2
    :initarg :chn2
    :type cl:fixnum
    :initform 0)
   (chn3
    :reader chn3
    :initarg :chn3
    :type cl:fixnum
    :initform 0)
   (chn4
    :reader chn4
    :initarg :chn4
    :type cl:fixnum
    :initform 0)
   (chn5
    :reader chn5
    :initarg :chn5
    :type cl:fixnum
    :initform 0)
   (chn6
    :reader chn6
    :initarg :chn6
    :type cl:fixnum
    :initform 0)
   (chn7
    :reader chn7
    :initarg :chn7
    :type cl:fixnum
    :initform 0)
   (chn8
    :reader chn8
    :initarg :chn8
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ppmchnls (<ppmchnls>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ppmchnls>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ppmchnls)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custommsg-msg:<ppmchnls> is deprecated: use custommsg-msg:ppmchnls instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:header-val is deprecated.  Use custommsg-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'chn1-val :lambda-list '(m))
(cl:defmethod chn1-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:chn1-val is deprecated.  Use custommsg-msg:chn1 instead.")
  (chn1 m))

(cl:ensure-generic-function 'chn2-val :lambda-list '(m))
(cl:defmethod chn2-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:chn2-val is deprecated.  Use custommsg-msg:chn2 instead.")
  (chn2 m))

(cl:ensure-generic-function 'chn3-val :lambda-list '(m))
(cl:defmethod chn3-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:chn3-val is deprecated.  Use custommsg-msg:chn3 instead.")
  (chn3 m))

(cl:ensure-generic-function 'chn4-val :lambda-list '(m))
(cl:defmethod chn4-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:chn4-val is deprecated.  Use custommsg-msg:chn4 instead.")
  (chn4 m))

(cl:ensure-generic-function 'chn5-val :lambda-list '(m))
(cl:defmethod chn5-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:chn5-val is deprecated.  Use custommsg-msg:chn5 instead.")
  (chn5 m))

(cl:ensure-generic-function 'chn6-val :lambda-list '(m))
(cl:defmethod chn6-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:chn6-val is deprecated.  Use custommsg-msg:chn6 instead.")
  (chn6 m))

(cl:ensure-generic-function 'chn7-val :lambda-list '(m))
(cl:defmethod chn7-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:chn7-val is deprecated.  Use custommsg-msg:chn7 instead.")
  (chn7 m))

(cl:ensure-generic-function 'chn8-val :lambda-list '(m))
(cl:defmethod chn8-val ((m <ppmchnls>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custommsg-msg:chn8-val is deprecated.  Use custommsg-msg:chn8 instead.")
  (chn8 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ppmchnls>) ostream)
  "Serializes a message object of type '<ppmchnls>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn3)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn3)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn4)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn4)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn5)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn5)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn6)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn6)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn7)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn7)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn8)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn8)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ppmchnls>) istream)
  "Deserializes a message object of type '<ppmchnls>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn3)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn3)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn4)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn4)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn5)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn5)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn6)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn6)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn7)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn7)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'chn8)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'chn8)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ppmchnls>)))
  "Returns string type for a message object of type '<ppmchnls>"
  "custommsg/ppmchnls")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ppmchnls)))
  "Returns string type for a message object of type 'ppmchnls"
  "custommsg/ppmchnls")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ppmchnls>)))
  "Returns md5sum for a message object of type '<ppmchnls>"
  "4976e6ed228d03b8df848315fce63edb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ppmchnls)))
  "Returns md5sum for a message object of type 'ppmchnls"
  "4976e6ed228d03b8df848315fce63edb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ppmchnls>)))
  "Returns full string definition for message of type '<ppmchnls>"
  (cl:format cl:nil "Header header~%uint16 chn1~%uint16 chn2~%uint16 chn3~%uint16 chn4~%uint16 chn5~%uint16 chn6~%uint16 chn7~%uint16 chn8~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ppmchnls)))
  "Returns full string definition for message of type 'ppmchnls"
  (cl:format cl:nil "Header header~%uint16 chn1~%uint16 chn2~%uint16 chn3~%uint16 chn4~%uint16 chn5~%uint16 chn6~%uint16 chn7~%uint16 chn8~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ppmchnls>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     2
     2
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ppmchnls>))
  "Converts a ROS message object to a list"
  (cl:list 'ppmchnls
    (cl:cons ':header (header msg))
    (cl:cons ':chn1 (chn1 msg))
    (cl:cons ':chn2 (chn2 msg))
    (cl:cons ':chn3 (chn3 msg))
    (cl:cons ':chn4 (chn4 msg))
    (cl:cons ':chn5 (chn5 msg))
    (cl:cons ':chn6 (chn6 msg))
    (cl:cons ':chn7 (chn7 msg))
    (cl:cons ':chn8 (chn8 msg))
))
