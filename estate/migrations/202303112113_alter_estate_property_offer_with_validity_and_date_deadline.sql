-- Add the following fields to the estate.property.offer model
-- Field Type Default
-- validity Integer 7
-- date_deadline Date

ALTER TABLE estate_property ADD validity INTEGER DEFAULT 7;
ALTER TABLE estate_property ADD date_deadline TIMESTAMP WITHOUT TIME ZONE;