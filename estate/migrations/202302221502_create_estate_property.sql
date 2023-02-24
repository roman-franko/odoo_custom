CREATE SEQUENCE estate_property_id_seq INCREMENT 1 START 1;

CREATE TABLE estate_property (
   id INTEGER DEFAULT nextval('estate_property_id_seq'::regclass),
   create_uid INTEGER, 
   create_date TIMESTAMP WITHOUT TIME ZONE,
   write_uid INTEGER,
   write_date TIMESTAMP WITHOUT TIME ZONE,
   name character varying NOT NULL,
   description text,
   postcode character varying,
   availability_date date,
   expected_price double precision NOT NULL,
   selling_price double precision,
   bedrooms integer,
   living_area integer,
   facades integer,
   garage boolean,
   garden boolean,
   garden_area integer,
   garden_orientation character varying,
   CONSTRAINT estate_property_pkey 
      PRIMARY KEY (id),
   CONSTRAINT estate_property_create_uid_fkey 
      FOREIGN KEY (create_uid) 
      REFERENCES res_users(id) 
      ON DELETE SET NULL,
   CONSTRAINT estate_property_write_uid_fkey 
      FOREIGN KEY (write_uid) 
      REFERENCES res_users(id) 
      ON DELETE SET NULL
);


