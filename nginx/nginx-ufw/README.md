# nginx-ufw

На вашем сервере может быть запущено несколько сервисов помимо nginx. Оставлять доступ к ним открытым из Интернета может быть очень опасно.
Злоумышленники могут этим воспользоваться и взломать один из открытых сервисов.

Для безопасности, нужно закрыть к ним доступы и оставить только доступ к веб-серверу nginx. Одним из способов это сделать является команда `ufw`.

На данном уроке, мы научимся как обезопасить свой сервер.

### Полезные ссылки

- [UFW - Uncomplicated Firewall](https://help.ubuntu.com/community/UFW)
- [Hello Linux: Nginx & UFW Firewall](https://www.codingforentrepreneurs.com/blog/hello-linux-nginx-and-ufw-firewall)

### Задание

1. На своем компьютере запустите nginx. Скачайте `ufw` и настройте доступ извне только на порты 80 и 443.
2. Отправьте выполненные команды.

---

### Ответ

aseke@aseke-ThinkPad-E14:~$ sudo apt install ufw
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово         
Уже установлен пакет ufw самой новой версии (0.36.1-4ubuntu0.1).
Обновлено 0 пакетов, установлено 0 новых пакетов, для удаления отмечено 0 пакетов, и 1 пакетов не обновлено.
aseke@aseke-ThinkPad-E14:~$ sudo ufw status
Состояние: неактивен
aseke@aseke-ThinkPad-E14:~$ sudo ufw enable
Межсетевой экран включён и будет запускаться при запуске системы
aseke@aseke-ThinkPad-E14:~$ sudo ufw allow 22 80 443
ERROR: Неверное количество аргументов
aseke@aseke-ThinkPad-E14:~$ sudo ufw allow 22
Правило добавлено
Правило добавлено (v6)
aseke@aseke-ThinkPad-E14:~$ sudo ufw allow 80
Правило добавлено
Правило добавлено (v6)
aseke@aseke-ThinkPad-E14:~$ sudo ufw allow 443
Правило добавлено
Правило добавлено (v6)
aseke@aseke-ThinkPad-E14:~$ sudo ufw status numbered
Состояние: активен

     В                          Действие    Из
     -                          --------    --
[ 1] 22                         ALLOW IN    Anywhere                  
[ 2] 80                         ALLOW IN    Anywhere                  
[ 3] 443                        ALLOW IN    Anywhere                  
[ 4] 22 (v6)                    ALLOW IN    Anywhere (v6)             
[ 5] 80 (v6)                    ALLOW IN    Anywhere (v6)             
[ 6] 443 (v6)                   ALLOW IN    Anywhere (v6)             

aseke@aseke-ThinkPad-E14:~$