# dockerize

В данном задании докеризируем свой проект из задания `jusan-fastapi-final`.

### Полезное

- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [Docker Push for Publishing Images](https://www.section.io/engineering-education/docker-push-for-publishing-images-to-docker-hub/)

### Задание

1. Склонируйте содержимое репозитория `jusan-fastapi-final` в репо `jusan-docker/dockerize`.
   Работу будем ввести в нем.
2. Напишите для этого проекта Dockerfile, который запускает API на порту 8080.
3. Произвести сборку образа с именем `jusan-fastapi-final` и тегом `dockerized`.
4. Проверьте на наличие своего образа в вашей системе, перечислите все образы.
5. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 8080 на 8080 порт контейнера;
   - имя контейнера `jusan-dockerize`;
   - использует наш собранный образ.

6. Выполненные команды из шагов 3 и 5 записать в файл `dockerize/solution.sh`.
7. Запушить в репозиторий `jusan-docker`. В папке `dockerize` должны быть:
   - получившийся `Dockerfile`.
   - `solution.sh`
   - содержимое репозитория `jusan-fastapi-final`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-dockerize.sh

---

### Ответ

```bash
aseke@aseke-ThinkPad-E14:~$:/home/aseke/Projects/fastapi# ls
collection.json  Dockerfile  main.py  __pycache__  README.md  requirements.txt

aseke@aseke-ThinkPad-E14:~$:/home/aseke/Projects/fastapi# cat Dockerfile 
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

aseke@aseke-ThinkPad-E14:~$:/home/aseke/Projects/fastapi# docker build -t jusan-fastapi-final:dockerized .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  50.92MB
Step 1/6 : FROM python:3.10-slim
3.10-slim: Pulling from library/python
a480a496ba95: Already exists 
9555349e8380: Pull complete 
1c161e44b06b: Pull complete 
417516d8bb61: Pull complete 
Digest: sha256:eb9ca77b1a0ffbde84c1dc333beb3490a2638813cc25a339f8575668855b9ff1
Status: Downloaded newer image for python:3.10-slim
 ---> 3e625a83fe8d
Step 2/6 : WORKDIR /app
 ---> Running in 20c3392077cd
Removing intermediate container 20c3392077cd
 ---> 4eb80f2d9a71
Step 3/6 : COPY . .
 ---> 034ad8034ff9
Step 4/6 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Running in 701475ce54b2
Collecting annotated-types==0.7.0
  Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Collecting anyio==4.6.2.post1
  Downloading anyio-4.6.2.post1-py3-none-any.whl (90 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.4/90.4 kB 833.5 kB/s eta 0:00:00
Collecting asarPy==1.0.1
  Downloading asarPy-1.0.1.tar.gz (2.3 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting click==8.1.7
  Downloading click-8.1.7-py3-none-any.whl (97 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 3.9 MB/s eta 0:00:00
Collecting fastapi==0.115.2
  Downloading fastapi-0.115.2-py3-none-any.whl (94 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 94.7/94.7 kB 6.1 MB/s eta 0:00:00
Collecting h11==0.14.0
  Downloading h11-0.14.0-py3-none-any.whl (58 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 kB 9.2 MB/s eta 0:00:00
Collecting httptools==0.6.2
  Downloading httptools-0.6.2-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (420 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 420.0/420.0 kB 4.1 MB/s eta 0:00:00
Collecting idna==3.10
  Downloading idna-3.10-py3-none-any.whl (70 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 70.4/70.4 kB 59.4 MB/s eta 0:00:00
Collecting pydantic==2.9.2
  Downloading pydantic-2.9.2-py3-none-any.whl (434 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 434.9/434.9 kB 12.6 MB/s eta 0:00:00
Collecting pydantic_core==2.23.4
  Downloading pydantic_core-2.23.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 7.9 MB/s eta 0:00:00
Collecting python-dotenv==1.0.1
  Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
Collecting PyYAML==6.0.2
  Downloading PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (751 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 751.2/751.2 kB 10.6 MB/s eta 0:00:00
Collecting sniffio==1.3.1
  Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Collecting starlette==0.39.2
  Downloading starlette-0.39.2-py3-none-any.whl (73 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.2/73.2 kB 21.3 MB/s eta 0:00:00
Collecting typing_extensions==4.12.2
  Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Collecting uvicorn==0.31.1
  Downloading uvicorn-0.31.1-py3-none-any.whl (63 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.7/63.7 kB 62.9 MB/s eta 0:00:00
Collecting uvloop==0.21.0
  Downloading uvloop-0.21.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 8.5 MB/s eta 0:00:00
Collecting watchfiles==0.24.0
  Downloading watchfiles-0.24.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (425 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 425.7/425.7 kB 9.5 MB/s eta 0:00:00
Collecting websockets==13.1
  Downloading websockets-13.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (164 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 164.1/164.1 kB 12.6 MB/s eta 0:00:00
Collecting exceptiongroup>=1.0.2
  Downloading exceptiongroup-1.2.2-py3-none-any.whl (16 kB)
Building wheels for collected packages: asarPy
  Building wheel for asarPy (setup.py): started
  Building wheel for asarPy (setup.py): finished with status 'done'
  Created wheel for asarPy: filename=asarPy-1.0.1-py3-none-any.whl size=2850 sha256=b034795033d1c08010c09b1fb1a34a8bb8ef2fb967b87ef03bfdeca6b1180072
  Stored in directory: /tmp/pip-ephem-wheel-cache-i7grz5cn/wheels/b9/e5/78/3f46c93a5804204f5238265a047ff923a5785e9d4ce50bdf19
Successfully built asarPy
Installing collected packages: asarPy, websockets, uvloop, typing_extensions, sniffio, PyYAML, python-dotenv, idna, httptools, h11, exceptiongroup, click, annotated-types, uvicorn, pydantic_core, anyio, watchfiles, starlette, pydantic, fastapi
Successfully installed PyYAML-6.0.2 annotated-types-0.7.0 anyio-4.6.2.post1 asarPy-1.0.1 click-8.1.7 exceptiongroup-1.2.2 fastapi-0.115.2 h11-0.14.0 httptools-0.6.2 idna-3.10 pydantic-2.9.2 pydantic_core-2.23.4 python-dotenv-1.0.1 sniffio-1.3.1 starlette-0.39.2 typing_extensions-4.12.2 uvicorn-0.31.1 uvloop-0.21.0 watchfiles-0.24.0 websockets-13.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 24.3.1
[notice] To update, run: pip install --upgrade pip
Removing intermediate container 701475ce54b2
 ---> 42241c5746bb
Step 5/6 : EXPOSE 8080
 ---> Running in df7c9bebd848
Removing intermediate container df7c9bebd848
 ---> d6cd2fbefd46
Step 6/6 : CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
 ---> Running in 7d4665285d8b
Removing intermediate container 7d4665285d8b
 ---> 5aa4ea702b5c
Successfully built 5aa4ea702b5c
Successfully tagged jusan-fastapi-final:dockerized

aseke@aseke-ThinkPad-E14:~$:/home/aseke/Projects/fastapi# docker images
REPOSITORY            TAG                IMAGE ID       CREATED          SIZE
jusan-fastapi-final   dockerized         5aa4ea702b5c   16 seconds ago   219MB
nginx                 jusan-dockerfile   4b74f3123de3   23 minutes ago   192MB
python                3.10-slim          3e625a83fe8d   2 weeks ago      127MB
nginx                 mainline           3b25b682ea82   4 weeks ago      192MB

aseke@aseke-ThinkPad-E14:~$:/home/aseke/Projects/fastapi# docker run -d \
  --name jusan-dockerize \
  -p 8080:8080 \
  jusan-fastapi-final:dockerized
461aa645d175ba691da02cc29f71c661bc2391963ff79898612cadb29f168bf1

aseke@aseke-ThinkPad-E14:~$:/home/aseke/Projects/fastapi# curl -X PUT -d '{"element":"Apple"}' -H 'Content-Type: application/json' http://localhost:8080/list
{"result":["Apple"]}

aseke@aseke-ThinkPad-E14:~$:/home/aseke/Projects/fastapi# curl -X PUT -d '{"element":"Microsoft"}' -H 'Content-Type: application/json' http://localhost:8080/list
{"result":["Apple","Microsoft"]}