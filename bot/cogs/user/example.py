import discord
from discord.ext import commands


class ExampleCommands(commands.Cog):  # noqa: D101
    def __init__(self, bot: commands.Bot) -> None:  # noqa: D107
        self.bot = bot

    @discord.command(name="hello", description="Приветствие!")
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"Hello, {ctx.author.name}")

    @discord.command(
        name="plusaction",
        description="Сложите два числа!"
    )
    async def plus(
        self,
        ctx: discord.ApplicationContext,
        a: discord.Option(int, description="Первое число"),
        b: discord.Option(int, description="Второе число")
    ):
        await ctx.respond(f"Result: {a + b}")

    @discord.command(name="ping", description="Проверьте свой пинг!")
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"Pong! {round(self.bot.latency*1000)}ms")
