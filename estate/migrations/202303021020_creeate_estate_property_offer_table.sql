CREATE SEQUENCE estate_property_offer_id_seq INCREMENT 1 START 1;

CREATE TABLE estate_property_offer (
   id INTEGER DEFAULT nextval('estate_property_offer_id_seq'::regclass),
   create_uid INTEGER, 
   create_date TIMESTAMP WITHOUT TIME ZONE,
   write_uid INTEGER,
   write_date TIMESTAMP WITHOUT TIME ZONE,
   price numeric,
   status character varying,
   partner_id INTEGER NOT NULL,
   property_id INTEGER NOT NULL,
   CONSTRAINT estate_property_offer_pkey 
      PRIMARY KEY (id),
   CONSTRAINT estate_property_tyoe_create_uid_fkey 
      FOREIGN KEY (create_uid) 
      REFERENCES res_users(id) 
      ON DELETE SET NULL,
   CONSTRAINT estate_property_offer_write_uid_fkey 
      FOREIGN KEY (write_uid) 
      REFERENCES res_users(id) 
      ON DELETE SET NULL
);


