# dockerfile

В данном задании научимся собирать свой образ с приложением с помощью Dockerfile.

Dockerfile - это файл, описывающий команды сборки образа контейнера.

### Полезное

- [Изучаем Docker: файлы Dockerfile](https://habr.com/ru/company/ruvds/blog/439980/)
- [Dockerfile Tutorial](https://docker-curriculum.com/#dockerfile)

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `dockerfile`.
2. Скачать конфигурационный файл [jusan-dockerfile.conf][jusan-dockerfile-conf] с помощью `curl`.
3. Скачать конфигурационный файл [jusan-dockerfile.zip][jusan-dockerfile-zip] с помощью `curl`.
   Разархивировать архив с помощью `unzip`.
4. Создать Dockerfile, который:

   - использует базовый образ `nginx:mainline`;
   - копирует `jusan-dockerfile.conf` в `/etc/nginx/conf.d/jusan-dockerfile.conf`
   - копирует распакованный `jusan-dockerfile.zip`. Определите куда нужно монтировать по конфигурационному файлу.

5. Произвести сборку образа с именем `nginx` и тегом `jusan-dockerfile`.
6. Проверьте на наличие своего образа в вашей системе, перечислите все образы `docker images`.
7. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 6060 на 80 порт контейнера;
   - имя контейнера `jusan-dockerfile`;
   - использует наш собранный образ.

8. Проверьте запросы с помощью `curl`:

   - `http://localhost:6060` - ожидаемый ответ: `<h1>Hello, from jusan-dockerfile!</h1>`;
   - `http://localhost:6060/dockerfile` - ожидаемый ответ: `FROM nginx:mainline`;
   - `http://localhost:6060/secret` - ожидаемый ответ: `jusan-dockerfile`;
   - `http://localhost:6060/jusan` - ожидаемый ответ: `singularity`;

9. Команды из шагов 2, 3, 5, 7 записать в файл `dockerfile/solution.sh`.
10. Запушить в репозиторий `jusan-docker`. В папке `dockerfile` должны быть:
    - получившийся `Dockerfile`.
    - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[jusan-dockerfile-conf]: https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf
[jusan-dockerfile-zip]: https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip
[tester]: https://stepik.org/media/attachments/lesson/691221/tester-dockerfile.sh

---

### Ответ

```bash
aseke@aseke-ThinkPad-E14:~$ curl -O https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   229  100   229    0     0    559      0 --:--:-- --:--:-- --:--:--   561

aseke@aseke-ThinkPad-E14:~$ curl -O https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   676  100   676    0     0   2597      0 --:--:-- --:--:-- --:--:--  2600

aseke@aseke-ThinkPad-E14:~$ unzip jusan-dockerfile.zip 
Archive:  jusan-dockerfile.zip
   creating: jusan-dockerfile/
  inflating: jusan-dockerfile/index.html  
  inflating: jusan-dockerfile/dockerfile

aseke@aseke-ThinkPad-E14:~$ cat << EOF > Dockerfile
> FROM nginx:mainline
> COPY jusan-dockerfile.conf /etc/nginx/conf.d/jusan-dockerfile.conf
> COPY jusan-dockerfile /var/www/jusan-dockerfile
EOF

aseke@aseke-ThinkPad-E14:~$ cat Dockerfile
FROM nginx:mainline
COPY jusan-dockerfile.conf /etc/nginx/conf.d/jusan-dockerfile.conf
COPY jusan-dockerfile /var/www/jusan-dockerfile

aseke@aseke-ThinkPad-E14:~$ sudo docker build -t nginx:jusan-dockerfile .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  7.809GB
Step 1/3 : FROM nginx:mainline
 ---> 3b25b682ea82
Step 2/3 : COPY jusan-dockerfile.conf /etc/nginx/conf.d/jusan-dockerfile.conf
 ---> 99a0f66be2c1
Step 3/3 : COPY jusan-dockerfile /var/www/jusan-dockerfile
 ---> 4b74f3123de3
Successfully built 4b74f3123de3
Successfully tagged nginx:jusan-dockerfile

aseke@aseke-ThinkPad-E14:~$ sudo docker images
REPOSITORY   TAG                IMAGE ID       CREATED          SIZE
nginx        jusan-dockerfile   4b74f3123de3   13 seconds ago   192MB
nginx        mainline           3b25b682ea82   4 weeks ago      192MB

aseke@aseke-ThinkPad-E14:~$ sudo docker run -d --name jusan-dockerfile -p 6060:80 nginx:jusan-dockerfile
47351aa869c4e60830b9de7b9eaa361b732a1b9fc29ea798243a4e4ba4c7e2de

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: jusan.dockerfile" http://localhost:6060
<h1>Hello, from jusan-dockerfile!</h1>

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: jusan.dockerfile" http://localhost:6060/dockerfile
FROM nginx:mainline

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: jusan.dockerfile" http://localhost:6060/secret
jusan-dockerfile

aseke@aseke-ThinkPad-E14:~$ curl -H "Host: jusan.dockerfile" http://localhost:6060/jusan
singularity