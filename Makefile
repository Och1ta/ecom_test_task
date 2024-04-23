up:
    docker-compose -f docker-compose.yml down -v
    docker-compose up -d --build

down:
    docker-compose -f docker-compose.yml down -v