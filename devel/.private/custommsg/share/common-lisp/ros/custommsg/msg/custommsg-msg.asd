
(cl:in-package :asdf)

(defsystem "custommsg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ppmchnls" :depends-on ("_package_ppmchnls"))
    (:file "_package_ppmchnls" :depends-on ("_package"))
  ))