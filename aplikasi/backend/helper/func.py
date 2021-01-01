from aplikasi.backend.database.conn import connect
import datetime
from instance.config import SECRET_KEY, PERMANENT_SESSION_LIFETIME
import jwt


def makeToken(user_id, skey=SECRET_KEY):
    token = jwt.encode(
        {
            "user_id": user_id,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + PERMANENT_SESSION_LIFETIME,
        },
        skey,
        algorithm="HS256",
    )

    return token.decode("UTF-8")
