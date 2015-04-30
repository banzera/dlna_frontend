import sqlite3


CONN = sqlite3.connect('../files.db')


GENRES = '''
        SELECT GENRE
          FROM DETAILS 
      GROUP BY GENRE
'''

ARTISTS = '''
        SELECT ARTIST
          FROM DETAILS
      GROUP BY ARTIST
'''

ALBUMS = '''
        SELECT ALBUM
          FROM DETAILS
      GROUP BY ALBUM
'''

def genres():
    c = CONN.cursor()
    gg = [g[0] for g in c.execute(GENRES) if g[0] is not None]
    return {'genres': gg}


def artists():
    c = CONN.cursor()
    aa = [a[0] for a in c.execute(ARTISTS) if a[0] is not None]
    return {'artists': aa}


def albums():
    c = CONN.cursor()
    aa = [a[0] for a in c.execute(ALBUMS) if a[0] is not None]
    return {'albums': aa}


def items_in_genre(genre):

    p = (genre,)
    # c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    sql = '''
        SELECT NAME,CLASS,OBJECT_ID,PATH  
              FROM OBJECTS OB
         LEFT JOIN DETAILS DT
                ON OB.DETAIL_ID=DT.ID
             WHERE DT.GENRE=? AND
                   OB.CLASS<>'container.storageFolder' AND
                   PARENT_ID NOT LIKE '64%'
          ORDER BY OBJECT_ID
    '''

    c = CONN.cursor()
    
    ii = [{'name':name,
           'path':path} for name,clazz,oid,path
                         in c.execute(sql,p)]
    return {'items': ii}
    
