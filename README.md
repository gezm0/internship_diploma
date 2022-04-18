<h1>DevOps internship dimploma</h1>

<b>Current status:</b><br><br>
Application part. Web service ready.<br>
Infrastructure part. Manual deployment in AWS EKS infrastructure passed successfully. <br><br>
![Screenshot 2022-04-18 152056](https://user-images.githubusercontent.com/94368360/163809652-6be85562-82f6-42cb-bd33-9ea1b7abb812.png)
![Screenshot 2022-04-18 152240](https://user-images.githubusercontent.com/94368360/163809660-e50ec598-c9dc-45d5-8a7b-04d14dc053f1.png)

<b>Known problems:</b>
- <s>https://swapi.dev/ sometimes return 'ERROR 404' because of missing persons (i.e. https://swapi.dev/api/people/17) and ships (i.e. https://swapi.dev/api/starships/1/).</s>
- <s>Some persons have more than one starship (i.e. https://swapi.dev/api/people/10 have 5 starships).</s>

<b>Known bugs:</b>
- <s>Empty lines processing.</s>
- <s>Filling data cells by data from previous iteration.</s>
- <s>Inefficient ugly SQL query with not quite desired result. Need to rework with joins using, but at the end after all necessary diploma stages.</s> Just added another complete table. Result is still a bit undesirable.

<b>TODO:</b>
- <s>Fill 'ships_id' column with ships_id_list.</s>
- <s>Rework script for separate person lines with each starship (not several ships in one person line).</s>
- <s>Write query to display output.</s>
- <s>Maby split tasks of pulling data about ships and persons to different scripts.</s> Nope.
- <s>Clean out repo a bit.</s> I was reorganized hierarchy a bit.
- <s>Add flask support to display output.</s>

<b><i>Contents:</i></b>
- <b>app_back</b> directory with backend app for deployment
- <b>app_front</b> directory with frontend app for deployment
- <b>app_infra</b> directory with service apps for deployment (for create and delete database schemas)
- <b>aws_infrastructure</b> directory with Terraform manifests for AWS infrastructure deployment
- <b>dev</b> directory with application development files
- <b>k8s</b> directory with Kubernetes manifests for K8S infrastructure deployment
# Variables:
Through variables for AWS and K8S infrastructure:<br><br>
<b>TF_VAR_db_user</b> for database user.<br>
<b>TF_VAR_db_password</b> for database password.<br>
<b>TF_VAR_db_name</b> for database name.<br>
<b>db_host</b> for database endpoint (host).<br><br>
More information <a href="https://github.com/gezm0/internship_diploma/tree/main/aws-infrastructure#readme">here</a>.
