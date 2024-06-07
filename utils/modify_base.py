import psycopg2

con = psycopg2.connect(
    dbname='narod_pg_small_sample',
    user='narod_user',
    password='*****',
    host='localhost',
    port='5432'
)

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS file_meta_info (
    "file_meta_id" SERIAl PRIMARY KEY,
    "file_id" BIGINT,
    "size" BIGINT,
    "size_h" VARCHAR(100),
    "modification_date" TIMESTAMP,
    "html_code" TEXT,
    "title" TEXT,
    "author" TEXT,
    "page_count" BIGINT,
    "text_layer" BOOLEAN,
    "text" TEXT,
    "char_count" BIGINT,
    "word_count" BIGINT,
    "rows" BIGINT,
    "columns" BIGINT,
    "slides_count" INTEGER,
    "image_height" INTEGER,
    "image_width" INTEGER,
    "image_format" VARCHAR(100),
    "image_mode" VARCHAR(100),
    "exif" TEXT,
    "exif_make" TEXT,
    "exif_model" TEXT,
    "exif_software" TEXT,
    "exif_orientation" SMALLINT,
    "exif_datetime" TIMESTAMP,
    "exif_artist" TEXT,
    "exif_copyright" TEXT,
    "exif_hostcomputer" TEXT,
    FOREIGN KEY (file_id) REFERENCES file(file_id)
);
""")

con.commit()

con.close()