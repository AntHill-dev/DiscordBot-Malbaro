from typing import Any

import discord


class PrivateVoiceControllerRenameModal(discord.ui.Modal):
    def __init__(self, listener_cog: Any) -> None:
        input_text = discord.ui.InputText(
            placeholder="Новое название личного голосового канала",
            label="Название голосового канала",
        )
        super().__init__(input_text, title="Переименование голосового канала")

        self.listener_cog = listener_cog

    async def callback(self, interaction: discord.Interaction) -> None:
        user = interaction.user._user
        if user.name not in self.listener_cog._private_channels:
            await interaction.response.send_message("Вы не в своем личном приватном голосовом канале!", ephemeral=True)
            return

        voice_channel = await self.listener_cog.get_voice_channel_by_id(self.listener_cog._private_channels[user.name])
        self.listener_cog._private_channels[user.name] = (await voice_channel.edit(name=self.children[0].value)).id
        await interaction.response.send_message("Личный голосовой канал был успешно переименован!", ephemeral=True)


class PrivateVoiceControllerLimitModal(discord.ui.Modal):
    def __init__(self, listener_cog: Any) -> None:
        input_text = discord.ui.InputText(
            placeholder="Новое значение",
            label="Новое кол-во слотов для голосового канала",
            style=discord.InputTextStyle.long,
        )
        super().__init__(input_text, title="Кол-во слотов голосового канала")

        self.listener_cog = listener_cog

    async def callback(self, interaction: discord.Interaction) -> None:
        user = interaction.user._user
        if user.name not in self.listener_cog._private_channels:
            await interaction.response.send_message("Вы не в своем личном приватном голосовом канале!", ephemeral=True)
            return

        voice_channel = await self.listener_cog.get_voice_channel_by_id(self.listener_cog._private_channels[user.name])
        self.listener_cog._private_channels[user.name] = (await voice_channel.edit(
            user_limit=int(self.children[0].value),
        )).id
        await interaction.response.send_message("Кол-во слотов было успешно изменено!", ephemeral=True)


class PrivateVoiceControllerView(discord.ui.View):
    """Private voice controller view."""

    def __init__(self, listener_cog: Any) -> None:
        super().__init__(timeout=None)
        self.listener_cog = listener_cog

    @discord.ui.button(custom_id="private-voice:limit-add", style=discord.ButtonStyle.primary, row=1, emoji="➕")
    async def add_slot_to_limit(self, button, interaction) -> None:
        user = interaction.user._user

        if user.name not in self.listener_cog._private_channels:
            await interaction.response.send_message("Вы не в своем личном приватном голосовом канале!", ephemeral=True)

        voice_channel = await self.listener_cog.get_voice_channel_by_id(self.listener_cog._private_channels[user.name])
        self.listener_cog._private_channels[user.name] = (await voice_channel.edit(user_limit=voice_channel.user_limit + 1)).id
        await interaction.response.send_message("Один слот был успешно добавлен!", ephemeral=True)

    @discord.ui.button(custom_id="private-voice:limit-remove", style=discord.ButtonStyle.primary, row=1, emoji="➖")
    async def remove_slot_in_limit(self, button, interaction) -> None:
        user = interaction.user._user

        if user.name not in self.listener_cog._private_channels:
            await interaction.response.send_message("Вы не в своем личном приватном голосовом канале!", ephemeral=True)
            return

        voice_channel = await self.listener_cog.get_voice_channel_by_id(self.listener_cog._private_channels[user.name])
        new_limit = voice_channel.user_limit - 1
        if new_limit < 1:
            await interaction.response.send_message(
                "Количество слотов обязательно должно быть больше 0!",
                ephemeral=True,
            )
            return

        self.listener_cog._private_channels[user.name] = (await voice_channel.edit(user_limit=new_limit)).id
        await interaction.response.send_message("Один слот был успешно удалён!", ephemeral=True)

    @discord.ui.button(custom_id="private-voice:open", style=discord.ButtonStyle.primary, row=2, emoji="🔐")
    async def open(self, button, interaction) -> None:
        user = interaction.user._user

        if user.name not in self.listener_cog._private_channels:
            await interaction.response.send_message("Вы не в своем личном приватном голосовом канале!", ephemeral=True)
            return

        voice_channel: discord.VoiceChannel = await self.listener_cog.get_voice_channel_by_id(self.listener_cog._private_channels[user.name])

        self.listener_cog._private_channels[user.name] = (await voice_channel.edit(
            overwrites={
                role: discord.PermissionOverwrite(connect=True)
                for role in voice_channel.guild.roles
            },
        )).id

        await interaction.response.send_message(
            "Доступ в ваш приватный голосовой канал был успешно открыт!",
            ephemeral=True,
        )

    @discord.ui.button(custom_id="private-voice:close", style=discord.ButtonStyle.primary, row=2, emoji="🔒")
    async def close(self, button, interaction) -> None:
        user = interaction.user._user

        if user.name not in self.listener_cog._private_channels:
            await interaction.response.send_message("Вы не в своем личном приватном голосовом канале!", ephemeral=True)
            return

        voice_channel = await self.listener_cog.get_voice_channel_by_id(self.listener_cog._private_channels[user.name])
        self.listener_cog._private_channels[user.name] = (await voice_channel.edit(
            overwrites={
                role: discord.PermissionOverwrite(connect=False)
                for role in voice_channel.guild.roles
            },
        )).id

        await interaction.response.send_message("Ваш приватный голосовой канал был успешно закрыт!", ephemeral=True)

    @discord.ui.button(label="Изменить имя", custom_id="private-voice:rename", style=discord.ButtonStyle.primary, row=3)
    async def rename(self, button, interaction: discord.Interaction) -> None:
        user = interaction.user._user

        if user.name not in self.listener_cog._private_channels:
            await interaction.response.send_message("Вы не в своем личном приватном голосовом канале!", ephemeral=True)
            return

        await interaction.response.send_modal(PrivateVoiceControllerRenameModal(self.listener_cog))

    @discord.ui.button(label="Изменить кол-во слотов", custom_id="private-voice:limit", style=discord.ButtonStyle.primary, row=3)
    async def limit(self, button, interaction: discord.Interaction) -> None:
        user = interaction.user._user

        if user.name not in self.listener_cog._private_channels:
            await interaction.response.send_message("Вы не в своем личном приватном голосовом канале!", ephemeral=True)
            return

        await interaction.response.send_modal(PrivateVoiceControllerLimitModal(self.listener_cog))
