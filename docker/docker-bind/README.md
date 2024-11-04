# docker-bind

### Полезное

- [Use bind mounts](https://docs.docker.com/storage/bind-mounts/)

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `docker-bind`.
2. Скачать конфигурационный файл [nginx.conf](./nginx.conf) с помощью `curl`.
3. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 7777 на 80 порт контейнера;
   - имя контейнера `jusan-docker-bind`;
   - монтирует скачанный `nginx.conf` внутрь контейнера `/etc/nginx/nginx.conf`;
   - использует образ `nginx:mainline`.

4. Проверьте запрос `http://localhost:7777` с помощью `curl`. В ответ должно прийтие `Привет из Docker контейнера! 🐳`.
5. Посмотрите список запущенных контейнеров. Проверьте в списке, как отображается контейнер `jusan-docker-bind`.
6. Посмотрите на логи `nginx` командой:

```bash
docker logs jusan-docker-bind
```

7. Все выполненные команды в шаге 2 и 3 записать в файл `docker-bind/solution.sh`.

8. Запушить в репозиторий `jusan-docker`. В папке `docker-bind` должны быть:
   - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-bind.sh

---

### Ответ

```bash
aseke@aseke-ThinkPad-E14:~$ sudo docker run -d --name jusan-docker-bind -p 7777:80 -v /home/aseke/Projects/TechOrda/docker/docker-bind/nginx.conf:/etc/nginx/nginx.conf:ro nginx:mainline
a7a419f833afaa43430985fb9b9c6ab99b656755ab0cb8136e3e80e4340e5e34

aseke@aseke-ThinkPad-E14:~$ curl http://localhost:7777
Привет из Docker контейнера! 🐳

aseke@aseke-ThinkPad-E14:~$ sudo docker logs jusan-docker-bind
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/11/04 04:53:54 [notice] 1#1: using the "epoll" event method
2024/11/04 04:53:54 [notice] 1#1: nginx/1.27.2
2024/11/04 04:53:54 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2024/11/04 04:53:54 [notice] 1#1: OS: Linux 6.8.0-48-generic
2024/11/04 04:53:54 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2024/11/04 04:53:54 [notice] 1#1: start worker processes
2024/11/04 04:53:54 [notice] 1#1: start worker process 29
2024/11/04 04:53:54 [notice] 1#1: start worker process 30
2024/11/04 04:53:54 [notice] 1#1: start worker process 31
2024/11/04 04:53:54 [notice] 1#1: start worker process 32
2024/11/04 04:53:54 [notice] 1#1: start worker process 33
2024/11/04 04:53:54 [notice] 1#1: start worker process 34
2024/11/04 04:53:54 [notice] 1#1: start worker process 35
2024/11/04 04:53:54 [notice] 1#1: start worker process 36
172.17.0.1 - - [04/Nov/2024:04:53:59 +0000] "GET / HTTP/1.1" 203 52 "-" "curl/7.81.0" "-"

aseke@aseke-ThinkPad-E14:~$ sudo docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                   NAMES
a7a419f833af   nginx:mainline   "/docker-entrypoint.…"   35 seconds ago   Up 34 seconds   0.0.0.0:7777->80/tcp, :::7777->80/tcp   jusan-docker-bind