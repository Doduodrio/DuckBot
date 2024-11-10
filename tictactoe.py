import datetime
import discord

data = range(1, 11)
page = 0

def get_embed():
    embed = discord.Embed(
        color = discord.Color.dark_teal(),
        title = 'This is a test',
        description = f'The number is {data[page]}',
        timestamp = datetime.datetime.now()
    )
    embed.add_field(name='', value=f'Page {page} of {len(data)}')

    return embed

class MyView(discord.ui.View):
    async def send(self, message: discord.Message):
        self.message = await message.channel.send(embed=get_embed(), view=self)
    
    async def update(self):
        await self.message.edit(embed=get_embed(), view=self)