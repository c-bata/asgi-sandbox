import asyncio
import time

from django.http import HttpResponse


async def hello(request):
    await asyncio.sleep(1.0)
    return HttpResponse('Hello, async world!')


def sync_hello(request):
    time.sleep(1.0)
    return HttpResponse('Hello, sync world!')
