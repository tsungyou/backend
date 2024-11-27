-- Table: public.realtime_top3

-- DROP TABLE IF EXISTS public.realtime_top3;

CREATE TABLE IF NOT EXISTS public.realtime_top3
(
    da timestamp without time zone NOT NULL,
    code character varying(25) COLLATE pg_catalog."default" NOT NULL,
    cl double precision,
    hi double precision,
    lo double precision,
    op double precision,
    vol bigint,
    adj double precision,
    CONSTRAINT realtime_top3_pkey PRIMARY KEY (da, code)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.realtime_top3
    OWNER to mini;
-- Index: idx_code

-- DROP INDEX IF EXISTS public.idx_code;

CREATE INDEX IF NOT EXISTS idx_code
    ON public.realtime_top3 USING btree
    (code COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_da

-- DROP INDEX IF EXISTS public.idx_da;

CREATE INDEX IF NOT EXISTS idx_da
    ON public.realtime_top3 USING btree
    (da ASC NULLS LAST)
    TABLESPACE pg_default;