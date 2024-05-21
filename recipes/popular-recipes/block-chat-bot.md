# Блокировка чат-ботов

Для блокировки ресурсов, взаимодействующих с чат-ботами, потребуется создать правило в Контент-фильтре:

1\. Перейдите в раздел **Правила трафика -> Контент-фильтр -> Пользовательские категории**.

2\. Добавьте правило, заполнив следующие поля:

* **Название** - введите любое навзвание;
* **URL** - внесите список URL из блока ниже;
* **Комментарий** - заполнение не обязательно.

<details>

<summary>Список URL</summary>

```
chatgpt* 
ai.360.cn
aibot.ru 
ai.dedao.cn
ai.ls 
aiservice.vercel.app
aitianhu.com
anse.app
anthropic.com
b.ai-huan.xyz
bard.google.com
bard.google.com
bettergpt.chat
bing.com
bing.com
chadgpt.ru
character.ai
chat4gpt.ru 
chat9.yqcloud.top
chat.acytoo.com
chataigpt.org 
chat.ai-open.ru 
chatboxai.app
chat.dfehub.com
chat.getgpt.world
chatglm.cn
chatgp.ru 
chat.gpt4free.io 
chatgpt4rus.ru 
chatgpt.ai 
chatgptbot.ru 
chat-gpt.com
chatgptfree.ai 
chat-gpt-free.ru 
chatgptlogin.ac
chatgpt-me.ru 
chat-gpt-na.ru
chat-gpt-na.ru
chatgptnarusskom.ru 
chat-gpt.org
chatgpt.org
chatgpt.pro 
chat-gpt.ru 
chatgpt-telegram.com
chatgptweb.ru 
chathub.gg 
chatinfo.ru 
chat.lmsys.org
chat.openai.com
chat.ramxn.dev
chat.su
claude.ai
crfm.stanford.edu
deepai.org
easychat-ai.app
itbabushka.com 
forefront.com
freechatgpt.chat
free-chatgpt.ru
free.easychat.work
gpt2.ru 
gpt4all.io
gpt-chatbot.ru
gptchatbot.ru 
gptchatly.com
gpt-gm.h2o.ai
gptgo.ai
gpt-open.ru
gptschat.ru 
gradio.app
h2o.ai
huggingface.co
iask.ai 
liaobots.com
liftweb.ru 
lmsys.org
macgpt.com
mashagpt.ru 
moss.fastnlp.top
neice.tiangong.cn
openai.ru
openai-gpt.ru
openai-chat-gpt.ru 
open-assistant.io
opencat.app
petals.ml
play.vercel.ai
poe.com
ru-chatgpt.ru
rugpt.chat 
sdk.vercel.ai
supertest.lockchat.app
tenchat.ru 
theb.ai
timeai.ru 
tongyi.aliyun.com
tools.zmo.ai
trychatgpt.ru
wewordle.org
xinghuo.xfyun.cn
yandex-gpt.com
yandex-gpt.ru
yiyan.baidu.com
you.com
zhpt.tech
```

</details>

![](/.gitbook/assets/block-chat-bot.png)

4\. Сохраните правило.

3\. Перейдите на вкладку **Правила** и добавьте правило с действием **Запретить**:

![](/.gitbook/assets/block-chat-bot1.png)
