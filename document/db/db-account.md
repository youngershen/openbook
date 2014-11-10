account

    | id           | int(11)      | NO   | PRI | NULL    | auto_increment |
    | user_id      | int(11)      | YES  | MUL | NULL    |                |
    | email        | varchar(255) | NO   | MUL | NULL    |                |
    | password     | varchar(255) | NO   |     | NULL    |                |
    | update_time  | timestamp    | YES  |     | NULL    |                |
    | create_time  | timestamp    | YES  |     | NULL    |                |
    | is_avaliable | tinyint(1)   | NO   |     | NULL    |                |
