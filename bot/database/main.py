from contextlib import suppress
from typing import Any, LiteralString

import psycopg2
import psycopg2.sql
from loguru import logger

from bot.misc.config import config
from bot.misc.utils import SingletonABC


class DatabaseMalboro(metaclass=SingletonABC):
    """Main Database class.

    Methods:
        execute(query: str, *values) -> Any
            Executes the given SQL query with the provided values and returns the result.

        close() -> None
            Closes the connection to the database.
    """

    def __init__(self) -> None:
        self._check_exist_db()

        self._conn = psycopg2.connect(
            host=config.db.host,
            database=config.db.database,
            user=config.db.user,
            password=config.db.password,
            port=config.db.port,
        )
        self._conn.autocommit = True
        self._cursor = self._conn.cursor()

        self._check_exist_tables()


    def execute(self, query: LiteralString | psycopg2.sql.SQL, *values, noreturn: bool = False) -> Any:
        """Executes the given SQL query with the provided values and returns the result.

        Args:
            query (LiteralString): The SQL query to execute.
            *values: Variable length argument list of values to substitute in the query.
            noreturn (bool, optional): Whether to return the result (fetchall) or not.

        Returns:
            The result of executing the query.
        """
        if self._conn.closed:
            msg = "Database connection is closed."
            raise psycopg2.DatabaseError(msg)

        self._cursor.execute(query, values)
        return self._cursor.fetchall() if not noreturn else None


    def _check_exist_db(self) -> None:
        root_conn = psycopg2.connect(
            host=config.db.host,
            database=config.db.root_database,
            user=config.db.user,
            password=config.db.password,
            port=config.db.port,
        )
        root_conn.autocommit = True
        root_cur = root_conn.cursor()

        try:
            root_cur.execute("CREATE DATABASE " + config.db.database + ";")
        except psycopg2.errors.DuplicateDatabase:
            logger.info(f"Database with name {config.db.database} found.")
        else:
            logger.info(f"Database with name {config.db.database} created.")

        root_conn.close()


    def _check_exist_tables(self) -> None:
        for table_name, table_columns in config.db.tables.items():
            exists = self.execute(
                "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)",
                table_name,
            )
            if not exists[0][0]:
                logger.info(f"Table <{table_name}> doesn't exist. Creating...")
                self.execute(
                    psycopg2.sql.SQL("CREATE TABLE {} ({});").format(
                        psycopg2.sql.Identifier(table_name),
                        psycopg2.sql.SQL(table_columns),
                    ),
                    noreturn=True,
                )
                logger.info(f"Table <{table_name}> created with columns <{table_columns}>.")


    def close(self) -> None:
        """Close the database connection.

        This function closes the database connection by closing the cursor and the connection itself.
        """
        self._cursor.close()
        self._conn.close()
        logger.info("Database connection closed.")


    def __del__(self) -> None:  # noqa: D105
        with suppress(Exception):
            self.close()


database = DatabaseMalboro()
