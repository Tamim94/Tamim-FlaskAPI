package main


deny[msg] {
  input.kind == "Deployment"
  input.spec.template.spec.securityContext.runAsUser == 0
  msg := "SECURITY ALERT: Containers must not run as root! Please change runAsUser to a non-zero value."
}