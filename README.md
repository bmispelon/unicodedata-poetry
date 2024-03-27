# unicodedata-poetry

The code for the bot at https://botsin.space/@unicodedatapoetry (running on Digital Ocean serverless)


## Initial setup

```
# 1. create a DO "namespace" for the function to live in
# use `doctl serverless namespaces list-regions` to get a list of available regions
doctl serverless namespaces create --label YOUR_NAMESPACE_LABEL --region ams3

# 2. create the .env file with your mastodon api secrets
# you get those by creating an "application" in the "Development" tab of your
# mastodon preferences page
cp .env.example .env
```


## Deploying the function

```
doctl serverless deploy .
```
