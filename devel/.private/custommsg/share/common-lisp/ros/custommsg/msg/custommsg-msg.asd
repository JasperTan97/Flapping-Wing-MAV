
(cl:in-package :asdf)

(defsystem "custommsg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "kinematicstamped" :depends-on ("_package_kinematicstamped"))
    (:file "_package_kinematicstamped" :depends-on ("_package"))
    (:file "ppmchnls" :depends-on ("_package_ppmchnls"))
    (:file "_package_ppmchnls" :depends-on ("_package"))
  ))