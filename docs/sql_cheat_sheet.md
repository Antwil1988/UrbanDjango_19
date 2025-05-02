# SQL Cheat Sheet

## Цель: Понимать, как хранить и обрабатывать данные

### SQL Основы

#### Создание таблиц и типы данных

- **CREATE TABLE**: Создает новую таблицу.

  ```sql
  CREATE TABLE table_name (
      column1 datatype PRIMARY KEY,
      column2 datatype,
      column3 datatype
  );
  ```

- **Типы данных**: INTEGER, TEXT, DATE, BOOLEAN и т.д.

#### CRUD-операции

- **INSERT**: Вставка данных в таблицу.

  ```sql
  INSERT INTO table_name (column1, column2) VALUES (value1, value2);
  ```

- **SELECT**: Извлечение данных из таблицы.

  ```sql
  SELECT column1, column2 FROM table_name WHERE condition;
  ```

- **UPDATE**: Обновление данных в таблице.

  ```sql
  UPDATE table_name SET column1 = value1 WHERE condition;
  ```

- **DELETE**: Удаление данных из таблицы.

  ```sql
  DELETE FROM table_name WHERE condition;
  ```

### Продвинутые операции

#### JOIN, GROUP BY, HAVING

- **JOIN**: Объединение данных из нескольких таблиц.

  ```sql
  SELECT columns FROM table1 JOIN table2 ON table1.column = table2.column;
  ```

- **GROUP BY**: Группировка данных для агрегатных функций.

  ```sql
  SELECT column, COUNT(*) FROM table_name GROUP BY column;
  ```

- **HAVING**: Условие для групп.

  ```sql
  SELECT column, COUNT(*) FROM table_name GROUP BY column HAVING COUNT(*) > 1;
  ```

### Оптимизация

#### Индексы, транзакции, оптимизация запросов

- **Индексы**: Ускоряют поиск данных.

  ```sql
  CREATE INDEX index_name ON table_name (column);
  ```

- **Транзакции**: Группировка операций для атомарности.

  ```sql
  BEGIN;
  -- SQL операции
  COMMIT;
  ```

- **Оптимизация запросов**: Используйте индексы, избегайте SELECT *, анализируйте планы выполнения.

Эта шпаргалка поможет вам быстро вспомнить основные концепции SQL и эффективно работать с базами данных.
