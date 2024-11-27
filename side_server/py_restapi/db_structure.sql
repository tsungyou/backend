 Schema |        Name        | Type  | Owner 
--------+--------------------+-------+-------
 public | block_code3_deatil | table | mini
 public | maincode           | table | mini
 public | price              | table | mini
 public | realtime_top3      | table | mini
 public | stock_price        | table | mini
 public | user_credential    | table | mini

                    Table "public.block_code3_deatil"
    Column |            Type             | Collation | Nullable | Default 
    --------+-----------------------------+-----------+----------+---------
    code   | character varying(50)       |           |          | 
    da     | timestamp without time zone |           | not null | 
    cl     | double precision            |           |          | 


                           Table "public.maincode"
       Column       |         Type          | Collation | Nullable | Default 
--------------------+-----------------------+-----------+----------+---------
 code               | character varying(50) |           | not null | 
 cname              | character varying(50) |           |          | 
 ename              | character varying(50) |           |          | 
 round_lot          | integer               |           |          | 
 outstanding_shares | bigint                |           |          | 
 equity_float       | double precision      |           |          | 
 is_download_data   | boolean               |           |          | 
 is_rt              | boolean               |           |          | false
Indexes:
    "lastda_pkey" PRIMARY KEY, btree (code)


                          Table "public.price"
 Column  |            Type             | Collation | Nullable | Default 
---------+-----------------------------+-----------+----------+---------
 da      | timestamp without time zone |           | not null | 
 code    | character varying(50)       |           | not null | 
 cl      | double precision            |           |          | 
 hi      | double precision            |           |          | 
 lo      | double precision            |           |          | 
 op      | double precision            |           |          | 
 vol     | bigint                      |           |          | 
 adj     | double precision            |           |          | 
 wma_20  | double precision            |           |          | 
 wma_50  | double precision            |           |          | 
 wma_100 | double precision            |           |          | 
Indexes:
    "price_backup_pkey" PRIMARY KEY, btree (code, da)
    "idx_price_backup_code" btree (code)
    "idx_price_code" btree (code)
    "idx_price_da" btree (da)
    "idx_price_future_backup_code" btree (code)
    "price_backup_index" btree (da, code)
    "price_future_backup_index" btree (da, code)

                     Table "public.realtime_top3"
 Column |            Type             | Collation | Nullable | Default 
--------+-----------------------------+-----------+----------+---------
 da     | timestamp without time zone |           | not null | 
 code   | character varying(25)       |           | not null | 
 cl     | double precision            |           |          | 
 hi     | double precision            |           |          | 
 lo     | double precision            |           |          | 
 op     | double precision            |           |          | 
 vol    | bigint                      |           |          | 
 adj    | double precision            |           |          | 
Indexes:
    "realtime_top3_pkey" PRIMARY KEY, btree (da, code)
    "idx_code" btree (code)
    "idx_da" btree (da)


                      Table "public.stock_price"
 Column |            Type             | Collation | Nullable | Default 
--------+-----------------------------+-----------+----------+---------
 da     | timestamp without time zone |           | not null | 
 code   | character varying(25)       |           | not null | 
 cl     | double precision            |           |          | 
 hi     | double precision            |           |          | 
 lo     | double precision            |           |          | 
 op     | double precision            |           |          | 
 vol    | bigint                      |           |          | 
 adj    | double precision            |           |          | 
Indexes:
    "blp_stockprice_pkey" PRIMARY KEY, btree (da, code)
    "idx_stock_price_da" btree (da)
    "name" btree (da, code)


 DESC table_name;
 SHOW COLUMNS FROM table_name;

 SELECT COLUMN_NAME, DATA_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_NAME = 'table_name'
AND TABLE_SCHEMA = 'database_name';

\d table_name
