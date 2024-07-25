# A guide to adding a simple Discord bot to a server
0. Go to the Discord Developer Portal
1. Create a new application
![Create a new application](/add-bot-readme/1-create-app-button.png)
2. Name your application and agree to Discord's Developer Terms of Service
![Name your application](/add-bot-readme/2-create-app-dialog.png)
3. Go to the "Installation" tab and remove the install link
![Remove the install link](/add-bot-readme/3-turn-off-install-link.png)
4. Go to the "Bot" tab and turn off "Public Bot" (If you want to keep your bot private to you) and turn on "Message Content Intent" then hit Save.
![Turn off Public Bot](/add-bot-readme/4-turn-off-public-and-turn-on-message-intent.png)
5. Click on `Reset Token` to obtain your bot token
> [!IMPORTANT]
> Do NOT share your bot token with anyone. It is the equivalent of a password and they will steal your bot and do nefarious things.
![Reset Token](/add-bot-readme/5-reset-to-obtain-token.png)
![Reset Confirmation](/add-bot-readme/5.1-reset-confirm.png)
> [!NOTE]
> If your account has 2FA enabled, you will need to enter your 2FA code to reset the token.
![2FA Code](/add-bot-readme/5.2-2fa-reset.png)
6. Copy the token and paste it somewhere safe (or in this case the `.env` file)
![Copy Token](/add-bot-readme/6-copy-token.png)
7. Go to the "OAuth2" tab and select "bot" and "applications.commands" under "OAuth2 URL Generator". Then, scroll down and set the permissions you want your bot to have. Then click the copy button and paste the link into your browser.
![Invite Bot](/add-bot-readme/7-application-scope.png)
![Invite Bot](/add-bot-readme/7.1-add-bot-link.png)
8. Select the server you want to add the bot to and click "Authorize"
![Authorize Bot](/add-bot-readme/8-select-server.png)
> [!NOTE]
> Complete the captcha if shown
![Captcha](/add-bot-readme/8.1-captcha.png)
9. You should see a success message. Click "X" to close the window.
![Success](/add-bot-readme/9-done.png)