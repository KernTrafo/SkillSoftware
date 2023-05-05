# app

### Run with Docker
	- make sure you have an internet connection or prebuild images loaded
	- to load prebuilt images use:
		- docker load -i imagename.tar

	- start the database container:
		- docker run --name app_db -p 3306:3306 -e MYSQL_DATABASE='kerntrafo' -e MYSQL_ROOT_PASSWORD='@KTDB2021' -v db-data:/var/lib/kerntrafo_mysql -d mysql --sql-mode=""	
	- start and link the app container:
		- docker run --name app -d -p 8000:8000 -e DATABASE_URI='mysql+pymysql://root:@KTDB2021@app_db:3306/kerntrafo' --link app_db app_app
	- after an update of the app stop the container to be updated by executing: 
		- docker stop app
	- remove the app container:
		- docker rm app_app
	- load the new container:
		- docker load -i app.tar
	- start and link the app container again:
		- docker run --name app -d -p 8000:8000 -e DATABASE_URI='mysql+pymysql://root:@KTDB2021@app_db:3306/kerntrafo' --link app_db app_app 
	- navigate to localhost:8000

### export data from the Database:
	- to export the data app docker container
	- execute the command 
	- docker exec app -it /bin/bash -c "python export_data.py"
	- docker cp app:/home/kerntrafo/data_export_YYYY_MM_DD.csv .
	- the data is now in the current working directory

### Backup sql Table
docker exec app_db /usr/bin/mysqldump -u root --password=@KTDB2021 kerntrafo > backup.sql

### Restore Table from backup
cat backup.sql | docker exec -i app_db /usr/bin/mysql -u root --password=@KTDB2021 kerntrafo
