CREATE DATABASE facebook WITH owner=postgres;


CREATE TABLE IF NOT EXISTS public.posts_staging
(
    id character varying(25) COLLATE pg_catalog."default" NOT NULL,
    text character varying(1800) COLLATE pg_catalog."default" NOT NULL,
    image character varying(150) COLLATE pg_catalog."default" NOT NULL,
    likes bigint NOT NULL,
    shares bigint,
    comments bigint,
    CONSTRAINT posts_staging_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS PUBLIC.posts AS
(SELECT * FROM public.posts_staging WHERE id = null);

ALTER TABLE PUBLIC.posts ADD CONSTRAINT posts_pk PRIMARY KEY(id);

