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