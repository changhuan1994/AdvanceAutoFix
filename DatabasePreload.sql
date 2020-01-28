INSERT INTO qualification(qualification_name) VALUES ('Windshield Wiper Replacement');
INSERT INTO qualification(qualification_name) VALUES ('Oil Change');
INSERT INTO qualification(qualification_name) VALUES ('Tire Change');
#Select * from qualification;

INSERT INTO job_types(job_name, HHTP_Link) VALUES ('Windshield Wiper Replacement', 'HTTP Wipers');
INSERT INTO job_types(job_name, HHTP_Link) VALUES ('Oil Change', 'HTTP Oil');
INSERT INTO job_types(job_name, HHTP_Link) VALUES ('Tire Change', 'HTTP Tire');
INSERT INTO job_types(job_name, HHTP_Link) VALUES ('Tire and Oil Change', 'HTTP Tire and Oil');
#Select * from job_types;

INSERT INTO job_qualifications(qual_id, job_type_id) VALUES (1, 1);
INSERT INTO job_qualifications(qual_id, job_type_id) VALUES (2, 2);
INSERT INTO job_qualifications(qual_id, job_type_id) VALUES (3, 3);
INSERT INTO job_qualifications(qual_id, job_type_id) VALUES (2, 4);
INSERT INTO job_qualifications(qual_id, job_type_id) VALUES (3, 4);
#Select * from job_qualifications;

INSERT INTO master_parts_list(part_name) VALUES ('Windshield Wiper');
INSERT INTO master_parts_list(part_name) VALUES ('Oil');
INSERT INTO master_parts_list(part_name) VALUES ('Tire');
INSERT INTO master_parts_list(part_name) VALUES ('Wrench');
#Select * from master_parts_list;

INSERT INTO parts_list_for_job(parts_id, job_type_id) VALUES (1, 1);
INSERT INTO parts_list_for_job(parts_id, job_type_id) VALUES (2, 2);
INSERT INTO parts_list_for_job(parts_id, job_type_id) VALUES (3, 3);
INSERT INTO parts_list_for_job(parts_id, job_type_id) VALUES (2, 4);
INSERT INTO parts_list_for_job(parts_id, job_type_id) VALUES (3, 4);
INSERT INTO parts_list_for_job(parts_id, job_type_id) VALUES (4, 4);
#Select * from parts_list_for_job;

INSERT INTO users(full_name, username, ASECert_id, address, bio, paypal_info, ASECert_HTTP) 
VALUES ("The Boss","Big Boss","","Boss St","The Big Boss", "", "");

INSERT INTO users(full_name, username, ASECert_id, address, bio, paypal_info, ASECert_HTTP) 
VALUES ("Greg","The Customer","","Work For Me St","I can't Build IT", "PayPal To pay you", "");

INSERT INTO users(full_name, username, ASECert_id, address, bio, paypal_info, ASECert_HTTP) 
VALUES ("Bob","Bob The Builder","IcanBuildIt","builder St","I can Build IT", "pay me", "HTTP");

INSERT INTO users(full_name, username, ASECert_id, address, bio, paypal_info, ASECert_HTTP) 
VALUES ("Bilbo Baggins","Hobbit","2nd Brunch","The Shire","Is it tea time", "pay me here", "HTTP");
#Select * from users;

INSERT INTO permissions(permission_name) VALUES ('Admin');
INSERT INTO permissions(permission_name) VALUES ('Mechanic');
INSERT INTO permissions(permission_name) VALUES ('Customer');
#Select * from permissions;

INSERT INTO user_permissions(permission_id, user_id) VALUES (1, 1);
INSERT INTO user_permissions(permission_id, user_id) VALUES (3, 2);
INSERT INTO user_permissions(permission_id, user_id) VALUES (2 , 3);
INSERT INTO user_permissions(permission_id, user_id) VALUES (2 , 4);
#Select * from user_permissions;

INSERT INTO mechanics_qualifications(qual_id, mec_id) VALUES (1, 3);
INSERT INTO mechanics_qualifications(qual_id, mec_id) VALUES (2, 3);
INSERT INTO mechanics_qualifications(qual_id, mec_id) VALUES (3 , 3);
INSERT INTO mechanics_qualifications(qual_id, mec_id) VALUES (1 , 4);
#Select * from user_permissions;

INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (1, Point(-78.673575, 35.772310), "Customer's car Address", "Help Me", 2);
INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (2, Point(-78.648781, 35.788279), "Customer's 2nd car Address", "Help Me", 2);
INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (3, Point(-78.625679, 35.804994), "Customer's 3rd car Address", "Help Me", 2);
INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (4, Point(-78.625679, 35.804994), "Customer's 5th car Address", "Help Me", 2);
INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (1, Point(-78.625529, 35.819539), "Customer's 4th car Address", "Help Me", 2);

INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (2, Point(-78.673575, 35.772310), "Customer's 6thcar Address", "Help Me", 2);
INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (3, Point(-78.648781, 35.788279), "Customer's 7th car Address", "Help Me", 2);
INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (4, Point(-78.625679, 35.804994), "Customer's 8th car Address", "Help Me", 2);
INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (1, Point(-78.625679, 35.804994), "Customer's 9th car Address", "Help Me", 2);
INSERT INTO jobs(job_type_id, location, address, details, cus_id) VALUES (2, Point(-78.625529, 35.819539), "Customer's 10th car Address", "Help Me", 2);
#Select * from jobs;

INSERT INTO store(store_address, location) VALUES ( "AA store Road", Point(-78.625679, 35.819539));
INSERT INTO store(store_address, location) VALUES ("The Shire", Point(-78.625529, 35.804994));
INSERT INTO store(store_address, location) VALUES ("builder St", Point(-78.625679, 35.772310));
#Select * from store;

INSERT INTO bookings(job_id, store_id, mec_id) VALUES (4, 1, 3);
INSERT INTO bookings(job_id, store_id, mec_id) VALUES (3, 1, 3);
INSERT INTO bookings(job_id, store_id, mec_id) VALUES (5, 1, 4);
#Select * from bookings;

INSERT INTO status(status_name) VALUES ("Accepted");
INSERT INTO status(status_name) VALUES ("Parts Pick up");
INSERT INTO status(status_name) VALUES ("Start Job ");
INSERT INTO status(status_name) VALUES ("Processing");
INSERT INTO status(status_name) VALUES ("Finish Repairs ");
INSERT INTO status(status_name) VALUES ("Return tools");
INSERT INTO status(status_name) VALUES ("Finish Job");
INSERT INTO status(status_name) VALUES ("Pre Start Canceled");
INSERT INTO status(status_name) VALUES ("Post Start Canceled");
INSERT INTO status(status_name) VALUES ("Emergency Job");
#Select * from status;

INSERT INTO Status_list(status_id, job_id, status_update, status_time) VALUES (1, 4, "accepted job", "2019-11-17 12:00:01");
INSERT INTO Status_list(status_id, job_id, status_update, status_time) VALUES (2, 4, "Parts Pick Up", "2019-11-17 14:00:01");
INSERT INTO Status_list(status_id, job_id, status_update, status_time) VALUES (3, 4, "Starting", "2019-11-17 15:00:01");
INSERT INTO Status_list(status_id, job_id, status_update, status_time) VALUES (1, 3, "accepted job", "2019-11-17 12:00:01");
INSERT INTO Status_list(status_id, job_id, status_update, status_time) VALUES (1, 5, "accepted job", "2019-11-17 12:00:01");
#Select * from Status_list;





