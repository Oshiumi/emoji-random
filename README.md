# emoji-random

Emoji-random is a [slash command in slack](https://api.slack.com/slash-commands) by [Google Cloud Funcitons](https://cloud.google.com/functions/?hl=ja) to post emojis at random.

## Usage

```
/emoji-random [pattern] [count]
```

A pattern is a regular expression.

## Deploy

```
gcloud beta functions deploy emoji-random \
    --memory=128MB \
    --runtime=python37 \
    --trigger-http \
    --entry-point=emoji_random \
    --set-env-vars SLACK_TOKEN=YOUR_TOKEN \
    --source .
```
