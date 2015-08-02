# you need 2 pieces of data in order to insert a new row into the database, the MessageID and the Text (in the form of a byte string)
curs.execute("""INSERT INTO message(msgMessageID, msgText) VALUES (%s, %s)""",(message_id, text))
