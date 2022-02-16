<h1>DevOps internship dimploma</h1>

<b>Known problems:</b>
- <s>https://swapi.dev/ sometimes return 'ERROR 404' because of missing persons (i.e. https://swapi.dev/api/people/17) and ships (i.e. https://swapi.dev/api/starships/1/).</s>
- Some persons have more than one starship (i.e. https://swapi.dev/api/people/10 have 5 starships).

<b>Known bugs:</b>
<s>- Empty lines processing.</s>
<s>- Filling data cells by data from previous iteration.</s>

<b>TODO:</b>
- To create table for linking starships and persons.
- To write query to display output.
- Add flask support to display output.

<b><i>Contents:</i></b>
- <b>create_db.py</b> script for creating tables in database.
- <b>db_check.py</b> script for checking something in database.
- <b>people.json</b> json structure for 'people' reply.
- <b>ships.json</b> json structure for 'starships' reply.
- <b>work_with_data.py</b> main script for retrieving data from site and pushing them to database.
