CREATE UNLOGGED TABLE IF NOT EXISTS postsstaging
(
    id character varying(25) COLLATE pg_catalog."default" NOT NULL,
    text character varying(1800) COLLATE pg_catalog."default" NOT NULL,
    image character varying(400) COLLATE pg_catalog."default" NOT NULL,
    likes bigint NOT NULL,
    shares bigint,
    comments bigint,
    CONSTRAINT posts_staging_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS posts AS
(SELECT * FROM postsstaging WHERE id = null);

ALTER TABLE posts ADD CONSTRAINT posts_pk PRIMARY KEY(id);

COMMIT;

