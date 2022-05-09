USE crm_schema;

SELECT * FROM users;

SELECT * FROM tasks;

INSERT INTO users ( fName, lName, email, password, todos_done, image, created_at, updated_at )
VALUES ('admin', 'admin', 'admin@gmail.com', 'rootroot', 0, null, NOW(), NOW() );

INSERT INTO users ( fName, lName, email, password, todos_done, created_at, updated_at )
VALUES ('tester', 'test', 'test@gmail.com', 'rootroot', 0, NOW(), NOW() );
