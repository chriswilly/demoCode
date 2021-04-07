"""load all queries as dict, moved out of class"""


def sql_stmt():  # key:str
    d = {}
    d['create_tbl'] = """
                      CREATE TABLE IF NOT EXISTS ssa_names (
                          id INTEGER NOT NULL,
                	      name TEXT NOT NULL,
                   	      sex TEXT NOT NULL,
                	      number INTEGER NOT NULL,
                          year INTEGER NOT NULL,
                          PRIMARY KEY (id)
                          );
                      """

    # update with sqlalchemy fmt
    d['insert_rec'] = """
                      INSERT INTO ssa_names (
                          name,
                          sex,
                          number,
                          year
                          )
                          VALUES ('{0}','{1}','{2}','{3}');
                      """


    d['insert_gen'] = """
                      INSERT INTO {0} {1}
                          VALUES {2};
                      """

                      # """
                      # INSERT INTO {table} {cols}
                      #     VALUES {vals};
                      # """

# coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
# >>> 'Coordinates: {latitude}, {longitude}'.format(**coord)

    d['tbl_gen'] = """
                      CREATE TABLE IF NOT EXISTS {table} (
                          id INTEGER NOT NULL,
                	      {col1} {typ1} NOT NULL,
                   	      {col2} {typ2} NOT NULL,
                	      {col3} {typ3} NOT NULL,
                          {col4} {typ4} NOT NULL,
                          PRIMARY KEY (id)
                          );
                      """


    d['simple_select'] = """
                         SELECT {0} FROM {1}
                         WHERE {2}
                         ORDER BY {3};
                         """
    return d   # [key]
