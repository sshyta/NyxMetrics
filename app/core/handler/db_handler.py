import psycopg2
import bcrypt

def login(user_login, password, signal):
    try:
        con = psycopg2.connect(dbname='NyxMetric', user='postgres', password='467912', host='127.0.0.1')
        cur = con.cursor()

        cur.execute("SELECT * FROM users WHERE login = %s;", (user_login,))
        value = cur.fetchall()

        if not value:
            signal.emit('Пользователь не найден')
            return
        
        stored_hash = value[0][2].encode('utf-8') # получение хэша из бд (2 столбец таблицы) 
        input_password_bytes = password.encode('utf-8') # перевод введенного пароля в байты

        if bcrypt.checkpw(input_password_bytes, stored_hash): # проверка хэша
            signal.emit('Успешная авторизация')
        else:
            signal.emit('Неверный пароль!')

    except Exception as e:
        signal.emit(f'Ошибка при авторизации: {str(e)}') 
    finally:
        cur.close()
        con.close()

def register(user_login, password, signal):
    try:
        con = psycopg2.connect(dbname='NyxMetric', user='postgres', password='467912', host='127.0.0.1')
        cur = con.cursor()

        cur.execute("SELECT * FROM users WHERE login = %s;", (user_login,))
        value = cur.fetchall()

        if value:
            signal.emit('Такой логин уже используется!')
        else:
            # хэшируем пароль перед сохранением в бд  
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            # INSERT INTO users (login, user_pass) VALUES (%s, crypto(%s, gen_salt('md5')));
            cur.execute("INSERT INTO users (login, user_pass) VALUES (%s, %s);", (user_login, password_hash))
            con.commit()
            signal.emit('Вы успешно зарегистрированы!')

    except Exception as e:
        con.rollback() 
        signal.emit(f'Ошибка при регистрации: {str(e)}')  
    finally:
        cur.close()
        con.close()