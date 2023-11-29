import asyncio
import inspect
import os
import sys
import time

import hikari
import lightbulb

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from _debugger import get_bot

titles = {"justice": [], "duke": [], "architect": [], "scientist": []}

token = "MTEwMDM2MTgyNTQ0MDIzOTY3Ng.Gvz3U-.cjhCXxzLs4kNjlqnaZiwJm55-yHRUjKW6oxMks"
guild_id = 1123944825125867602
channel_id = 1123944830628810753  # title channel

duration = 5 * 60

bot = lightbulb.BotApp(token=token, prefix="!", default_enabled_guilds=guild_id)

user_list_lock = asyncio.Lock()

bot_rok = get_bot(3)


async def async_function(type, kingdom, x, y):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, bot_rok.title.run, type, kingdom, x, y)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot is ready.")


async def waitForClosure(type, current_user):
    timer = duration
    while current_user in titles[type] and timer:
        await asyncio.sleep(1)
        timer = timer - 1
    if current_user in titles[type]:
        titles[type].remove(current_user)


@bot.command()
@lightbulb.option("y", "City Y location", type=int)
@lightbulb.option("x", "City X location", type=int)
@lightbulb.option("kingdom", "Your kingdom (#1111)", type=str)
@lightbulb.option("title", "(justice|duke|architect|scientist)", type=str)
@lightbulb.command(name="title", description="Ask your title there")
@lightbulb.implements(lightbulb.SlashCommand)
async def title(ctx: lightbulb.Context):
    user = ctx.author
    title = ctx.options.title.lower()

    if title not in titles:
        await ctx.respond(
            "You may have misspelled your title request. Unable to proceed."
        )

    titles[title].append(
        {
            "user_id": user.id,
            "username": str(user),
            "mention": user.mention,
            "kd": ctx.options.kingdom,
            "x": ctx.options.x,
            "y": ctx.options.y,
            "time": time.time(),
        }
    )

    await ctx.respond(await add_to_queue(title, user.username))

    current_user = titles[title][0]

    if current_user["time"] + duration < time.time() and len(titles[title]) >= 2:
        current_user = titles[title][1]

        # await ctx.respond(f"{previous_user['mention']} is out of time! Giving it to {current_user['username']}.")

        print(f"Job started for {current_user['username']}")

        if await async_function(
            title, current_user["kd"], current_user["x"], current_user["y"]
        ):
            await ctx.respond(
                f"{title} is now assigned to {current_user['username']} for {duration} sec."
            )
            await ctx.respond(await get_current_queue(title))
        else:
            await ctx.respond(
                f"Unable to assign {title.capitalize()} to {current_user['username']}."
            )
            await ctx.respond(await get_current_queue(title))

        await waitForClosure(title, current_user)

        print(f"Job ended for {current_user['username']}")

    elif len(titles[title]) == 1:
        # await ctx.respond(f"The list is empty. Assigning {title} to {current_user['username']}.")

        print(f"Job started for {current_user['username']}")

        if await async_function(
            title, current_user["kd"], current_user["x"], current_user["y"]
        ):
            await ctx.respond(
                f"{title} is now assigned to {current_user['username']} for {duration} sec."
            )
        else:
            await ctx.respond(
                f"Unable to assign {title.capitalize()} to {current_user['username']}."
            )
        print(f"Job ended for {current_user['username']}")

        await waitForClosure(title, current_user)


@bot.command()
@lightbulb.option("title", "(justice|duke|architect|scientist)", type=str)
@lightbulb.command(name="done", description="Remove yourself from the waiting list")
@lightbulb.implements(lightbulb.SlashCommand)
async def done(ctx: lightbulb.Context):
    if ctx.channel_id != channel_id:
        return

    user = ctx.author
    found = False

    for i, user_info in enumerate(titles[ctx.options.title]):
        if user_info["user_id"] == user.id:
            titles[ctx.options.title].remove(i)
            found = True
            break

    if found:
        await ctx.respond(f"{user.username}, you have been removed from the list.")
        await ctx.respond(await get_current_queue(titles[ctx.options.title]))
    else:
        await ctx.respond(f"{user.username}, you are not currently in the list.")


async def add_to_queue(type, username):
    embed = hikari.Embed(
        title=f"{type.capitalize()} Request Added from {username}",
        description=f"**Queue Position**: {len(titles[type])}\n**Duration**: {duration} sec",
        color=0x00FF00,  # Green color
    )
    return embed


async def get_current_queue(type):
    embed = hikari.Embed(
        title=f"{type.capitalize()} Requests",
        description=f"**Waiting queue**: {len(titles[type])}\n**Duration**: {duration} sec",
        color=0x00FF00,  # Green color
    )
    return embed


bot.run()
