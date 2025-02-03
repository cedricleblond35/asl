# DATABASE MYSQL ---------------------------------------------------------------------------------------------

#créer le conteneur de mysql
docker run --name mysql -e MYSQL_ROOT_PASSWORD=MYsql -p 3310:3306 -d docker.io/library/mysql
#demarrer le conteneur
docker start mysql
#rentrer ds le conteneur
docker exec -it mysql bash
# identifier
mysql -u root -p

#--------------------------------------------------------
python3.10 -m venv env
source env/bin/activate
#----------------------------------------------------------------------------------------------------------------------
create file
pip freeze > requirements.txt

* in env:
pip install -r requirements.txt



#lancer application
python3 app/app.py

# --------------------------------------------------------------------------------------------
#test unitaire
#Rentrer dans le repertoire app
python3 -m pytest tests -v