# fastapi-postgres-traefik
First go to app/main.py to adjust your email account in.
$docker-compose down -v   #to ensure empty containers are running background
$docker-compose -f docker-compose.prod.yml down -v    #to ensure empty containers are running background

!------Building your container up------!
$docker-compose up -d --build     #use this command to begin build up your container.
$docker-compose up -d db      #if the container has issue wth above command buil to running, kindly seperately run commands.
$docker-compose up        #kindly seperately run commands.
