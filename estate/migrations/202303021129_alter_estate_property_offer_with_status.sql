-- Five values are possible: Accepted, Refused. 

ALTER TABLE estate_property_offer
   ADD CONSTRAINT check_status_types 
   CHECK (status = 'Accepted' OR status = 'Refused');