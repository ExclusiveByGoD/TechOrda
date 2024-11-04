# docker-run

Задания в данном модуле будут проверяться ментором в конце модуля.

Для сдачи данного модуля создайте репозиторий в ([ССЫЛКА GITHUB CLASSROOM]).

### Полезное

- [Установка Docker](https://docs.docker.com/get-docker/)

### Задание

1. Установить Docker, если еще не установлен на вашем компьютере.
2. Запустить контейнер на порту `8888` из официального образа `nginx`:

```bash
docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
```

3. Вывести список активных контейнеров:

```bash
docker ps
```

4. Проверьте запрос на `http://localhost:8888` с помощью `curl`. Должно появиться приветственное сообщение от `nginx`.
5. Остановить запущенный контейнер:

```bash
docker stop jsn-dkr-run
```

6. Вывести список активных контейнеров, чтобы убедиться что нашего контейнера нет в списке.
7. Проверьте запрос `http://localhost:8888` с помощью `curl`. Должна появиться ошибка, так как наш контейнер был остановлен.
8. Вывести список всех контейнеров. В нем должен появиться наш остановленный контейнер.

```bash
docker ps -a
```

9. Все выполенные команды `docker` записать в репозиторий в файл `docker-run/solution.sh`. В скрипте не должно быть команд `curl`.
   Запушить в гит.

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-run.sh

---

### Ответ

```bash
aseke@aseke-ThinkPad-E14:~$ docker
Команда «docker» не найдена, но может быть установлена с помощью:
sudo snap install docker         # version 24.0.5, or
sudo apt  install docker.io      # version 24.0.7-0ubuntu2~22.04.1
sudo apt  install podman-docker  # version 3.4.4+ds1-1ubuntu1.22.04.2
См. 'snap info docker', чтобы посмотреть дополнительные версии.

aseke@aseke-ThinkPad-E14:~$ sudo apt  install docker.io
[sudo] пароль для aseke:          
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово         
Будут установлены следующие дополнительные пакеты:
  bridge-utils containerd pigz runc ubuntu-fan
Предлагаемые пакеты:
  ifupdown aufs-tools btrfs-progs cgroupfs-mount | cgroup-lite debootstrap
  docker-doc rinse zfs-fuse | zfsutils
Следующие НОВЫЕ пакеты будут установлены:
  bridge-utils containerd docker.io pigz runc ubuntu-fan
Обновлено 0 пакетов, установлено 6 новых пакетов, для удаления отмечено 0 пакетов, и 2 пакетов не обновлено.
Необходимо скачать 75,2 MB архивов.
После данной операции объём занятого дискового пространства возрастёт на 283 MB.
Хотите продолжить? [Д/н] y
Пол:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 pigz amd64 2.6-1 [63,6 kB]
Пол:2 http://kz.archive.ubuntu.com/ubuntu jammy-updates/main amd64 runc amd64 1.1.12-0ubuntu2~22.04.1 [8 405 kB]
Пол:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 bridge-utils amd64 1.7-1ubuntu3 [34,4 kB]
Пол:4 http://archive.ubuntu.com/ubuntu jammy/universe amd64 ubuntu-fan all 0.12.16 [35,2 kB]
Пол:5 http://kz.archive.ubuntu.com/ubuntu jammy-updates/main amd64 containerd amd64 1.7.12-0ubuntu2~22.04.1 [37,8 MB]
Пол:6 http://kz.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 docker.io amd64 24.0.7-0ubuntu2~22.04.1 [28,8 MB]
Получено 75,2 MB за 16с (4 726 kB/s)                                           
Предварительная настройка пакетов …
Выбор ранее не выбранного пакета pigz.
(Чтение базы данных … на данный момент установлено 333102 файла и каталога.)
Подготовка к распаковке …/0-pigz_2.6-1_amd64.deb …
Распаковывается pigz (2.6-1) …
Выбор ранее не выбранного пакета bridge-utils.
Подготовка к распаковке …/1-bridge-utils_1.7-1ubuntu3_amd64.deb …
Распаковывается bridge-utils (1.7-1ubuntu3) …
Выбор ранее не выбранного пакета runc.
Подготовка к распаковке …/2-runc_1.1.12-0ubuntu2~22.04.1_amd64.deb …
Распаковывается runc (1.1.12-0ubuntu2~22.04.1) …
Выбор ранее не выбранного пакета containerd.
Подготовка к распаковке …/3-containerd_1.7.12-0ubuntu2~22.04.1_amd64.deb …
Распаковывается containerd (1.7.12-0ubuntu2~22.04.1) …
Выбор ранее не выбранного пакета docker.io.
Подготовка к распаковке …/4-docker.io_24.0.7-0ubuntu2~22.04.1_amd64.deb …
Распаковывается docker.io (24.0.7-0ubuntu2~22.04.1) …
Выбор ранее не выбранного пакета ubuntu-fan.
Подготовка к распаковке …/5-ubuntu-fan_0.12.16_all.deb …
Распаковывается ubuntu-fan (0.12.16) …
Настраивается пакет runc (1.1.12-0ubuntu2~22.04.1) …
Настраивается пакет bridge-utils (1.7-1ubuntu3) …
Настраивается пакет pigz (2.6-1) …
Настраивается пакет containerd (1.7.12-0ubuntu2~22.04.1) …
Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service →
 /lib/systemd/system/containerd.service.
Настраивается пакет ubuntu-fan (0.12.16) …
Created symlink /etc/systemd/system/multi-user.target.wants/ubuntu-fan.service →
 /lib/systemd/system/ubuntu-fan.service.
Настраивается пакет docker.io (24.0.7-0ubuntu2~22.04.1) …
Добавляется группа «docker» (GID 141) ...
Готово.
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /li
b/systemd/system/docker.service.
Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /lib/sy
stemd/system/docker.socket.
Обрабатываются триггеры для man-db (2.10.2-1) …

aseke@aseke-ThinkPad-E14:~$ docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/create?name=jsn-dkr-run": dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.

aseke@aseke-ThinkPad-E14:~$ sudo docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
Unable to find image 'nginx:mainline' locally
mainline: Pulling from library/nginx
a480a496ba95: Pull complete 
f3ace1b8ce45: Pull complete 
11d6fdd0e8a7: Pull complete 
f1091da6fd5c: Pull complete 
40eea07b53d8: Pull complete 
6476794e50f4: Pull complete 
70850b3ec6b2: Pull complete 
Digest: sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb
Status: Downloaded newer image for nginx:mainline
1d538f2939a1a5b5cfe7a9debb88791bb3d7920e8850c82ecd5a54bff8a9fe39

aseke@aseke-ThinkPad-E14:~$ curl http://localhost:8888
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

aseke@aseke-ThinkPad-E14:~$ docker ps
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied

aseke@aseke-ThinkPad-E14:~$ sudo docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                   NAMES
1d538f2939a1   nginx:mainline   "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:8888->80/tcp, :::8888->80/tcp   jsn-dkr-run

aseke@aseke-ThinkPad-E14:~$ sudo docker stop jsn-dkr-run
jsn-dkr-run

aseke@aseke-ThinkPad-E14:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

aseke@aseke-ThinkPad-E14:~$ sudo docker ps -a
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS                     PORTS     NAMES
1d538f2939a1   nginx:mainline   "/docker-entrypoint.…"   2 minutes ago   Exited (0) 6 seconds ago             jsn-dkr-run