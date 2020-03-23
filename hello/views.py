import asyncio

from django.http import HttpResponse


async def hello(request):
    await asyncio.sleep(0.5)
    return HttpResponse('Hello, async world!')
