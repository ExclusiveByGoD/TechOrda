# nginx-ip

Защита ценных ресурсов и сервисов в Интернете должна осуществляться поэтапно. NGINX является одним из этих этапов.

Директива `deny` блокирует доступ к конкретному блоку, а директива `allow` может использоваться для
разрешения подмножества заблокированного доступа. Вы можете использовать IP-адреса, IPv4 или IPv6, и ключевое слово `all`.

Как правило, при защите ресурса можно запретить доступ для всех к определенному `location` блоку и разрешить доступ только с определенных IP адресов.

### Полезные ссылки

- [Restricting Access by IP Address ](https://docs.nginx.com/nginx/admin-guide/security-controls/controlling-access-proxied-tcp/)
- [How to block/allow IP-addresses in Nginx](https://support.hypernode.com/en/hypernode/nginx/how-to-block-allow-ip-addresses-in-nginx)

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` равным значению `example.com`.
3. Добавьте `location /secret_word`, который возвращает строку `jusan-nginx-ip` со статусом `203`. Разрешите доступ к блоку из `192.0.0.1/20` кроме `192.0.0.1` и запретите все остальные.
4. Отправьте получившийся результат.

---

### Ответ

aseke@aseke-ThinkPad-E14:/etc/nginx/conf.d$ curl -v http://localhost:8080/secret_word --header "Host: example.com"
*   Trying 127.0.0.1:8080...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /secret_word HTTP/1.1
> Host: example.com
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 203 
< Server: nginx/1.27.2
< Date: Sat, 19 Oct 2024 19:52:05 GMT
< Content-Type: application/octet-stream
< Content-Length: 14
< Connection: keep-alive
< 
* Connection #0 to host localhost left intact
jusan-nginx-ip

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
        allow 192.0.0.0/20;
        deny 192.0.0.1;
        deny all;

        return 203 'jusan-nginx-ip';
        add_header Content-Type text/plain;
    }

}