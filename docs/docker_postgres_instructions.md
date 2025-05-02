# Инструкции по подключению к PostgreSQL и управлению контейнерами

## Подключение к контейнеру PostgreSQL

1. **Запустите Docker Desktop**, если он еще не запущен.

2. **Проверьте, что контейнер PostgreSQL работает**:

   ```bash
   docker ps
   ```

3. **Подключитесь к PostgreSQL**:

   ```bash
   docker exec -it my_postgres psql -U postgres
   ```

## Управление контейнерами

- **Запустить контейнер**:

  ```bash
  docker start my_postgres
  ```

- **Остановить контейнер**:

  ```bash
  docker stop my_postgres
  ```

- **Проверить статус контейнеров**:

  ```bash
  docker ps
  ```

## Подключение к pgAdmin

1. **Откройте браузер и перейдите по адресу**: `http://localhost`

2. **Войдите в pgAdmin** с использованием учетных данных, которые вы указали при установке (например, `admin@example.com` и `admin`).

3. **Добавьте сервер PostgreSQL в pgAdmin**:
   - Имя ��ервера: `My PostgreSQL`
   - Hostname/Address: `my_postgres`
   - Port: `5432`
   - Maintenance database: `postgres`
   - Username: `postgres`
   - Password: `mysecretpassword`

Сохраните этот файл в удобном для вас месте, чтобы всегда иметь под рукой инструкции по подключению и управлению вашей базой данных. Если у вас возникнут дополнительные вопросы, не стесняйтесь обращаться!
