# How to use this package to create a BoondManager app

You can use this package to start to build a BoondManager application.

First of all, read the [quick start guides](https://support.boondmanager.com/hc/fr/articles/360027681152-Quick-start-Guides) to create an app.

For an app, you'll need to store the _app token_ on your side. The app token is sent during installation.

## Create your application on BoondManager

You'll need to create a registered application on BoondManager, to get an app token and enable available endpoints.

The next steps required that you have an administrator account.

Go to the Administration section > Developers space > Apps tab and click on the "Develop an app" button. The required informations are :

* Name : the name of your application, could be anything
* App code : a code for your application
* URL of the app : The url where your app lives. It should be accessible by BoondManager. It could be changed so you can use a dev url first.

The type of your app should be iFrame. You can enable a config page if you need (accessible at `/configuration` uri).

The most important, here, is to enable the API's endpoints you'll need to use.

There are many more things you can do, you can refer to the official documentation.

## Configure your application

After saving your application page, you'll get an app key. You'll need to store it on your side.

Your application needs at least 3 availables uri :

* `/install` : it's called by BoondManager when you click on the "Install" button. BoondManager checks that your application responds and sends a secret token that you'll need to save on your side.
* `/uninstall` : It's called when an administrator uninstalls your app on BoondManager and should be used to delete the token.
* Your homepage, entered in the url field. It's the page displayed on the iFrame.

As said before, you can set a configuration page.

If your application needs a frontend, you also need to use the [BoondManager SDK](https://ui.boondmanager.com/sdk/boondmanager.js). It's used to manage with the primary context of root document (like set the iframe dimensions).

```javascript
document.addEventListener("DOMContentLoaded", function() {
    BoondManager.setAutoResize();
});
```

When BoondManager tries to install your app, it sends an encoded payload that you can read with the `boondmanager.auth.decode_boondmanager_payload` function. It contains a lot of information that you'll need to store on your side.

By example, you can read this with the following `bottle` code :

```python
@route('/install', method='POST')
def install():
    signed_request = request.forms.get('signedRequest')
    payload = decode_boondmanager_payload(signed_request, BOONDMANAGER_APP_KEY)
    settings = {
        "client_token": payload.get('clientToken'),
        "client_name": payload.get('clientName'),
        "app_token": payload.get('appToken'),
        "refresh_token": payload.get('refreshToken'),
        "created_at": payload.get('createdAt'),
        "expires_in": payload.get('expiresIn'),
        "installation_code": payload.get('installationCode'),
        "issued_at": payload.get('issuedAt'),
        "expiration_date": payload.get('expirationDate'),
    }
    with open('settings.json', 'w', encoding='utf-8') as settings_file:
        json.dump(settings, settings_file)
    response_data = {'result': True}
    json.dumps(response_data)
```

When it's done, each time you'll display your application on the iFrame, BoondManager will also send a signedRequest query parameter that you can decode, to ensure that your application is displayed by BoondManager, and to get the current user token.

## Hello_app example

You can run the hello_app example to see how it works.

```bash
python hello_app.py
```
