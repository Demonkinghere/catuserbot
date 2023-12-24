from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 17989550
    API_HASH = "73fb532f0d1655071362f0384313da0a"
    # the name to display in your alive message
    ALIVE_NAME = "Mohit"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://trtyxill:Ho5FYG6tNmiI6lEzVhFHJg0aPHKxFYLp@drona.db.elephantsql.com/trtyxill"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOIgBuwyDQATMYiOd_Ll-FO6_-d4swJwORQf09i9SKmJNdPWlucTGt9BtnDG1mISaSjB8kUnvKPwIqts0pmqYe9_Zgb_oHjGHcZF5uDL_za2g-QnXLOdJe1kLAnfNNiIfyBSsAypN0vGkEb-m3T2yRUQQG23G5FNSNsRcRy_WDFHkkcMCdrUlXjaJxyRYl1Duv8avkEh71UrMMelVgWALaJ6scuBsTz7GstcoIBrVeuN1BrllxrmHdAM-eyA506Yk4w2PAyYr_gG0ouczDHyOVExDFLqNjAS3-ZX63eRIQbpJ7JPOUxPq1h0uShcJ2Fq_M07b850SvLxWhBV0vBALDYPtWsY="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6972990380:AAEZyUh5XfU5R1ClnRM07LWjl-kef-Af7Fo"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002102378431
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"