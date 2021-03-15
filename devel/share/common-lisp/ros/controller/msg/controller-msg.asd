
(cl:in-package :asdf)

(defsystem "controller-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ppmchnls" :depends-on ("_package_ppmchnls"))
    (:file "_package_ppmchnls" :depends-on ("_package"))
  ))