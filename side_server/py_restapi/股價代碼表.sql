-- Table: public.maincode

-- DROP TABLE IF EXISTS public.maincode;

CREATE TABLE IF NOT EXISTS public.maincode
(
    code character varying(50) COLLATE pg_catalog."default" NOT NULL,
    cname character varying(50) COLLATE pg_catalog."default",
    ename character varying(50) COLLATE pg_catalog."default",
    round_lot integer,
    outstanding_shares bigint,
    equity_float double precision,
    is_download_data boolean,
    is_rt boolean DEFAULT false,
    CONSTRAINT lastda_pkey PRIMARY KEY (code)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.maincode
    OWNER to mini;

GRANT ALL ON TABLE public.maincode TO mini;




-- 
-- Table: public.maincode
DROP TABLE IF EXISTS public.maincode;

CREATE TABLE IF NOT EXISTS public.maincode
(
    code character varying(50) COLLATE pg_catalog."default" NOT NULL,
    cname character varying(50) COLLATE pg_catalog."default",
    ename character varying(50) COLLATE pg_catalog."default",
    round_lot VARCHAR(225),
    outstanding_shares VARCHAR(225),
    equity_float VARCHAR(225),
    is_download_data VARCHAR(225),
    is_rt VARCHAR(225),
    CONSTRAINT lastda_pkey PRIMARY KEY (code)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.maincode
    OWNER to mini;

GRANT ALL ON TABLE public.maincode TO mini;
-- 