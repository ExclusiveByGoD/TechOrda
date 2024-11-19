# nginx-auth

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html)
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip). Установите авторизованный вход для учетки: `design:SteveJobs1955`, т.е. логин `design`, пароль `SteveJobs1955`.
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip). Установите авторизованный вход для учетки: `marketing:marketingP@ssword`.
6. Учетка `design` не должна иметь доступ на другие пути, тоже самое касается других учеток.

---

### Ответ
```bash

aseke@aseke-ThinkPad-E14:/etc/nginx/conf.d$ curl -u 'design:SteveJobs1955' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/images/sleep.png
curl -u 'design:SteveJobs1955' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/images/flower.png
curl -u 'design:SteveJobs1955' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/images/glasses.png
curl -u 'design:SteveJobs1955' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/images/gray-animal.jpeg
curl -u 'design:SteveJobs1955' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/images/mafia.png
curl -u 'marketing:marketingP@ssword' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/gifs/sad.gif
curl -u 'marketing:marketingP@ssword' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/gifs/jam.gif
curl -u 'marketing:marketingP@ssword' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/gifs/dancing.gif
curl -u 'marketing:marketingP@ssword' -s -w "%{size_download}\n" -o /dev/null http://localhost:8080/
curl -u 'marketing:marketingP@ssword' -I http://localhost:8080/images/sleep.png
curl -u 'design:SteveJobs1955' -I http://localhost:8080/gifs/dancing.gif
curl -u 'security:CuteCats<33' -I http://localhost:8080/gifs/dancing.gif
curl -u 'security:CuteCats<33' -I http://localhost:8080/images/sleep.png
153
153
153
153
153
153
153
153
153
HTTP/1.1 401 Unauthorized
Server: nginx/1.27.2
Date: Sat, 19 Oct 2024 19:47:02 GMT
Content-Type: text/html
Content-Length: 179
Connection: keep-alive
WWW-Authenticate: Basic realm="Приватный сайт"

HTTP/1.1 401 Unauthorized
Server: nginx/1.27.2
Date: Sat, 19 Oct 2024 19:47:02 GMT
Content-Type: text/html
Content-Length: 179
Connection: keep-alive
WWW-Authenticate: Basic realm="Приватный сайт"

HTTP/1.1 401 Unauthorized
Server: nginx/1.27.2
Date: Sat, 19 Oct 2024 19:47:02 GMT
Content-Type: text/html
Content-Length: 179
Connection: keep-alive
WWW-Authenticate: Basic realm="Приватный сайт"

HTTP/1.1 401 Unauthorized
Server: nginx/1.27.2
Date: Sat, 19 Oct 2024 19:47:02 GMT
Content-Type: text/html
Content-Length: 179
Connection: keep-alive
WWW-Authenticate: Basic realm="Приватный сайт"

aseke@aseke-ThinkPad-E14:/etc/nginx/conf.d$ cat example.com.conf 
server {
    listen 8080;
    server_name example.com;

    location / {
        root /home/aseke/task-nginx;
        index index.html;
    }

    location /images {
        root /home/aseke/task-nginx/images;
        auth_basic "Приватный сайт";
        auth_basic_user_file /etc/nginx/.de_passwd;
    }

    location /gifs {
        root /home/aseke/task-nginx/gifs;
        auth_basic "Приватный сайт";
        auth_basic_user_file /etc/nginx/.mar_passwd;
    }

    location /secret_word {
        return 201 'jusan-nginx-locations';
        add_header Content-Type text/plain;
    }
}