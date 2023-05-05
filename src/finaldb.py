import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

#Create clinic table
create_clinic_query = """
    CREATE TABLE Clinic (
    clinicNo INT PRIMARY KEY NOT NULL,
    name VARCHAR(255),
    address VARCHAR(255) UNIQUE,
    phoneNo VARCHAR(12),
    managerNo INT NOT NULL,
    
    FOREIGN KEY (managerNo) REFERENCES Staff(staffNo)
);"""

#Create staff table
create_staff_query = """
    CREATE TABLE Staff (
    staffNo INT PRIMARY KEY NOT NULL,
    name VARCHAR(255),
    address VARCHAR(255) UNIQUE,
    phoneNo VARCHAR(12),
    dob DATE,
    position VARCHAR(255),
    salary INT,
    clinicNo INT NOT NULL,
    
    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
);"""
    
#Create examination table
create_examination_query = """
    CREATE TABLE Examination (
    examNo INT PRIMARY KEY NOT NULL,
    chiefComplaint VARCHAR(255),
    description VARCHAR(255),
    dateSeen DATE,
    actionsTaken VARCHAR(255),
    staffNo INT NOT NULL,
    petNo INT NOT NULL,
    
      
    FOREIGN KEY (petNo) REFERENCES Pets(petNo),
    FOREIGN KEY (staffNo) REFERENCES Staff(staffNo)
);"""
    
#Create Pets table
create_pets_query = """

    CREATE TABLE Pets(
    petNo INT PRIMARY KEY NOT NULL,
    name VARCHAR(255),
    dob DATE,
    species VARCHAR(255),
    breed VARCHAR(255),
    color VARCHAR(255),clinicNo INT NOT NULL,
    ownerNo INT NOT NULL,

    FOREIGN KEY(clinicNo) REFERENCES Clinic(clinicNo),
    FOREIGN KEY(ownerNo) REFERENCES Owner(ownerNo)

);"""

#Create Owner TABLE
create_owner_query = """

    CREATE TABLE Owner(
    ownerNo INT PRIMARY KEY NOT NULL,
    name VARCHAR(255),
    address VARCHAR(255),
    phoneNo VARCHAR(12)

);"""
# Execute query, the result is stored in cursor

cursor.execute(create_clinic_query)
cursor.execute(create_staff_query)
cursor.execute(create_examination_query)
cursor.execute(create_pets_query)
cursor.execute(create_owner_query)

# Insert info into clinic
clinic_info = """
    INSERT INTO Clinic VALUES
(1, 'Pawsome Pets Hollywood', '123 Santa St, Hollywood, FL 33145', '123-456-7890', 1),
(2, 'Pawsome Pets Miami', '456 Park Ave, Miami, FL 33146', '234-567-8901', 2),
(3, 'Pawsome Pets Gables', '789 Hill Ct, Gables, FL 33165', '345-678-9012', 5),
(4, 'Pawsome Pets Kendall', '321 Halandale Rd, Kendall FL 33178', '456-789-0123', 4),
(5, 'Pawsome Pets Hialeah', 'Mountain Ave, Hialeah, FL 33157 ',  '567-890-1234', 3);
"""
cursor.execute(clinic_info)

# Insert info into staff
staff_info = """
    INSERT INTO Staff VALUES
(1, 'John Green', '83 Cherry Court, Pensacola, FL 32526', '123-456-7890', '1990-01-01', 'Technician', 60000, 1),
(2, 'Jane Doe', '8 Bedford Road, Brandon, FL 33511', '234-567-8901', '1995-04-15', 'Veterinarian', 80000, 2),
(3, 'Barb Johnson', '41 Mill Pond Ave, Miami, FL 33161', '345-678-9012', '1980-07-05', 'Veterinarian', 80000, 3),
(4, 'Star Williams', '9337 Foster Avenue, Bradenton, FL 34208', '456-789-0123', '1985-10-20', 'Technician', 60000, 4),
(5, 'Stella Brown', '69 William St.New Port Richey, FL 34653', '567-890-1234', '1988-12-31', 'Receptionist', 40000, 5);
"""

cursor.execute(staff_info)

# Insert info into owner
owner_info = """
INSERT INTO Owner VALUES
(1, 'Juliana Parrish', '83 Cherry Court, Pensacola, FL 32526', '123-456-7890'),
(2, 'Brandon Gates', '125 Glenridge St., Jacksonville, FL 32211', '234-567-8901'),
(3, 'Kamila Burch', '13 Del Monte St., Hialeah, FL 33014', '345-678-9012'),
(4, 'David Williams', '53 Pumpkin Hill Ave., Tampa, FL 33612', '456-789-0123'),
(5, 'Juliet Washington', '7179 E. Blackburn Dr., Pompano Beach, FL 33060', '567-890-1234');
"""

cursor.execute(owner_info)

# Insert info into Pets
pets_info= """
INSERT INTO Pets VALUES
(1, 'Fluffy', '2010-01-01', 'Dog', 'Labrador Retriever', 'Yellow', 1, 5),
(2, 'Buddy', '2012-03-15', 'Dog', 'Golden Retriever', 'Golden', 2, 4),
(3, 'Sasha', '2011-05-07', 'Cat', 'Siamese', 'Gray', 3, 3),
(4, 'Max', '2009-09-21', 'Dog', 'German Shepherd', 'Black', 4, 2),
(5, 'Kitty', '2008-12-31', 'Cat', 'Domestic Shorthair', 'Tuxedo', 5, 1);
"""

cursor.execute(pets_info)

#Insert info into examinations
examination_info = """
    INSERT OR IGNORE INTO Examination
    VALUES
        (2,'Check Up', 'Monthly appointment', '2010-12-31', 'N/A', 2, 1),
        (1,'Teeth checkup', 'Looked at teeth', '2005-09-21', 'Given meds', 2,2),
        (3,'Dentist', 'Took teeth out', '2001-08-11', 'treats', 1, 3),
        (4,'Femur tumor', 'remove tumor', '2010-10-08', 'Treats', 1, 4),
        (5,'Surgery', 'Had broken ribs', '2014-04-23', 'N/A', 2, 5);
    """

cursor.execute(examination_info)

print("Database")

# Get the clinic number, name, and address any clinic in Gables
query_1 = """
    SELECT clinicNo, name, address
    FROM Clinic
    WHERE address LIKE '%Gables%';
    """
cursor.execute(query_1)

#Get the staff number, name, and position for all staff members who are veterinarians
query_2 = """
    SELECT staffNo, name, position
    FROM Staff
    WHERE position = 'Veterinarian';
    """
cursor.execute(query_2)

#Get the owner number, name, and telephone number for all owners who have pets registered at Clinic 1
query_3 = """
    SELECT o.ownerNo, o.name, o.phoneNo
    FROM Owner o
    JOIN Pets p ON o.ownerNo = p.ownerNo
    JOIN Clinic c ON p.clinicNo = c.clinicNo
    WHERE c.clinicNo = 1;
    """
cursor.execute(query_3)

#Get the pet number, name, species, and breed for all pets registered at Clinic 2
query_4 = """
    SELECT p.petNo, p.name, species, breed
    FROM Pets p
    JOIN Clinic c ON p.clinicNo = c.clinicNo
    WHERE c.clinicNo = 2;
"""
cursor.execute(query_4)

query_5 = """
    SELECT dateSeen
    FROM Examination;
    """
cursor.execute(query_5)

queries = [query_1, query_2, query_3, query_4, query_5]
for query in queries:
    cursor.execute(query)
    column_names = [row[0] for row in cursor.description]
    table_data = cursor.fetchall()
    df = pd.DataFrame(table_data, columns = column_names)
    print("...")
    print(df)
    print("...")

db_connect.close()


