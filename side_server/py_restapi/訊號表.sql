-- Table: public.block_code3_deatil

-- DROP TABLE IF EXISTS public.block_code3_deatil;

CREATE TABLE IF NOT EXISTS public.block_code3_deatil
(
    code character varying(50) COLLATE pg_catalog."default",
    da timestamp without time zone NOT NULL,
    cl double precision
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.block_code3_deatil
    OWNER to mini;

GRANT ALL ON TABLE public.block_code3_deatil TO mini;



DROP TABLE IF EXISTS public.block_code3_deatil;
CREATE TABLE IF NOT EXISTS public.block_code3_deatil
(
    code character varying(50) COLLATE pg_catalog."default",
    da timestamp without time zone NOT NULL,
    cl double precision
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE OR REPLACE FUNCTION notify_new_message() 
RETURNS TRIGGER AS $$
BEGIN
  PERFORM pg_notify('new_message_channel', row_to_json(NEW)::text);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER new_message_trigger
AFTER INSERT ON block_code3_deatil
FOR EACH ROW EXECUTE FUNCTION notify_new_message();
