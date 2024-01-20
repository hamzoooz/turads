<!-- pg_dump -U themezoz -d themezoz > backup_file_name.sql

open this in I:\hamzoooz\files\djanog\themezoz\backup_file_name.sql Hamzoooz&0784512346#themezoz.com
C:\Program Files\PostgreSQL\16\bin>

psql -U themezoz -d themezoz -f backup_file_name.sql -->
make backup 
pg_dump -U themezoz -d themezoz > backup_file_name.sql

to restore backup 
psql -U themezoz -d themezoz -f backup_file_name.sql
psql -U themezoz -d themezoz -f I:\hamzoooz\files\djanog\themezoz\backup_file_name.sql
