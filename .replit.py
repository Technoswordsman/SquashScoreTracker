modules = ["python-3.11", "postgresql-16"]

[nix]
channel = "stable-24_05"

[deployment]
deploymentTarget = "autoscale"
run = ["sh", "-c", "streamlit run main.py"]

[workflows]
runButton = "Project"

[[workflows.workflow]]
name = "Project"
mode = "parallel"
author = "agent"

[[workflows.workflow.tasks]]
task = "workflow.run"
args = "Squash Scorecard App"

[[workflows.workflow]]
name = "Squash Scorecard App"
author = "agent"

[workflows.workflow.metadata]
agentRequireRestartOnSave = false

[[workflows.workflow.tasks]]
task = "packager.installForAll"

[[workflows.workflow.tasks]]
task = "shell.exec"
args = "streamlit run main.py"
waitForPort = 5000

[[ports]]
localPort = 5000
externalPort = 80
