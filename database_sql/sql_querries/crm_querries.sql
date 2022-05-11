USE crm_schema;

SELECT * FROM users;

INSERT INTO users ( f_Name, l_Name, email, password, todos_fin, created_at, updated_at )
VALUES ('tester', 'test', 'test@gmail.com', 'rootroot', 0, NOW(), NOW() );

SELECT * FROM users WHERE id = 1;

UPDATE users
SET f_name = 'tester', l_name = 'fellow', email = 'test@gmail.com',
password = 'rootroot', updated_at = NOW()
WHERE id = 1;

DELETE FROM users WHERE id = 1;

SELECT * FROM tasks;

INSERT INTO tasks ( task_description, priority, is_recurring, reminder_time, due_date, created_at, updated_at, user_id )
VALUES ('test', 3, 0, NOW(), NOW(), NOW(), NOW(), 1 );

SELECT * FROM tasks WHERE id = 1;

UPDATE tasks
SET task_description = 'test update', priority = 2, is_recurring = 2, reminder_time = NOW(), 
due_date = NOW(), updated_at = NOW()
WHERE id = 1;

DELETE FROM tasks WHERE id = 1;
