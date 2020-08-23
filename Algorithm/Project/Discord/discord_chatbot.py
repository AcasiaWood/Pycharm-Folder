import discord

# a token to work a bot.
token = 'To protect personal information, tokens have not been entered.'

# define bot`s function.
class MyClient(discord.Client):

    # a working function when discord bot is working.
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # send "hello" to other users.
    async def hello(self, message):
        await message.channel.send('Hello, {0.author}. Nice to Meet You!'.format(message))

    # follow code is sending message specially.
    async def follow(self, message):
        try:
            repeat_txt = message.content.replace('#follow', '')
            await message.channel.send(repeat_txt)
        except discord.errors.HTTPException:
            await message.channel.send('There is Nothing to Say.')

    # show the members.
    async def show_user_list(self, message):
        msg = ''
        member_list = message.channel.members
        for member in member_list:
            msg += member.name + '\n'
        await message.channel.send(msg)

    # clear all message.
    async def clear_message(self, message):
        arg = message.content.split(sep=' ')
        try:
            value = int(arg[1])
            await message.channel.purge(limit=value)
        except ValueError:
            await message.channel.send('Invalid Command Format. \nCorrect Format: #Clear [Number]')
        except IndexError:
            await message.channel.send('Enter the number of chats to delete. \nCorrect Format: #Clear [Number]')

    # a working function when discord bot is pushing the message.
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        msg = message.content.split(' ')[0]
        if msg.startswith('#'):
            if 'hello' in msg:
                await self.hello(message)
            elif 'follow' in msg:
                await self.follow(message)
            elif 'picture' in msg:
                await message.channel.send(file=discord.File('python.png'))
            elif 'show_member' in msg:
                await self.show_user_list(message)
            elif 'clear_message' in msg:
                await self.clear_message(message)
            elif 'bot_logout' in msg:
                await client.logout()

# create a bot client.
client = MyClient()

# start a bot.
client.run(token)
