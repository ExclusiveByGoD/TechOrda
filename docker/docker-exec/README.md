# docker-exec

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `docker-exec`.
2. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 8181 на 80 порт контейнера;
   - имя контейнера `jusan-docker-exec`;
   - использует образ `nginx:mainline`.

3. Зайти в терминал контейнера `jusan-docker-exec`.
4. Создать новый конфигурационный файл для nginx.

```bash
cat << EOF > /etc/nginx/conf.d/jusan-docker-exec.conf
server {
    listen 80;
    server_name jusan.singularity;

    location / {return 200 'Hello, from jusan-docker-exec';}
    location /home {return 201 'This is my home!';}
    location /about {return 202 'I am just an exercise!';}
}
EOF
```

5. Перезагрузите nginx внутри контейнера.
6. Выйти из терминала контейнера
7. Проверьте запросы с помощью `curl`:

   - `http://localhost:8181` - ожидаемый ответ: `Hello, from jusan-docker-exec`;
   - `http://localhost:8181/home` - ожидаемый ответ: `This is my home!`;
   - `http://localhost:8181/about` - ожидаемый ответ: `I am just an exercise!`;

8. Посмотрите на логи `nginx`:

```bash
docker logs jusan-docker-exec
```

7. Все выполненные команды начиная со 2 шага, кроме 7 и 8, записать в файл `docker-exec/solution.sh`.
8. Запушить в репозиторий `jusan-docker`. В папке `docker-exec` должны быть:
   - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-exec.sh

---

### Ответ

```bash

aseke@aseke-ThinkPad-E14:~$ sudo docker run -d --name jusan-docker-exec -p 8181:80 nginx:mainline
d52d34c01cfe9b012c7d143c5f2942c856b5ec34d53f5f5ff380184e54af2f10

aseke@aseke-ThinkPad-E14:~$ sudo docker exec -ti jusan-docker-exec bash
root@d52d34c01cfe:/# cat << EOF > /etc/nginx/conf.d/jusan-docker-exec.conf
server {
    listen 80;
    server_name jusan.singularity;

    location / {return 200 'Hello, from jusan-docker-exec';}
    location /home {return 201 'This is my home!';}
    location /about {return 202 'I am just an exercise!';}
}
> 
> EOF

root@d52d34c01cfe:/# systemctl restart nginx
bash: systemctl: command not found

root@d52d34c01cfe:/# /etc/init.d/nginx restart
Restarting nginx: nginx

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: jusan.singularity" http://localhost:8181
curl: (7) Failed to connect to localhost port 8181 after 0 ms: В соединении отказано

aseke@aseke-ThinkPad-E14:~$ sudo docker ps -a
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS                          PORTS     NAMES
d52d34c01cfe   nginx:mainline   "/docker-entrypoint.…"   2 minutes ago   Exited (0) About a minute ago             jusan-docker-exec

aseke@aseke-ThinkPad-E14:~$ sudo docker start jusan-docker-exec
jusan-docker-exec

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: jusan.singularity" http://localhost:8181
Hello, from jusan-docker-exec

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: jusan.singularity" http://localhost:8181/home
This is my home!

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: jusan.singularity" http://localhost:8181/about
I am just an exercise!

aseke@aseke-ThinkPad-E14:~$ sudo docker logs jusan-docker-exec
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/11/04 05:26:17 [notice] 1#1: using the "epoll" event method
2024/11/04 05:26:17 [notice] 1#1: nginx/1.27.2
2024/11/04 05:26:17 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2024/11/04 05:26:17 [notice] 1#1: OS: Linux 6.8.0-48-generic
2024/11/04 05:26:17 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2024/11/04 05:26:17 [notice] 1#1: start worker processes
2024/11/04 05:26:17 [notice] 1#1: start worker process 28
2024/11/04 05:26:17 [notice] 1#1: start worker process 29
2024/11/04 05:26:17 [notice] 1#1: start worker process 30
2024/11/04 05:26:17 [notice] 1#1: start worker process 31
2024/11/04 05:26:17 [notice] 1#1: start worker process 32
2024/11/04 05:26:17 [notice] 1#1: start worker process 33
2024/11/04 05:26:17 [notice] 1#1: start worker process 34
2024/11/04 05:26:17 [notice] 1#1: start worker process 35
2024/11/04 05:28:09 [notice] 1#1: signal 15 (SIGTERM) received from 49, exiting
2024/11/04 05:28:09 [notice] 34#34: exiting
2024/11/04 05:28:09 [notice] 31#31: exiting
2024/11/04 05:28:09 [notice] 33#33: exiting
2024/11/04 05:28:09 [notice] 32#32: exiting
2024/11/04 05:28:09 [notice] 28#28: exiting
2024/11/04 05:28:09 [notice] 30#30: exiting
2024/11/04 05:28:09 [notice] 32#32: exit
2024/11/04 05:28:09 [notice] 28#28: exit
2024/11/04 05:28:09 [notice] 33#33: exit
2024/11/04 05:28:09 [notice] 31#31: exit
2024/11/04 05:28:09 [notice] 30#30: exit
2024/11/04 05:28:09 [notice] 34#34: exit
2024/11/04 05:28:09 [notice] 29#29: exiting
2024/11/04 05:28:09 [notice] 29#29: exit
2024/11/04 05:28:09 [notice] 35#35: exiting
2024/11/04 05:28:09 [notice] 35#35: exit
2024/11/04 05:28:09 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2024/11/04 05:28:09 [notice] 1#1: worker process 29 exited with code 0
2024/11/04 05:28:09 [notice] 1#1: signal 29 (SIGIO) received
2024/11/04 05:28:09 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2024/11/04 05:28:09 [notice] 1#1: worker process 31 exited with code 0
2024/11/04 05:28:09 [notice] 1#1: signal 29 (SIGIO) received
2024/11/04 05:28:09 [notice] 1#1: signal 17 (SIGCHLD) received from 28
2024/11/04 05:28:09 [notice] 1#1: worker process 28 exited with code 0
2024/11/04 05:28:09 [notice] 1#1: worker process 35 exited with code 0
2024/11/04 05:28:09 [notice] 1#1: signal 29 (SIGIO) received
2024/11/04 05:28:09 [notice] 1#1: signal 17 (SIGCHLD) received from 35
2024/11/04 05:28:09 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2024/11/04 05:28:09 [notice] 1#1: worker process 32 exited with code 0
2024/11/04 05:28:09 [notice] 1#1: signal 29 (SIGIO) received
2024/11/04 05:28:09 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2024/11/04 05:28:09 [notice] 1#1: worker process 33 exited with code 0
2024/11/04 05:28:09 [notice] 1#1: worker process 30 exited with code 0
2024/11/04 05:28:09 [notice] 1#1: signal 29 (SIGIO) received
2024/11/04 05:28:09 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2024/11/04 05:28:09 [notice] 1#1: signal 17 (SIGCHLD) received from 34
2024/11/04 05:28:09 [notice] 1#1: worker process 34 exited with code 0
2024/11/04 05:28:09 [notice] 1#1: exit
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: IPv6 listen already enabled
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/11/04 05:29:22 [notice] 1#1: using the "epoll" event method
2024/11/04 05:29:22 [notice] 1#1: nginx/1.27.2
2024/11/04 05:29:22 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2024/11/04 05:29:22 [notice] 1#1: OS: Linux 6.8.0-48-generic
2024/11/04 05:29:22 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2024/11/04 05:29:22 [notice] 1#1: start worker processes
2024/11/04 05:29:22 [notice] 1#1: start worker process 22
2024/11/04 05:29:22 [notice] 1#1: start worker process 23
2024/11/04 05:29:22 [notice] 1#1: start worker process 24
2024/11/04 05:29:22 [notice] 1#1: start worker process 25
2024/11/04 05:29:22 [notice] 1#1: start worker process 26
2024/11/04 05:29:22 [notice] 1#1: start worker process 27
2024/11/04 05:29:22 [notice] 1#1: start worker process 28
2024/11/04 05:29:22 [notice] 1#1: start worker process 29
172.17.0.1 - - [04/Nov/2024:05:29:26 +0000] "GET / HTTP/1.1" 200 29 "-" "curl/7.81.0" "-"
172.17.0.1 - - [04/Nov/2024:05:29:32 +0000] "GET /home HTTP/1.1" 201 16 "-" "curl/7.81.0" "-"
172.17.0.1 - - [04/Nov/2024:05:29:37 +0000] "GET /about HTTP/1.1" 202 22 "-" "curl/7.81.0" "-"
aseke@aseke-ThinkPad-E14:~$ 