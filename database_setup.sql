-- Use your existing Practice DB database
USE [Practice DB];
GO

-- Create Users table
CREATE TABLE Users (
    ID int IDENTITY(1,1) PRIMARY KEY,
    Name nvarchar(100) NOT NULL,
    Email nvarchar(100) NOT NULL,
    Phone nvarchar(20) NOT NULL,
    Designation nvarchar(100) NOT NULL,
    Company nvarchar(100) NOT NULL,
    CreatedAt datetime DEFAULT GETDATE()
);
GO