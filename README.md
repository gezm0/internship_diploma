<h1>DevOps internship dimploma</h1>

<b>Current status:</b><br><br>
Ready to start phase display result through web-server.<br><br>

<b>Known problems:</b>
- <s>https://swapi.dev/ sometimes return 'ERROR 404' because of missing persons (i.e. https://swapi.dev/api/people/17) and ships (i.e. https://swapi.dev/api/starships/1/).</s>
- <s>Some persons have more than one starship (i.e. https://swapi.dev/api/people/10 have 5 starships).</s>

<b>Known bugs:</b>
- <s>Empty lines processing.</s>
- <s>Filling data cells by data from previous iteration.</s>
- Inefficient ugly SQL query with not quite desired result. Need to rework with joins using, but at the end after all necessary diploma stages.

<b>TODO:</b>
- <s>Fill 'ships_id' column with ships_id_list.</s>
- <s>Rework script for separate person lines with each starship (not several ships in one person line).</s>
- <s>Write query to display output.</s>
- Maby split tasks of pulling data about ships and persons to different scripts. 
- Clean out repo a bit.
- Add flask support to display output.

<b><i>Contents:</i></b>
- <b>app_back</b> directory with backend app for deployment
- <b>app_front</b> directory with frontend app for deployment
- <b>app_infra</b> directory with service apps for deployment (for create and delete database schemas)
- <b>aws_infrastructure</b> directory with Terraform manifests for AWS infrastructure deployment
- <b>k8s</b> directory with Kubernetes manifests for K8S infrastructure deployment
<br>
- <b>db_create_tables.py</b> script for creating tables in database.
- <b>db_drop_tables.py</b> script for deleting tables in database.
- <b>people.json</b> json structure for 'people' reply.
- <b>script_output.py</b> Script with query to display desired output.
- <b>ships.json</b> json structure for 'starships' reply.
- <b>test.py</b> script for testing new features and significant code change.
- <b>work_with_data.py</b> main script for retrieving data from site and pushing them to database.
- <b>work_with_data_new.py</b> Last version of main script for retrieving data from site and pushing them to database.
# Variables:
Through variables for AWS and K8S infrastructure:<br><br>
<b>TF_VAR_db_user</b> for database user.<br>
<b>TF_VAR_db_password</b> for database password.<br>
<b>TF_VAR_db_name</b> for database name.<br>
<b>db_host</b> for database endpoint (host).<br><br>
More information <a href="https://github.com/gezm0/internship_diploma/tree/main/aws-infrastructure#readme">here</a>.
