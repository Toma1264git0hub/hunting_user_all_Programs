This Python script is a username availability scanner for multiple social media platforms. It generates random usernames based on various predefined patterns and checks if those usernames are available on platforms like TikTok, Facebook, Instagram, Telegram, GitHub, Discord, Snapchat, Twitter, Reddit, YouTube, Pinterest, and LinkedIn.

The script displays live statistics of found available usernames ("hits") and unavailable usernames ("bad") for each platform. When a username is found available, it sends a notification message to a specified Telegram bot and chat ID.

Features include:

Multiple username generation patterns (quadruple, triple, repeated characters, distinct characters, etc.)

Colorful animated console interface

Real-time update of hit/bad counts per platform

Telegram integration for alert notifications

Cross-platform compatibility (Windows/Linux)


Users input their Telegram bot token and chat ID, then select a username pattern to start scanning. The script continuously generates usernames, checks availability via HTTP requests, and reports results until manually stopped.
