# Restaraunt Menu

---
### Description

Релизованы два endpoint'а:
- список топпингов
- список еды с возможностью фильтрации по:
  - is_special
  - is_vegan
  - toppings__name (названию топпингов)

### Quickstart


1. Скопировать .envs
```
cp .env.local.dist .env.local
cp .env.local.db.dist .env.local.db
``` 
2. Запустить
```
docker-compose -f docker-compose.local.yml up -d --build
```
3. Документация
http://0.0.0.0:8001/api/v1/schema/swagger-ui/
