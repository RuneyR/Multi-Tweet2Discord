 The basic gist of this program is to read twitter names from a file and basically post specific, live, content from
those accounts. The program access a user's twitter account to do so. It can only see who the account is following. It
does not RT or like, only looks. It DOES post to discord via webhooks. With this, you can have many twitter accounts
being followed, and whenever new content is posted (has to be original tweet WITH MEDIA), it'll post to the supplied
Discord Webhooks.
    The program needs permissions and be in a place on the computer where it can Read and Write files. The user
will also need to supply Twitter API keys and Access Tokens. The account using the Access tokens must be following
the accounts you want to be followed and posted to Discord!
    At a fresh run, the program will create two files. ACCESS.txt and API.txt. Do not change the names.
Instructions will be written, follow them. API.txt will need the API keys or consumer keys/secrets. Similar to it,
ACCESS.txt needs access tokens.
    Only the 2nd and 4th line should be replaced in these files. Do not modify the file in any other way. Both files
should only have 4 lines!

    The code will run once more. It will use the accounts friends list and generate a FRIENDS.txt file. Here, the order
of the content structure is as follows:

Twitter Name
Twitter ID
Replace with Discord webhook URl....
END

    This will repeat for how many friends the account has. What you need to do is replace the proper line with a Discord
webhook. If you want one Twitter account status's to be posted to multiple/more than one webhook, then simply add
Webhook URL as new line after their TwitterID but Before the END line. Example:

Mark
0123456
DiscordWebhookURL1
DIscordWebhookURL2
DiscordWebhookURLN...
...
END

    If you wish to exclude an account from ever being listened to/being posted to Discord, delete their section. Basically,
delete the name,id, replace line and END lines.

    The program does take a command arguments. --reprint or --rp will reprint Friends.txt as it usually does, but without
deleting the original file by appending reprint. In other words, using the argument --reprint or --rp will make a txt
similar in structure and purpose of FRIENDS.txt but without deleting FRIENDS.txt, as the file created will be named
reprintFRIENDS.txt. This way, the original file is kept untouched and the user can modify the reprint, or simply take
information from it, as they may have added more people to follow and would like to see the tweets in Discord.
Note that this will override any reprintFRIENDS.txt files.
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
