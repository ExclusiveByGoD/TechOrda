# docker-compose

Скрипты запуска `docker run` бывают очень длинными. Такой скрипт сложно в дальнейшем
поддерживать. Более удобный способ по конфигурации и запуска контейнеров является
запуск через `docker-compose`.

В данном задании запустим наш предыдущий образ через `docker-compose`.

### Полезное

- [Overview of Docker Compose](https://docs.docker.com/compose/)
- [Использование Docker Compose для чайников](https://losst.ru/ispolzovanie-docker-dlya-chajnikov)

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `docker-compose`.
2. Напишите `docker-compose.yml`, который:

   - в сервисах имеет сервис `api`;
   - сервис `api` использует образ `jusan-fastapi-final:dockerized`;
   - сервис `api` перенаправляет запрос с хостового порта 8282 на 8080 порт контейнера;
   - сервис `api` имеет имя контейнера `jusan-compose`;

3. Запустить `docker-compose` на фоне. Проверьте работу сервисов.
4. Запушить в гит получившийся `docker-compose.yml`.

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-compose.sh

---

### Ответ

```bash
root@aseke-ThinkPad-E14:/home/aseke/Projects/fastapi# ls
collection.json  docker-compose.yml  Dockerfile  main.py  __pycache__  README.md  requirements.txt

root@aseke-ThinkPad-E14:/home/aseke/Projects/fastapi# cat docker-compose.yml 
version: '3.8'

services:
  api:
    image: jusan-fastapi-final:dockerized
    container_name: jusan-compose
    ports:
      - "8282:8080"
    restart: unless-stopped

root@aseke-ThinkPad-E14:/home/aseke/Projects/fastapi# docker-compose up -d
Creating network "fastapi_default" with the default driver
Creating jusan-compose ... done

root@aseke-ThinkPad-E14:/home/aseke/Projects/fastapi# curl -X PUT -d '{"element":"Microsoft"}' -H 'Content-Type: application/json' http://localhost:8282/list
{"result":["Microsoft"]}

root@aseke-ThinkPad-E14:/home/aseke/Projects/fastapi# docker-compose ps
    Name                   Command               State                    Ports                  
-------------------------------------------------------------------------------------------------
jusan-compose   uvicorn main:app --host 0. ...   Up      0.0.0.0:8282->8080/tcp,:::8282->8080/tcp