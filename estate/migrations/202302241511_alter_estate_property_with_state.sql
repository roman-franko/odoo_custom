-- Add a state field to the estate.property model. 
-- Five values are possible: New, Offer Received, Offer Accepted, Sold and Canceled. 

ALTER TABLE estate_property ADD state character varying;

ALTER TABLE estate_property 
   ADD CONSTRAINT check_state_types 
   CHECK (state = 'New' 
       OR state = 'Offer Received'
       OR state = 'Offer Accepted'
       OR state = 'Sold'
       OR state = 'Canceled');

ALTER TABLE estate_property 
    ALTER COLUMN state SET DEFAULT 'New';