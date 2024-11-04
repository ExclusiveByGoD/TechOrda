# docker-mount

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `docker-mount`.
2. Скачать конфигурационный файл [jusan-docker-mount.conf][jusan-docker-mount-conf] с помощью `curl`.
3. Скачать конфигурационный файл [jusan-docker-mount.zip][jusan-docker-mount-zip] с помощью `curl`.
   Разархивировать архив с помощью `unzip`.
4. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 9999 на 80 порт контейнера;
   - имя контейнера `jusan-docker-mount`;
   - монтирует скачанный `jusan-docker-mount.conf` внутрь контейнера `/etc/nginx/conf.d/jusan-docker-mount.conf`;
   - монтирует распакованный `jusan-docker-mount.zip` внутрь контейнера. Определите куда нужно монтировать по конфигурационному файлу;
   - использует образ `nginx:mainline`.

5. Проверьте запросы с помощью `curl`:

   - `http://localhost:9999` - ожидаемый ответ: `<h1>Hello, from jusan-docker-mount</h1>`;
   - `http://localhost:9999/test` - ожидаемый ответ: `Singularity`;
   - `http://localhost:9999/token` - ожидаемый ответ: `Jusan`;

6. Посмотрите на логи `nginx`:

```bash
docker logs jusan-docker-mount
```

7. Все выполненные команды начиная со 2 шага, кроме 5 и 6, записать в файл `docker-mount/solution.sh`.

8. Запушить в репозиторий `jusan-docker`. В папке `docker-mount` должны быть:
   - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[jusan-docker-mount-conf]: https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
[jusan-docker-mount-zip]: https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-mount.sh

---

### Ответ

```bash
aseke@aseke-ThinkPad-E14:~$ curl -O https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.conf
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   110  100   110    0     0    428      0 --:--:-- --:--:-- --:--:--   429

aseke@aseke-ThinkPad-E14:~$ curl -O https://stepik.org/media/attachments/lesson/686238/jusan-docker-mount.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1557  100  1557    0     0   6306      0 --:--:-- --:--:-- --:--:--  6329

aseke@aseke-ThinkPad-E14:~$ unzip jusan-docker-mount.zip 
Archive:  jusan-docker-mount.zip
   creating: jusan-docker-mount/
  inflating: jusan-docker-mount/token  
  inflating: jusan-docker-mount/index.html  
  inflating: jusan-docker-mount/.DS_Store  
  inflating: __MACOSX/jusan-docker-mount/._.DS_Store  
  inflating: jusan-docker-mount/test

aseke@aseke-ThinkPad-E14:~$ sudo docker run -d --name jusan-docker-mount -p 9999:80 -v /home/aseke/jusan-docker-mount.conf:/etc/nginx/conf.d/jusan-docker-mount.conf -v /home/aseke/jusan-docker-mount/*:/var/www/example/* nginx:mainline
5731224da843835640a7ee9f4dca5b54e0ba8645a1b89aaa6a9a482a79219e44

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: example.com" http://localhost:9999
<h1>Hello, from jusan-docker-mount</h1>

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: example.com" http://localhost:9999/test
Singularity

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: example.com" http://localhost:9999/token
Jusan

aseke@aseke-ThinkPad-E14:~$ sudo docker logs jusan-docker-mount
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/11/04 05:06:26 [notice] 1#1: using the "epoll" event method
2024/11/04 05:06:26 [notice] 1#1: nginx/1.27.2
2024/11/04 05:06:26 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2024/11/04 05:06:26 [notice] 1#1: OS: Linux 6.8.0-48-generic
2024/11/04 05:06:26 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2024/11/04 05:06:26 [notice] 1#1: start worker processes
2024/11/04 05:06:26 [notice] 1#1: start worker process 29
2024/11/04 05:06:26 [notice] 1#1: start worker process 30
2024/11/04 05:06:26 [notice] 1#1: start worker process 31
2024/11/04 05:06:26 [notice] 1#1: start worker process 32
2024/11/04 05:06:26 [notice] 1#1: start worker process 33
2024/11/04 05:06:26 [notice] 1#1: start worker process 34
2024/11/04 05:06:26 [notice] 1#1: start worker process 35
2024/11/04 05:06:26 [notice] 1#1: start worker process 36
172.17.0.1 - - [04/Nov/2024:05:17:13 +0000] "GET / HTTP/1.1" 200 39 "-" "curl/7.81.0" "-"
172.17.0.1 - - [04/Nov/2024:05:17:19 +0000] "GET /test HTTP/1.1" 200 11 "-" "curl/7.81.0" "-"
172.17.0.1 - - [04/Nov/2024:05:17:23 +0000] "GET /token HTTP/1.1" 200 5 "-" "curl/7.81.0" "-"
aseke@aseke-ThinkPad-E14:~$ 
