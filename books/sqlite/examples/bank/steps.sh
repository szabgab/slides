sqlite3 bank.db < setup_bank.sql
sqlite3 bank.db < show.sql

sqlite3 bank.db < transfer.sql
sqlite3 bank.db < show.sql

sqlite3 bank.db < without_transaction.sql
sqlite3 bank.db < show.sql

sqlite3 bank.db < with_transaction.sql
sqlite3 bank.db < show.sql

rm -f bank.db
