import discord

from utils.functions import FileSingleton

token = "MTEwMDM2MTgyNTQ0MDIzOTY3Ng.Gvz3U-.cjhCXxzLs4kNjlqnaZiwJm55-yHRUjKW6oxMks"


async def send_discord_message(name, message, path):
    file_Manager = FileSingleton()
    data = file_Manager.get_data()
    user_id = data["discord"]["user_id"]
    if not user_id:
        return
    intents = discord.Intents.default()
    intents.messages = True  # Enable the messages intent

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        try:
            user = await client.fetch_user(user_id)

            if user:
                file = discord.File(path, filename=path)

                embed = discord.Embed(
                    title=f"Error on {name}", description=message, color=0xFF0000
                )
                embed.set_image(url="attachment://" + path)
                await user.send(embed=embed, file=file)
                print(f"Message sent to user {user.name} ({user.id})")
            else:
                print(f"User with ID {user_id} not found!")

            await client.close()

        except discord.LoginFailure:
            print("Invalid token. Failed to log in.")
        except discord.HTTPException as e:
            print(f"Failed to send the message: {e}")

    await client.start(token)
