# Flask-Wepay

This extension provides a simple wrapper for WePay's Python API.

## Installation

`$pip install flask-wepay`

## Usage

Provide your API key in your app's config file. The following may be set:

`WEPAY_CONSUMER_KEY`
`WEPAY_CONSUMER_SECRET`
`WEPAY_IN_PRODUCTION`
`WEPAY_ACCESS_TOKEN`

Now in order to initialize the WePay object we pass the app object to it as
follows:
    
    from flask import Flask
    from flaskext.wepay import WePay
    
    app = Flask(__name__)
    wepay = WePay(app)

The API of the WePay Python API is now exposed via this object. The following
methods are available:

    wepay.call(uri, params, token)
    
    wepay.get_authorization_urls(redirect_uri, options, scope)
    
    wepay.get_token(redirect_uri, code)
