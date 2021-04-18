# Purpose

For the given Twitch video, the application draws a graph that shows average interactions (Twitch chat comments) for each segment of the video. Clicking at any point on the graph opens the video around that time.

# Pre-requisites

Existing Twitch Developer application that you have the client ID and secret for. This is used for downloading Twitch VOD chat logs.

# Usage

Running the program for the first time will copy `settings.json.reference` to `settings.json`.

Fill `client_id` and `client_secret` in `settings.json`.

Provide Twitch VOD URL or ID in the respective prompt. The program will download its chat logs, and draw a graph of the chat interactions. Clicking at any point of the graph opens the video around that time. Closing the graph will stop the program.

# Settings

`settings.json` properties:
* `client_id`: Twitch Developer application Client ID.
* `client_secret`: Twitch Developer application Client secret.
* `interval`: Average interactions are calculated for each interval (seconds).
* `neighbor`: Interactions are averaged with this range around the interval (seconds).
* `preview`: Clicking the graph to open the VOD at given time will open it by this earlier (seconds).

# Libraries

* Uses the following for downloading Twitch VOD chat logs: https://github.com/PetterKraabol/Twitch-Python
* Uses the following for drawing the graph: https://github.com/matplotlib/matplotlib