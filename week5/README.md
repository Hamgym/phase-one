# Task 2

> **Create a new database named website.**

    CREATE DATABASE website;
    SHOW DATABASES;
    USE website;

![2-1](./images/2-1.png)

---

> **Create a new table named member, in the website database, designed as below:**

    CREATE TABLE member(
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        follower_count INT UNSIGNED NOT NULL DEFAULT 0,
        time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    SHOW TABLES;

![2-2](./images/2-2.png)

---

# Task 3

> **INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.**

    INSERT INTO member(name, username, password, follower_count)
    VALUES('test', 'test', 'test', 40);
    INSERT INTO member(name, username, password, follower_count)
    VALUES('ethan', 'ethan', 'ethan', 35);
    INSERT INTO member(name, username, password, follower_count)
    VALUES('peter', 'peter', 'peter', 15);
    INSERT INTO member(name, username, password, follower_count)
    VALUES('henry', 'henry', 'henry', 20);
    INSERT INTO member(name, username, password, follower_count)
    VALUES('emma', 'emma', 'emma', 100);

![3-1](./images/3-1.png)

---

> **SELECT all rows from the member table.**

    SELECT * FROM member;

![3-2](./images/3-2.png)

---

> **SELECT all rows from the member table, in descending order of time.**

    SELECT * FROM member ORDER BY time DESC;

![3-3](./images/3-3.png)

---

> **SELECT total 3 rows, second to fourth, from the member table, in descending order of time.**

    SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;

![3-4](./images/3-4.png)

---

> **SELECT rows where username equals to test.**

    SELECT * FROM member WHERE username='test';

![3-5](./images/3-5.png)

---

> **SELECT rows where name includes the es keyword.**

    SELECT * FROM member WHERE name LIKE '%es%';

![3-6](./images/3-6.png)

---

> **SELECT rows where both username and password equal to test.**

    SELECT * FROM member WHERE username='test' AND password='test';

![3-7](./images/3-7.png)

---

> **UPDATE data in name column to test2 where username equals to test.**

    UPDATE member SET name='test2' WHERE username='test';
    SELECT * FROM member WHERE username='test';

![3-8](./images/3-8.png)

---

# Task 4

> **SELECT how many rows from the member table.**

    SELECT COUNT(id) FROM member;

![4-1](./images/4-1.png)

---

> **SELECT the sum of follower_count of all the rows from the member table.**

    SELECT SUM(follower_count) FROM member;

![4-2](./images/4-2.png)

---

> **SELECT the average of follower_count of all the rows from the member table.**

    SELECT AVG(follower_count) FROM member;

![4-3](./images/4-3.png)

---

> **SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.**

    SELECT AVG(follower_count)
    FROM (SELECT * FROM member ORDER BY follower_count DESC LIMIT 2)
    AS top_two;

![4-4](./images/4-4.png)

---

# Task 5

> **Create a new table named message, in the website database. designed as below:**

    CREATE TABLE message(
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        member_id BIGINT NOT NULL,
        content VARCHAR(255) NOT NULL,
        like_count INT UNSIGNED NOT NULL DEFAULT 0,
        time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (member_id) REFERENCES member(id)
    );
    SHOW TABLES;

![5-1](./images/5-1.png)

---

> **SELECT all messages, including sender names. We have to JOIN the member table to get that.**

    INSERT INTO message(member_id, content, like_count) VALUES(1, 'lorem', 4);
    INSERT INTO message(member_id, content, like_count) VALUES(2, 'lorem', 10);
    INSERT INTO message(member_id, content, like_count) VALUES(3, 'lorem', 1);
    INSERT INTO message(member_id, content, like_count) VALUES(4, 'lorem', 5);
    INSERT INTO message(member_id, content, like_count) VALUES(5, 'lorem', 30);
    INSERT INTO message(member_id, content, like_count) VALUES(1, 'lorem', 23);
    INSERT INTO message(member_id, content, like_count) VALUES(2, 'lorem', 21);
    INSERT INTO message(member_id, content, like_count) VALUES(3, 'lorem', 7);
    SELECT *
    FROM message JOIN member
    ON message.member_id=member.id;

![5-2](./images/5-2.png)

---

> **SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.**

    SELECT *
    FROM message JOIN member
    ON message.member_id=member.id
    WHERE member.username='test';

![5-3](./images/5-3.png)

---

> **Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.**

    SELECT AVG(like_count)
    FROM message JOIN member
    ON message.member_id=member.id
    WHERE member.username='test';

![5-4](./images/5-4.png)

---

> **Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.**

    SELECT member.username, AVG(like_count)
    FROM message JOIN member
    ON message.member_id=member.id
    GROUP BY member.username;

![5-5](./images/5-5.png)

---
