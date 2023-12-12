-- This SQL script converts the hbtn_0c_0 database, first_table.
-- Convert the database to utf8mb4
-- Convert the first_table table and name field to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
