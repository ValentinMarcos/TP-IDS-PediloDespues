CREATE TABLE Productos (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Descripcion VARCHAR(50) NOT NULL,
    Precio DECIMAL(6,2) NOT NULL,
    Categoria VARCHAR(50) NOT NULL
);
CREATE TABLE Tickets (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  
    ID_TRACKEO VARCHAR(100) NOT NULL,
    Total DECIMAL(10,2) NOT NULL,
    Payload VARCHAR(2000) NOT NULL,
    Estado VARCHAR(50) NOT NULL,
    FechaCreacion DATETIME DEFAULT NOW(),  
    UNIQUE (ID_TRACKEO)  
);
CREATE TABLE QR(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Descripcion VARCHAR(50) NOT NULL,
    Estado VARCHAR(50) NOT NULL
);