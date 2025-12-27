##MLFLOW Library used in all record on project wllbe recorded and compare to each other and visulize in all graps.

import dagshub
dagshub.init(repo_owner='rajputshrinath349', repo_name='MLFLOW', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

