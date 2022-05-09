USE crm_schema;

SELECT * FROM users;

SELECT * FROM tasks;

INSERT INTO users ( f_Name, l_Name, email, password, todos_done, created_at, updated_at )
VALUES ('tester', 'test', 'test@gmail.com', 'rootroot', 0, NOW(), NOW() );
