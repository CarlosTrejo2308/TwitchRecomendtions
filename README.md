# TwitchRecommendations
Twitch Recommendations takes the name of the user name, and based on the stremers he follows, it will return at list of other streames that he might be interrested in following.

## How does it work?
First, it gets the list of all the streams that a particular user follows.
Then, it does the same for each of those stremres.
FInally it saves them in a list and it ponders a priority base on the number of followers divided the streamer has, divided by the number of streamers he follows.
