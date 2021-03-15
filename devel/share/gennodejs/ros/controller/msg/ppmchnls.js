// Auto-generated. Do not edit!

// (in-package controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ppmchnls {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.chn1 = null;
      this.chn2 = null;
      this.chn3 = null;
      this.chn4 = null;
      this.chn5 = null;
      this.chn6 = null;
      this.chn7 = null;
      this.chn8 = null;
    }
    else {
      if (initObj.hasOwnProperty('chn1')) {
        this.chn1 = initObj.chn1
      }
      else {
        this.chn1 = 0;
      }
      if (initObj.hasOwnProperty('chn2')) {
        this.chn2 = initObj.chn2
      }
      else {
        this.chn2 = 0;
      }
      if (initObj.hasOwnProperty('chn3')) {
        this.chn3 = initObj.chn3
      }
      else {
        this.chn3 = 0;
      }
      if (initObj.hasOwnProperty('chn4')) {
        this.chn4 = initObj.chn4
      }
      else {
        this.chn4 = 0;
      }
      if (initObj.hasOwnProperty('chn5')) {
        this.chn5 = initObj.chn5
      }
      else {
        this.chn5 = 0;
      }
      if (initObj.hasOwnProperty('chn6')) {
        this.chn6 = initObj.chn6
      }
      else {
        this.chn6 = 0;
      }
      if (initObj.hasOwnProperty('chn7')) {
        this.chn7 = initObj.chn7
      }
      else {
        this.chn7 = 0;
      }
      if (initObj.hasOwnProperty('chn8')) {
        this.chn8 = initObj.chn8
      }
      else {
        this.chn8 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ppmchnls
    // Serialize message field [chn1]
    bufferOffset = _serializer.uint16(obj.chn1, buffer, bufferOffset);
    // Serialize message field [chn2]
    bufferOffset = _serializer.uint16(obj.chn2, buffer, bufferOffset);
    // Serialize message field [chn3]
    bufferOffset = _serializer.uint16(obj.chn3, buffer, bufferOffset);
    // Serialize message field [chn4]
    bufferOffset = _serializer.uint16(obj.chn4, buffer, bufferOffset);
    // Serialize message field [chn5]
    bufferOffset = _serializer.uint16(obj.chn5, buffer, bufferOffset);
    // Serialize message field [chn6]
    bufferOffset = _serializer.uint16(obj.chn6, buffer, bufferOffset);
    // Serialize message field [chn7]
    bufferOffset = _serializer.uint16(obj.chn7, buffer, bufferOffset);
    // Serialize message field [chn8]
    bufferOffset = _serializer.uint16(obj.chn8, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ppmchnls
    let len;
    let data = new ppmchnls(null);
    // Deserialize message field [chn1]
    data.chn1 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [chn2]
    data.chn2 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [chn3]
    data.chn3 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [chn4]
    data.chn4 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [chn5]
    data.chn5 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [chn6]
    data.chn6 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [chn7]
    data.chn7 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [chn8]
    data.chn8 = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'controller/ppmchnls';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '40ec51ccfeeb5a2284da850069525f99';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint16 chn1
    uint16 chn2
    uint16 chn3
    uint16 chn4
    uint16 chn5
    uint16 chn6
    uint16 chn7
    uint16 chn8
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ppmchnls(null);
    if (msg.chn1 !== undefined) {
      resolved.chn1 = msg.chn1;
    }
    else {
      resolved.chn1 = 0
    }

    if (msg.chn2 !== undefined) {
      resolved.chn2 = msg.chn2;
    }
    else {
      resolved.chn2 = 0
    }

    if (msg.chn3 !== undefined) {
      resolved.chn3 = msg.chn3;
    }
    else {
      resolved.chn3 = 0
    }

    if (msg.chn4 !== undefined) {
      resolved.chn4 = msg.chn4;
    }
    else {
      resolved.chn4 = 0
    }

    if (msg.chn5 !== undefined) {
      resolved.chn5 = msg.chn5;
    }
    else {
      resolved.chn5 = 0
    }

    if (msg.chn6 !== undefined) {
      resolved.chn6 = msg.chn6;
    }
    else {
      resolved.chn6 = 0
    }

    if (msg.chn7 !== undefined) {
      resolved.chn7 = msg.chn7;
    }
    else {
      resolved.chn7 = 0
    }

    if (msg.chn8 !== undefined) {
      resolved.chn8 = msg.chn8;
    }
    else {
      resolved.chn8 = 0
    }

    return resolved;
    }
};

module.exports = ppmchnls;
