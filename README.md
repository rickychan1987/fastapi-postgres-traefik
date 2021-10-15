# fastapi-postgres-traefik
First go to app/main.py to adjust your email account in.</br>
$docker-compose down -v   #to ensure empty containers are running background</br>
$docker-compose -f docker-compose.prod.yml down -v    #to ensure empty containers are running background</br>

!------Building your container up------!</br>
$docker-compose up -d --build     #use this command to begin build up your container.</br>
$docker-compose up -d db      #if the container has issue wth above command buil to running, kindly seperately run commands.</br>
$docker-compose up        #kindly seperately run commands.</br>
$docker ps    #to check which port containers are running</br>
$docker-compose ps    #to check which port compose are running
