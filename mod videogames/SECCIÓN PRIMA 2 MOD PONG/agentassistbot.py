# https://deepgram.com/learn/build-an-agent-assist-bot-with-python

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyaudio
import asyncio
import websockets
import json
import logging
import time
time.clock = time.time

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

DEEPGRAM_API_KEY = "49487da472b947c8c91fd09b982dc80a310d408a"

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 8000

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

trainer.train([
   'Hi',
   'Hello',
   'I need to buy medication.',
   'Sorry you are not feeling well. How much medication do you need?',
   'Just one, please',
   'Medication added. Would you like anything else?',
   'No Thanks',
   'Your order is complete! Your delivery will arrive soon.'
])

audio_queue = asyncio.Queue()

def callback(input_data, frame_count, time_info, status_flag):
   audio_queue.put_nowait(input_data)
   return (input_data, pyaudio.paContinue)


async def microphone():
   audio = pyaudio.PyAudio()
   stream = audio.open(
       format = FORMAT,
       channels = CHANNELS,
       rate = RATE,
       input = True,
       frames_per_buffer = CHUNK,
       stream_callback = callback
   )

   stream.start_stream()

   while stream.is_active():
       await asyncio.sleep(0.1)

   stream.stop_stream()
   stream.close()

async def process():
   extra_headers = {
       'Authorization': 'token ' + DEEPGRAM_API_KEY
   }

   async with websockets.connect('wss://api.deepgram.com/v1/listen?encoding=linear16&sample_rate=16000&channels=1', extra_headers = extra_headers) as ws:
       async def sender(ws):
           try:
               while True:
                   data = await audio_queue.get()
           except Exception as e:
               print('Error while sending: ', str(e))
               raise

       async def receiver(ws):
           async for msg in ws:
               msg = json.loads(msg)
               transcript = msg['channel']['alternatives'][0]['transcript']

               if transcript:
                   print('Customer(you):', transcript)

                   if transcript.lower() == "okay":
                       print('Agent: bye')
                       break
                   else:
                       response=bot.get_response(transcript)
                       print('Agent:', response)

       await asyncio.wait([
           asyncio.ensure_future(microphone()),
           asyncio.ensure_future(sender(ws)),
           asyncio.ensure_future(receiver(ws))
       ])


def main():
   asyncio.get_event_loop().run_until_complete(process())

if name == '__main__':
   main()
