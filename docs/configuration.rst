Configuration
=============

Default location: ``~/.soar_lite/config.yml``

Example
-------

.. code-block:: yaml

    database:
      uri: sqlite:///~/.soar_lite/soar.db

    connectors:
      slack:
        token: "xoxb-…"
      jira:
        url: "https://yourcompany.atlassian.net"
        user: "bot_user"
        api_token: "******"

Environment Overrides
---------------------

+----------------+------------------------------------------+
| Variable       | Description                              |
+================+==========================================+
| ``SOAR_DB_URI``| Override the ``database.uri`` field.     |
+----------------+------------------------------------------+
| ``SOAR_LOG_LEVEL``| Set root log level (INFO, DEBUG…).    |
+----------------+------------------------------------------+
