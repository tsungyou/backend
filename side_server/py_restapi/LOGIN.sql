-- Drop the table if it exists
DROP TABLE IF EXISTS public.user_credential;

-- Create the table with the specified columns
CREATE TABLE IF NOT EXISTS public.user_credential
(
    username VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    pwd VARCHAR(255) NOT NULL,
    phoneNumber VARCHAR(255) NOT NULL,
    plan1 VARCHAR(50) DEFAULT NULL,
    plan2 VARCHAR(50) DEFAULT NULL,
    plan3 VARCHAR(50) DEFAULT NULL,
    plan4 VARCHAR(50) DEFAULT NULL,
    plan5 VARCHAR(50) DEFAULT NULL,
    CONSTRAINT user_credential_pkey PRIMARY KEY (username)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

-- Optional: Set the table owner if needed
ALTER TABLE public.user_credential
    OWNER to mini;
ß