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

global user_list_lock
global current_user_getting_job
global titles
global _id
user_list_lock = asyncio.Lock()
current_user_getting_job = None
titles = {"justice": [], "duke": [], "architect": [], "scientist": []}
_id = 0
duration = 30
token = "MTEwMDM2MTgyNTQ0MDIzOTY3Ng.Gvz3U-.cjhCXxzLs4kNjlqnaZiwJm55-yHRUjKW6oxMks"
guild_id = 1123944825125867602
channel_id = 1123944830628810753  # title channel

bot = lightbulb.BotApp(token=token, prefix="!", default_enabled_guilds=guild_id)

rok_bot = get_bot(3)


async def async_function(type, kingdom, x, y):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, rok_bot.title.run, type, kingdom, x, y)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print(current_user_getting_job)
    print("Bot is ready.")


async def waitForOwnClosure(ctx, type, current_user):
    global titles
    if current_user is None:
        return
    timer = duration
    while (len(titles[type]) >= 1 and current_user == titles[type][0]) and timer:
        print(f"Waiting for closure {type} from {current_user}")
        await asyncio.sleep(1)
        timer = timer - 1
    if current_user in titles[type]:
        print("Timer ended removing  the  user")
        titles[type].remove(current_user)
    if len(titles[type]) >= 1:
        for element in titles[type]:
            print(f"{element}")
        print(f"{titles[type] =}")
        print(f"{current_user =}")
        await ctx.respond(f"⏰ Timer ended for {current_user['mention']}!")
    print(len(titles[type]))


async def waitForMyTurn(type, current_user):
    global titles
    if current_user is None:
        return
    timer = duration
    while current_user != titles[type][0]:
        print(f"{type} | Waiting for my turn {current_user}")
        await asyncio.sleep(1)
        timer = timer - 1


@bot.command()
@lightbulb.option("y", "City Y location", type=int)
@lightbulb.option("x", "City X location", type=int)
@lightbulb.option("kingdom", "Your kingdom (#1111)", type=str)
@lightbulb.option("title", "(justice|duke|architect|scientist)", type=str)
@lightbulb.command(name="title", description="Ask for your title")
@lightbulb.implements(lightbulb.SlashCommand)
async def title(ctx: lightbulb.Context):
    global current_user_getting_job
    global titles
    global _id
    global user_list_lock

    user = ctx.author
    title = ctx.options.title.lower()
    print(title)
    titles[title].append(
        {
            "id": _id,
            "user_id": user.id,
            "username": str(user),
            "mention": user.mention,
            "kd": ctx.options.kingdom,
            "x": ctx.options.x,
            "y": ctx.options.y,
            "time": time.time(),
        }
    )

    print(titles)
    current_user = titles[title][-1]
    _id += 1

    await ctx.respond(await whereAmI(title, current_user["user_id"]))
    print(f"Request added {titles[title]}")

    await waitForMyTurn(title, current_user)
    await user_list_lock.acquire()
    current_user_getting_job = current_user
    print(f"✅ Job started for {current_user['username']} ({current_user['id']})")
    await async_function(
        title, current_user["kd"], current_user["x"], current_user["y"]
    )
    print(f"❌ Job ended for {current_user['username']} ({current_user['id']})")
    user_list_lock.release()
    await ctx.respond(await send(title, current_user["username"]))
    await waitForOwnClosure(ctx, title, current_user)


@bot.command()
@lightbulb.option("title", "(justice|duke|architect|scientist)", type=str)
@lightbulb.command(name="done", description="Remove yourself from the waiting list")
@lightbulb.implements(lightbulb.SlashCommand)
async def done(ctx: lightbulb.Context):
    user = ctx.author

    for i, user_info in enumerate(titles[ctx.options.title]):
        if user_info["user_id"] == user.id:
            del titles[ctx.options.title][i]
            return await ctx.respond(
                f"{user_info['mention']}✅ Successfully removed you ({user_info['username']}) from {ctx.options.title.capitalize()} queue"
            )
    return await ctx.respond(f"{user.mention}❌ You are not in the list!")


@bot.command()
@lightbulb.option("title", "(justice|duke|architect|scientist)", type=str)
@lightbulb.command(name="where", description="Get your queue position")
@lightbulb.implements(lightbulb.SlashCommand)
async def where(ctx: lightbulb.Context):
    user = ctx.author

    for i, user_info in enumerate(titles[ctx.options.title]):
        if user_info["user_id"] == user.id:
            return await ctx.respond(await whereAmI(ctx.options.title, user.id))
    return await ctx.respond(await whereAmI(ctx.options.title, user.id))


async def send(type, username):
    embed = hikari.Embed(
        title=f"🎉 {username} is now {type.capitalize()}",
        description=f"**{type.capitalize()} Queue**: {len(titles[type])}\n**Duration**: {duration} sec",
        color=0x00FF00,  # Green color
    )
    return embed


async def whereAmI(type, user_id):
    embed = hikari.Embed(
        title=f"{type.capitalize()} Queue",
        description=f"👉 **Your Position**: {getPos(type, user_id)}",
        color=0x00FF00,  # Green color
    )
    return embed


def getPos(type, user_id):
    i = 0
    for element in titles[type]:
        i += 1
        if element["user_id"] == user_id:
            return i
    return -1


bot.run()
