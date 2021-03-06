# "javascript" section for javascript. see @app.route('/config.js') in app/views.py

# oauth constants
HOSTNAME = "http://hackathon.chinacloudapp.cn"  # host name of the UI site
QQ_OAUTH_STATE = "openhackathon"  # todo state should be constant. Actually it should be unguessable to prevent CSFA
HACkATHON_API_ENDPOINT = "http://hackathon.chinacloudapp.cn:15000"

Config = {
    "environment": "local",
    "login": {
        "github": {
            "access_token_url": 'https://github.com/login/oauth/access_token?client_id=a10e2290ed907918d5ab&client_secret=5b240a2a1bed6a6cf806fc2f34eb38a33ce03d75&redirect_uri=%s/github&code=' % HOSTNAME,
            "user_info_url": 'https://api.github.com/user?access_token=',
            "emails_info_url": 'https://api.github.com/user/emails?access_token='
        },
        "qq": {
            "access_token_url": 'https://graph.qq.com/oauth2.0/token?grant_type=authorization_code&client_id=101192358&client_secret=d94f8e7baee4f03371f52d21c4400cab&redirect_uri=%s/qq&code=' % HOSTNAME,
            "openid_url": 'https://graph.qq.com/oauth2.0/me?access_token=',
            "user_info_url": 'https://graph.qq.com/user/get_user_info?access_token=%s&oauth_consumer_key=%s&openid=%s'
        },
        "gitcafe": {
            "access_token_url": 'https://api.gitcafe.com/oauth/token?client_id=25ba4f6f90603bd2f3d310d11c0665d937db8971c8a5db00f6c9b9852547d6b8&client_secret=e3d821e82d15096054abbc7fbf41727d3650cab6404a242373f5c446c0918634&redirect_uri=%s/gitcafe&grant_type=authorization_code&code=' % HOSTNAME
        },
        "provider_enabled": ["github", "qq", "gitcafe"],
        "session_minutes": 60,
        "token_expiration_minutes": 60 * 24
    },
    "hackathon-api": {
        "endpoint": HACkATHON_API_ENDPOINT
    },
    "javascript": {
        "renren": {
            "clientID": "client_id=7e0932f4c5b34176b0ca1881f5e88562",
            "redirect_url": "redirect_uri=%s/renren" % HOSTNAME,
            "scope": "scope=read_user_message+read_user_feed+read_user_photo",
            "response_type": "response_type=token",
        },
        "github": {
            "clientID": "client_id=a10e2290ed907918d5ab",
            "redirect_uri": "redirect_uri=%s/github" % HOSTNAME,
            "scope": "scope=user",
        },
        "google": {
            "clientID": "client_id=304944766846-7jt8jbm39f1sj4kf4gtsqspsvtogdmem.apps.googleusercontent.com",
            "redirect_url": "redirect_uri=%s/google" % HOSTNAME,
            "scope": "scope=https://www.googleapis.com/auth/userinfo.profile+https://www.googleapis.com/auth/userinfo.email",
            "response_type": "response_type=token",
        },
        "qq": {
            "clientID": "client_id=101192358",
            "redirect_uri": "redirect_uri=%s/qq" % HOSTNAME,
            "scope": "scope=get_user_info",
            "state": "state=%s" % QQ_OAUTH_STATE,
            "response_type": "response_type=code",
        },
        "gitcafe": {
            "clientID": "client_id=25ba4f6f90603bd2f3d310d11c0665d937db8971c8a5db00f6c9b9852547d6b8",
            "clientSecret": "client_secret=e3d821e82d15096054abbc7fbf41727d3650cab6404a242373f5c446c0918634",
            "redirect_uri": "redirect_uri=http://hackathon.chinacloudapp.cn/gitcafe",
            "response_type": "response_type=code",
            "scope": "scope=public"
        },
        "hackathon": {
            "name": "open-xml-sdk",
            "endpoint": HACkATHON_API_ENDPOINT
        }
    }
}



